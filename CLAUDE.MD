# Galvanic - Electronics Design and Project Management Tool

## Project Overview

Galvanic is a comprehensive electronics design and project management platform for microcontroller/FPGA projects. It integrates Altium Designer projects with AI-powered analysis, datasheet management, and project tracking capabilities.

**Author**: Ross Harvey
**Python Version**: 3.13+
**Main Framework**: PySide6 (Qt for Python)

## Core Purpose

This tool streamlines the hardware engineering workflow by:
- Integrating with Altium Designer for schematic and BOM management
- Using AI (Google Gemini) to analyze datasheets and assist with design decisions
- Providing visual UI for microcontroller pad configuration and register mapping
- Tracking project tasks through Linear.app integration
- Managing component datasheets and vendor information

## Project Structure

```
galvanic/
├── src/
│   ├── galvanic/                    # Main desktop application (PySide6 UI)
│   ├── galvanic_altium/             # Altium Designer integration
│   ├── galvanic_design/             # Design controller and workflow orchestration
│   ├── galvanic_tracking/           # Linear.app issue tracking integration
│   ├── galvanic_ai/                 # LLM client (Gemini, etc.)
│   ├── galvanic_datasheets/         # Datasheet management and caching
│   └── galvanic_schema/             # Protocol Buffer definitions
├── scripts/                         # Utility scripts for various tasks
├── tests/                           # Test suite
└── _local_scripts/                  # Development scripts
```

## Key Modules

### galvanic (Main Package)
**Location**: `src/galvanic/`

The core desktop application with PySide6-based UI components:

- **UI Components** (`ui/`):
  - `register_map_ui.py`: Visualize and edit microcontroller register definitions
  - `microcontroller_pad_widget.py`: Interactive pin configuration interface
  - `base_ui_objects.py`: Abstract widget classes (GWidget) for consistent UI

- **Utilities** (`utils/`):
  - `colored_logger.py`: Colored logging system
  - `datasheet_parser.py`: PDF/markdown to JSON conversion using Gemini API
  - `passive_naming_schema.py`: Standardized naming for passive components
  - `digikey_api.py`: DigiKey component database integration

- **Signal System** (`signal/`): Defines hardware signal types (Digital, Analog, PWM, UART, I2C, SPI, Power Rails)

### galvanic_altium
**Location**: `src/galvanic_altium/`

Altium Designer integration for parsing projects and schematics:

- `project.py`: Parse Altium project files, manage component data
- `schematic.py`: Handle schematic sheets and net definitions
- `server_api.py`: Altium cloud server API (AFS) integration
- Extracts BOM, component AVL (Approved Vendor Lists), nets, and connections

### galvanic_design
**Location**: `src/galvanic_design/`

Design management and controller logic:

- `controller.py`: Main orchestrator that:
  - Loads Altium projects
  - Manages component datasheets
  - Integrates LLM client for AI assistance
  - Compiles passive component part numbers
  - Provides semantic querying of design data

- `microcontroller/pad.py`: Microcontroller pad representation

### galvanic_tracking
**Location**: `src/galvanic_tracking/`

Project task tracking through Linear API:

- `linear_client.py`: Linear API wrapper (LinearHelper class)
  - Create and manage issues
  - Support for priorities, time estimates, labels, assignees
  - Validation phase tracking (Smoke Test, Characterization, Reliability, Field)
  - Task types (Validation, Design, Review Feedback, Miscellaneous)

### galvanic_ai
**Location**: `src/galvanic_ai/`

LLM integration for AI-assisted analysis:

- `llm_client/gemini_client.py`: Google Gemini API client (primary)
- `llm_client/local_client.py`: Local model support
- `llm_client/llm_client.py`: Base client interface
- Modular design supports multiple LLM providers

### galvanic_datasheets
**Location**: `src/galvanic_datasheets/`

Datasheet lifecycle management:

- `datasheet_manager.py`:
  - Downloads datasheets from URLs or local paths
  - Converts PDF datasheets to JSON schemas using AI
  - Caches datasheet data for reuse
- Contains source datasheets for various components (STM32, BQ25756, etc.)

### galvanic_schema
**Location**: `src/galvanic_schema/`

Protocol Buffer definitions for data serialization

## Technologies Used

| Technology | Purpose |
|-----------|---------|
| PySide6 (6.9.1+) | Qt bindings for desktop UI |
| Google Gemini API | LLM for datasheet analysis and design assistance |
| Linear API | Project tracking and issue management |
| PyMuPDF4LLM | PDF document processing |
| Pydantic | Data validation |
| Protocol Buffers | Data serialization |
| Colorama | Colored terminal output |
| DigiKey API | Component information lookup |

## Development Notes

### Recent Changes
- Migrated from Qt to PySide6 for better licensing and maintenance
- Added pad UI elements for microcontroller configuration
- Integrated Linear API for task tracking
- Removed local model support, focusing on cloud-based AI services

### Environment Setup
- Python 3.13+ required
- Uses `uv` for dependency management (see `uv.lock`)
- Configuration in `pyproject.toml`

### Git Workflow
- Main branch: `main`

## Code Patterns and Conventions

### UI Development
- All UI widgets inherit from `GWidget` (base UI object)
- PySide6 Qt framework for GUI components
- Signal types are color-coded in the UI

### Data Management
- Protocol Buffers for serialization where needed
- Pydantic for data validation
- JSON caching for datasheets

### API Integrations
- Altium: Cloud-based project fetching via GUID
- Linear: Issue tracking and task management
- DigiKey: Component information retrieval
- Gemini: AI-powered datasheet parsing and design assistance

### Logging
- Use `colored_logger` utility for consistent, colored logging output

## Common Tasks

### Working with Altium Projects
- Load projects via `galvanic_altium.project`
- Access BOM and component data through the controller
- Parse schematics for net information

### Datasheet Management
- Use `datasheet_manager.py` to download and convert datasheets
- AI-powered PDF to JSON conversion for structured queries
- Cached results prevent redundant API calls

### UI Development
- Extend `GWidget` for new UI components
- Follow existing patterns in `ui/` directory
- Register map and pad widgets are key reference implementations

### AI Integration
- Primary LLM: Google Gemini
- Use `galvanic_ai.llm_client` for AI-powered analysis
- Datasheet parsing is a key use case

## Important File Locations

- Main entry point: `main.py`
- Project config: `pyproject.toml`
- UI components: `src/galvanic/ui/`
- Design controller: `src/galvanic_design/controller.py`
- Altium integration: `src/galvanic_altium/`
- Scripts and utilities: `scripts/`

## Testing

Test suite located in `tests/` directory.

## Notes for AI Assistance

- This is a hardware engineering tool, so understanding electronics terminology is helpful
- Component designators (R1, C5, U3, etc.) are standard references
- Microcontroller pads/pins have specific signal types and configurations
- BOM (Bill of Materials) and AVL (Approved Vendor List) are key concepts
- The project bridges software (Python/Qt) with hardware design (Altium, datasheets)
