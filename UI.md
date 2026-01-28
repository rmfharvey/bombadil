# UI Framework

PySide6-based UI framework using a custom GWidget base class pattern.

## GWidget Base Class

**Location:** `bombadil/ui/base_ui_objects.py`

All custom widgets inherit from GWidget:

```python
from bombadil.ui.base_ui_objects import GWidget
from mypackage.forms.my_form_ui import Ui_Form as MyForm

class MyWidget(GWidget):
    def __init__(self, data_object=None):
        super().__init__(MyForm, linked_obj=data_object)

    def _setup(self):
        """Configure UI elements - REQUIRED"""
        self.ui.name_label.setText("Example")

    def _connect_signals(self):
        """Connect signal handlers - REQUIRED"""
        self.ui.submit_pushbutton.clicked.connect(self._handler_submit_clicked)

    def _handler_submit_clicked(self):
        """Handle button click"""
        pass
```

**Key Features:**
- `self.ui`: Access to form elements
- `self._obj` / `self.obj`: Linked data object
- Automatic `setupUi()` call from form class
- Comment button support via `_check_common_elements()`

## Widget Naming Convention

Widget names end with the widget type as a single lowercase word, without the Q prefix:

| Qt Class | Suffix | Example |
|----------|--------|---------|
| QPushButton | pushbutton | `browse_pushbutton` |
| QLineEdit | lineedit | `part_number_lineedit` |
| QLabel | label | `status_label` |
| QComboBox | combobox | `value_combobox` |
| QCheckBox | checkbox | `autocreate_json_checkbox` |
| QFrame | frame | `drop_frame` |
| QGroupBox | groupbox | `register_groupbox` |

## Directory Structure

```
bombadil/ui/
├── base_ui_objects.py           # GWidget base class
├── batch_uic.py                 # Compile .ui → _ui.py
├── register_map/
│   ├── register_map_ui.py       # Widget implementations
│   └── forms/
│       ├── field.ui             # Qt Designer file
│       └── field_ui.py          # Generated Python
└── utils/
    ├── datasheet_adder_widget.py
    └── forms/
        ├── datasheet_adder.ui
        └── datasheet_adder_ui.py
```

## Creating New Widgets

1. **Create .ui file** in `forms/` directory using Qt Designer
2. **Generate Python** with pyside6-uic:
   ```bash
   pyside6-uic -o forms/my_widget_ui.py forms/my_widget.ui
   ```
3. **Create widget class** inheriting from GWidget
4. **Implement** `_setup()` and `_connect_signals()`

## Form Compilation

**Location:** `bombadil/ui/batch_uic.py`

Batch compile all .ui files:
```bash
python -m bombadil.ui.batch_uic
```

Uses `build_list.json` to define which files and directories to compile.

```python
def main():
    from bombadil import MainApp

    widget = MyWidget()
    widget.show()
    MainApp.exec()

if __name__ == "__main__":
    main()
```