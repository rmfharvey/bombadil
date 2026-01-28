# Datasheet System

The datasheet system manages electronics component datasheets through three layers: storage, conversion, and access.

## Architecture

```
DatasheetManager (Access) → DatasheetStructure (Storage) → DatasheetConverter (Conversion)
```

## DatasheetManager

**Location:** `bombadil_datasheets/datasheet_manager.py`

Global singleton for accessing all datasheets:

```python
from bombadil_datasheets import DatasheetManager

# Get existing datasheet
ds = DatasheetManager.get_datasheet("stm32f103")

# Create new datasheet
ds = DatasheetManager.new_datasheet(
    part_number="lm5050",
    datasheet_path="/path/to/datasheet.pdf",
    autocreate_json=True
)

# Browse by organization
DatasheetManager.by_manufacturer  # Grouped by manufacturer
DatasheetManager.by_type          # Grouped by device type
```

## DatasheetStructure

Manages a single datasheet's file organization:

```
source_datasheets/{part_number}/
├── datasheet.pdf    # Original PDF
├── datasheet.md     # Markdown conversion
└── datasheet.json   # Parsed structured data
```

**Properties:**
- `has_pdf`, `has_md`, `has_json`: Check file existence
- `pdf_path`, `md_path`, `json_path`: Get file paths

**Methods:**
- `download_datasheet(path)`: Copy from local path or download from URL
- `create_json()`: Convert to JSON using DatasheetConverter
- `load_json_datasheet()`: Load parsed JSON

## DatasheetConverter

**Location:** `bombadil/utils/datasheet_parser/datasheet_converter.py`

AI-powered converter using Gemini API:

```python
from bombadil.utils.datasheet_parser import DatasheetConverter

converter = DatasheetConverter(
    source_path="datasheet.pdf",  # or .md
    output_directory="/path/to/output"
)
converter.save_config("/path/to/datasheet.json")
```

**Extraction Pipeline:**
1. PDF → Markdown (via pymupdf4llm)
2. Markdown → Structured JSON (via Gemini AI)

**Extracted Data:**
- High-level info (manufacturer, device type, serial buses)
- Pin information (names, numbers, types)
- Serial bus registers (I2C, SPI, UART configurations)
- Pin connectivity details

## JSON Schema

```json
{
  "high_level": {
    "manufacturer": "Texas Instruments",
    "device_type": "Hot Swap Controller",
    "serial_busses": ["I2C"]
  },
  "pins": {
    "VCC": {
      "pin_name": "VCC",
      "pin_number": "1",
      "implementation": {}
    }
  },
  "serial_bus": {
    "registers": {}
  }
}
```

## Storage Location

All datasheets stored in: `bombadil_datasheets/source_datasheets/`

Each part number gets its own directory with consistent file naming.
