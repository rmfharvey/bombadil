# ConnectionValidator

The `ConnectionValidator` class analyzes an Altium project to check if connections match the recommendations and precautions in component datasheets.

## Overview

The `ConnectionValidator` class provides functionality to:

1. Load an Altium project from a GUID, a JSON file, or a dictionary
2. Find datasheets for components using the DatasheetManager
3. Validate component connections against datasheet recommendations
4. Generate a validation report

## Usage

### Basic Usage

```python
from galvanic_design.connection_validator import ConnectionValidator

# Initialize with a project GUID
validator = ConnectionValidator("DA220208-0D1D-4C1A-A0FF-E0D169E92F96")

# Validate all components
results = validator.validate_all_components()

# Generate and print a report
report = validator.generate_report()
print(report)

# Save the report to a file
validator.save_report("connection_validation_report.md")
```

### Using a Local JSON File

```python
from pathlib import Path
from galvanic_design.connection_validator import ConnectionValidator

# Path to a JSON file containing project data
json_file = Path("path/to/project.json")

# Initialize with a JSON file
validator = ConnectionValidator(json_file)

# Validate all components
results = validator.validate_all_components()

# Generate and print a report
report = validator.generate_report()
print(report)
```

### Using a Dictionary

```python
from galvanic_design.connection_validator import ConnectionValidator

# Dictionary containing project data
project_data = {
    "components": {...},
    "nets": {...}
}

# Initialize with a dictionary
validator = ConnectionValidator(project_data)

# Validate all components
results = validator.validate_all_components()
```

## Class Methods

### `__init__(project_source)`

Initialize the ConnectionValidator with an Altium project.

**Parameters:**
- `project_source`: Either a GUID string for the Altium project, a path to a JSON file, or a dictionary containing project data

### `find_component_datasheet(component)`

Find the datasheet for a component using the DatasheetManager.

**Parameters:**
- `component`: The component to find a datasheet for

**Returns:**
- The datasheet JSON if found, None otherwise

### `validate_component_connections(component, datasheet)`

Validate the connections of a component against its datasheet.

**Parameters:**
- `component`: The component to validate
- `datasheet`: The datasheet JSON for the component

**Returns:**
- A dictionary with validation results for each pin

### `validate_all_components()`

Validate connections for all components in the project.

**Returns:**
- A dictionary with validation results for each component

### `generate_report()`

Generate a human-readable report of the validation results.

**Returns:**
- A string containing the validation report

### `save_report(output_path)`

Save the validation report to a file.

**Parameters:**
- `output_path`: The path to save the report to

## Validation Results

The validation results are stored in a dictionary with the following structure:

```python
{
    "component_designator": {
        "designator": "component_designator",
        "has_datasheet": True/False,
        "pins": {
            "pin_name": {
                "pin_name": "pin_name",
                "pin_number": "pin_number",
                "issues": [
                    {
                        "type": "issue_type",
                        "message": "issue_message"
                    }
                ],
                "recommendations": [
                    {
                        "type": "recommendation_type",
                        "message": "recommendation_message"
                    }
                ],
                "connected_net": "net_name"
            }
        }
    }
}
```

## Limitations

1. **Datasheet Matching**: The current implementation may not find datasheets for all components if the part numbers in the project don't match the datasheet part numbers in the DatasheetManager.

2. **Connection Analysis**: The validation focuses on whether pins are connected, but doesn't analyze the specific components they're connected to or the signal integrity of the connections.

3. **Datasheet Coverage**: The validation is only as good as the datasheet information available. If datasheets don't include detailed implementation recommendations, the validation will be limited.

## Future Improvements

1. **Enhanced Part Number Matching**: Implement more sophisticated part number matching logic to improve datasheet finding.

2. **Manual Datasheet Mapping**: Add a way to manually specify datasheet mappings for components.

3. **Signal Integrity Analysis**: Add analysis of signal integrity based on datasheet recommendations.

4. **Component-to-Component Validation**: Validate connections between specific components based on datasheet recommendations.

## Example Report

```markdown
# Connection Validation Report

Total components: 100
Components with datasheets: 75
Components without datasheets: 25

Total issues found: 15

## Issues by Component

### U1

- Pin VCC: Pin VCC should be connected according to datasheet
- Pin GND: Pin GND should be connected according to datasheet

### U2

- Pin ALERT: Pin ALERT should be connected according to datasheet

## Recommendations by Component

### U1

- Pin VCC: Should be connected to Power Supply, Bypass Capacitor
- Pin GND: Connect the GND pin directly to the system's ground plane or ground connection in the schematic.
- Pin SCL: The SCL pin is an open-drain input and requires an external pull-up resistor to function correctly in an I2C bus system.

### U2

- Pin ALERT: The ALERT pin is open-drain, meaning it requires an external pull-up resistor to function correctly as an output.
```