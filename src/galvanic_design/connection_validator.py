import os
import json
import logging
from pathlib import Path
from typing import Dict, List, Optional, Tuple, Set, Any, Union

from galvanic import colored_logger
from galvanic_altium.project import AltiumProject
from galvanic_altium.utils import AltiumBasic
from galvanic_datasheets.datasheet_manager import DatasheetManager

logger = colored_logger(__file__)

class ConnectionValidator:
    """
    A class that validates connections in an Altium project against datasheet recommendations.
    
    This class analyzes an Altium project, finds datasheets for components, and checks if
    connections match the recommendations and precautions in the datasheets.
    """
    
    def __init__(self, project_source: Union[str, Dict, Path]):
        """
        Initialize the ConnectionValidator with an Altium project.
        
        Args:
            project_source: Either a GUID string for the Altium project, a path to a JSON file,
                           or a dictionary containing project data
        """
        self.logger = colored_logger(self.__class__.__name__)
        
        # Initialize project based on the type of project_source
        if isinstance(project_source, str):
            # Assume it's a GUID
            self.logger.info(f"Loading project from GUID: {project_source}")
            self.project = AltiumProject(project_source)
        elif isinstance(project_source, dict):
            # Assume it's project data
            self.logger.info("Loading project from provided data dictionary")
            self.project = self._create_project_from_dict(project_source)
        elif isinstance(project_source, Path) or (isinstance(project_source, str) and os.path.exists(project_source)):
            # Assume it's a path to a JSON file
            path = Path(project_source) if isinstance(project_source, str) else project_source
            self.logger.info(f"Loading project from JSON file: {path}")
            with open(path, 'r') as f:
                project_data = json.load(f)
            self.project = self._create_project_from_dict(project_data)
        else:
            raise ValueError("project_source must be a GUID string, a dictionary, or a path to a JSON file")
        
        self.datasheet_manager = DatasheetManager
        self.validation_results = {}
    
    def _create_project_from_dict(self, project_data: Dict) -> AltiumBasic:
        """
        Create an AltiumProject-like object from a dictionary of project data.
        
        Args:
            project_data: Dictionary containing project data
            
        Returns:
            An object with the same interface as AltiumProject
        """
        # Create a simple object that mimics the AltiumProject interface
        class ProjectFromDict(AltiumBasic):
            def __init__(self, data):
                self.components = {}
                self.nets = {}
                
                # Load components
                if "components" in data:
                    for designator, comp_data in data["components"].items():
                        self.components[designator] = self._create_component(comp_data, designator)
                
                # Load nets
                if "nets" in data:
                    for name, net_data in data["nets"].items():
                        self.nets[name] = self._create_net(net_data, name)
            
            def _create_component(self, comp_data, designator):
                # Create a simple component object
                class ComponentFromDict(AltiumBasic):
                    def __init__(self, data, des):
                        self.designator = des
                        self.parameters = data.get("parameters", {})
                        self.avl = data.get("avl", [])
                        self.pins = {}
                        
                        # Load pins
                        if "pins" in data:
                            for pin_number, pin_data in data["pins"].items():
                                self.pins[pin_number] = self._create_pin(pin_data, pin_number)
                    
                    def _create_pin(self, pin_data, pin_number):
                        # Create a simple pin object
                        class PinFromDict(AltiumBasic):
                            def __init__(self, data, num):
                                self.number = num
                                self.name = data.get("pin_name", "")
                                self.connected_net = None
                                
                                # Set connected_net if available
                                net_name = data.get("connected_net")
                                if net_name:
                                    # This will be set later when nets are available
                                    self.connected_net = net_name
                        
                        return PinFromDict(pin_data, pin_number)
                
                return ComponentFromDict(comp_data, designator)
            
            def _create_net(self, net_data, name):
                # Create a simple net object
                class NetFromDict(AltiumBasic):
                    def __init__(self, data, net_name):
                        self.name = net_name
                        self.connected_pins = data.get("connected_pins", {})
                
                return NetFromDict(net_data, name)
            
            def get_component(self, designator):
                return self.components.get(designator)
        
        # Create the project object
        project = ProjectFromDict(project_data)
        
        # Link nets to pins
        for designator, component in project.components.items():
            for pin_number, pin in component.pins.items():
                if isinstance(pin.connected_net, str) and pin.connected_net in project.nets:
                    pin.connected_net = project.nets[pin.connected_net]
        
        return project
        
    def find_component_datasheet(self, component) -> Optional[Dict]:
        """
        Find the datasheet for a component using the DatasheetManager.
        
        Args:
            component: The component to find a datasheet for
            
        Returns:
            The datasheet JSON if found, None otherwise
        """
        # Try to find the datasheet using the component's AVL (Approved Vendor List)
        if component.avl:
            for manufacturer, part_number in component.avl:
                # Try to find an exact match for the part number
                if part_number in self.datasheet_manager.datasheets:
                    datasheet_dir = self.datasheet_manager._ROOT_DIR / part_number
                    return self.datasheet_manager.load_json_datasheet(datasheet_dir, prompt_for_source=False)
                
                # Try to find a match for the base part number (without package/variant)
                for ds_part_number in self.datasheet_manager.datasheets:
                    # Check if the datasheet part number is a substring of the component part number
                    # or vice versa (to handle different formatting)
                    if ds_part_number in part_number or part_number in ds_part_number:
                        datasheet_dir = self.datasheet_manager._ROOT_DIR / ds_part_number
                        return self.datasheet_manager.load_json_datasheet(datasheet_dir, prompt_for_source=False)
        
        # If no datasheet found by AVL, try using component parameters
        if "Part Number" in component.parameters:
            part_number = component.parameters["Part Number"]
            if part_number in self.datasheet_manager.datasheets:
                datasheet_dir = self.datasheet_manager._ROOT_DIR / part_number
                return self.datasheet_manager.load_json_datasheet(datasheet_dir, prompt_for_source=False)
            
            # Try to find a match for the base part number
            for ds_part_number in self.datasheet_manager.datasheets:
                if ds_part_number in part_number or part_number in ds_part_number:
                    datasheet_dir = self.datasheet_manager._ROOT_DIR / ds_part_number
                    return self.datasheet_manager.load_json_datasheet(datasheet_dir, prompt_for_source=False)
        
        self.logger.warning(f"No datasheet found for component {component.designator}")
        return None
    
    def validate_component_connections(self, component, datasheet) -> Dict:
        """
        Validate the connections of a component against its datasheet.
        
        Args:
            component: The component to validate
            datasheet: The datasheet JSON for the component
            
        Returns:
            A dictionary with validation results for each pin
        """
        results = {}
        
        # Skip if datasheet doesn't have pin information
        if "pins" not in datasheet:
            self.logger.warning(f"No pin information in datasheet for {component.designator}")
            return results
        
        # Get all nets in the project
        project_nets = self.project.nets
        
        # Validate each pin
        for pin_number, pin in component.pins.items():
            pin_name = pin.name
            
            # Skip if pin name is not in datasheet
            if pin_name not in datasheet["pins"]:
                self.logger.warning(f"Pin {pin_name} not found in datasheet for {component.designator}")
                continue
            
            pin_datasheet = datasheet["pins"][pin_name]
            pin_results = {
                "pin_name": pin_name,
                "pin_number": pin_number,
                "issues": [],
                "recommendations": [],
                "connected_net": pin.connected_net.name if pin.connected_net else None
            }
            
            # Skip if no implementation details in datasheet
            if "implementation" not in pin_datasheet:
                continue
            
            implementation = pin_datasheet["implementation"]
            
            # Check if pin is connected
            if not pin.connected_net:
                # Check if pin should be connected according to datasheet
                if "connectivity" in implementation and implementation["connectivity"]:
                    pin_results["issues"].append({
                        "type": "missing_connection",
                        "message": f"Pin {pin_name} should be connected according to datasheet"
                    })
            else:
                # Pin is connected, check if it follows datasheet recommendations
                connected_net = pin.connected_net
                connected_pins = connected_net.connected_pins
                
                # Check connected components
                if "connected_components" in implementation:
                    recommended_components = []
                    if isinstance(implementation["connected_components"], list):
                        for comp in implementation["connected_components"]:
                            if isinstance(comp, dict) and "component_name" in comp:
                                recommended_components.append(comp["component_name"])
                    elif isinstance(implementation["connected_components"], str):
                        # Sometimes connected_components is a string description
                        pin_results["recommendations"].append({
                            "type": "connection_recommendation",
                            "message": implementation["connected_components"]
                        })
                    
                    if recommended_components:
                        pin_results["recommendations"].append({
                            "type": "recommended_components",
                            "components": recommended_components
                        })
                
                # Add connectivity recommendations
                if "connectivity" in implementation and implementation["connectivity"]:
                    pin_results["recommendations"].append({
                        "type": "connectivity",
                        "message": implementation["connectivity"]
                    })
                
                # Add precautions
                if "precautions" in implementation:
                    precautions = implementation["precautions"]
                    if isinstance(precautions, list):
                        for precaution in precautions:
                            pin_results["recommendations"].append({
                                "type": "precaution",
                                "message": precaution
                            })
                    elif isinstance(precautions, str):
                        pin_results["recommendations"].append({
                            "type": "precaution",
                            "message": precautions
                        })
            
            results[pin_name] = pin_results
        
        return results
    
    def validate_all_components(self) -> Dict:
        """
        Validate connections for all components in the project.
        
        Returns:
            A dictionary with validation results for each component
        """
        results = {}
        
        for designator, component in self.project.components.items():
            self.logger.info(f"Validating component {designator}")
            
            # Find datasheet for component
            datasheet = self.find_component_datasheet(component)
            
            if datasheet:
                # Validate component connections
                component_results = self.validate_component_connections(component, datasheet)
                
                # Add to results
                results[designator] = {
                    "designator": designator,
                    "has_datasheet": True,
                    "pins": component_results
                }
            else:
                # No datasheet found
                results[designator] = {
                    "designator": designator,
                    "has_datasheet": False,
                    "pins": {}
                }
        
        self.validation_results = results
        return results
    
    def generate_report(self) -> str:
        """
        Generate a human-readable report of the validation results.
        
        Returns:
            A string containing the validation report
        """
        if not self.validation_results:
            self.validate_all_components()
        
        report = []
        report.append("# Connection Validation Report")
        report.append("")
        
        # Count components with and without datasheets
        total_components = len(self.validation_results)
        components_with_datasheet = sum(1 for r in self.validation_results.values() if r["has_datasheet"])
        report.append(f"Total components: {total_components}")
        report.append(f"Components with datasheets: {components_with_datasheet}")
        report.append(f"Components without datasheets: {total_components - components_with_datasheet}")
        report.append("")
        
        # Count issues
        total_issues = 0
        for component_result in self.validation_results.values():
            if component_result["has_datasheet"]:
                for pin_result in component_result["pins"].values():
                    total_issues += len(pin_result["issues"])
        
        report.append(f"Total issues found: {total_issues}")
        report.append("")
        
        # Report issues by component
        report.append("## Issues by Component")
        report.append("")
        
        for designator, component_result in self.validation_results.items():
            if not component_result["has_datasheet"]:
                continue
            
            component_issues = []
            for pin_name, pin_result in component_result["pins"].items():
                for issue in pin_result["issues"]:
                    component_issues.append(f"- Pin {pin_name}: {issue['message']}")
            
            if component_issues:
                report.append(f"### {designator}")
                report.append("")
                report.extend(component_issues)
                report.append("")
        
        # Report recommendations by component
        report.append("## Recommendations by Component")
        report.append("")
        
        for designator, component_result in self.validation_results.items():
            if not component_result["has_datasheet"]:
                continue
            
            component_recommendations = []
            for pin_name, pin_result in component_result["pins"].items():
                for recommendation in pin_result["recommendations"]:
                    if recommendation["type"] == "recommended_components":
                        component_recommendations.append(f"- Pin {pin_name}: Should be connected to {', '.join(recommendation['components'])}")
                    else:
                        component_recommendations.append(f"- Pin {pin_name}: {recommendation['message']}")
            
            if component_recommendations:
                report.append(f"### {designator}")
                report.append("")
                report.extend(component_recommendations)
                report.append("")
        
        return "\n".join(report)
    
    def save_report(self, output_path: str) -> None:
        """
        Save the validation report to a file.
        
        Args:
            output_path: The path to save the report to
        """
        report = self.generate_report()
        
        with open(output_path, "w") as f:
            f.write(report)
        
        self.logger.info(f"Report saved to {output_path}")


if __name__ == "__main__":
    # Example usage
    project_guid = "your_project_guid_here"
    validator = ConnectionValidator(project_guid)
    results = validator.validate_all_components()
    report = validator.generate_report()
    print(report)