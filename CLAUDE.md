# Bombadil Project

An integrated electronics design and analysis platform combining datasheet parsing, Altium CAD integration, component management, and AI-powered design assistance.

## Project Structure

```
src/
├── bombadil/                    # Core package
│   ├── ui/                      # PySide6 UI framework (see @ui.md)
│   ├── model/                   # Data models (register maps, fields)
│   ├── signal/                  # Signal definition schema
│   └── utils/                   # Utilities (datasheet parser, digikey API)
├── bombadil_datasheets/         # Datasheet management (see @datasheets.md)
├── bombadil_design/             # Design analysis and validation
├── bombadil_ai/                 # AI client integrations (Claude, Gemini)
├── bombadil_altium/             # Altium CAD integration
├── bombadil_tracking/           # Linear issue tracking
└── bombadil_tools/              # Standalone tool utilities
```

## Key Conventions

### Logging
```python
from bombadil import colored_logger
logger = colored_logger(__file__)
```

### Singleton Pattern
```python
class _MyManager:
    pass
MyManager = _MyManager()  # Global singleton instance
```

### Signal Handlers
Private methods prefixed with `_handler_`:
```python
def _handler_button_clicked(self):
    pass
```

### Config-Driven Models
Models load from dictionaries and auto-create UI objects:
```python
class MyModel:
    def __init__(self, config):
        self.load_config(config)
        self.ui_object = MyWidget(self)
```

## Dependencies

- **pyside6**: Qt UI framework
- **anthropic**: Claude API client
- **google-genai**: Gemini API client
- **pymupdf4llm**: PDF to Markdown conversion

## Supplementary Documentation

- @DATASHEETS.md - Datasheet management system.  Any requests to create a datasheet or reference datasheet data should use this for guidance
- @UI.md - UI framework and widget patterns.  Any work on UI elements should use this for guidance.
