from pathlib import Path
from urllib.parse import urlparse

from PySide6.QtCore import Signal
from PySide6.QtWidgets import QFileDialog, QMainWindow

from bombadil.ui.base_ui_objects import GWidget
from bombadil.ui.utils.forms.datasheet_adder_ui import Ui_Form as DatasheetAdderForm
from bombadil_datasheets import DatasheetManager


class DatasheetAdderWidget(GWidget):
    """Widget for adding electronics component datasheets.

    Allows users to add datasheets via drag-and-drop or file browser,
    specify a part number, and create markdown/JSON versions using DatasheetManager.
    """

    datasheet_created = Signal(str)  # Emits part number on successful creation

    VALID_EXTENSIONS = {".pdf", ".md"}

    def __init__(self):
        super().__init__(DatasheetAdderForm)

    def _setup(self):
        """Setup UI elements and enable drag-drop functionality."""
        self.setAcceptDrops(True)
        self._selected_file_path = None
        self._update_create_pushbutton_state()

    def _connect_signals(self):
        """Connect all signals to handler functions."""
        self.ui.browse_pushbutton.clicked.connect(self._handler_browse_clicked)
        self.ui.create_pushbutton.clicked.connect(self._handler_create_clicked)
        self.ui.cancel_pushbutton.clicked.connect(self._handler_cancel_clicked)
        self.ui.part_number_lineedit.textChanged.connect(self._handler_part_number_changed)
        self.ui.url_lineedit.textChanged.connect(self._handler_url_changed)

    def _update_create_pushbutton_state(self):
        """Enable create button only when (file or URL) and part number are provided."""
        has_file = self._selected_file_path is not None
        has_url = self._is_valid_url(self.ui.url_lineedit.text().strip())
        has_part_number = bool(self.ui.part_number_lineedit.text().strip())
        self.ui.create_pushbutton.setEnabled((has_file or has_url) and has_part_number)

    def _is_valid_url(self, text):
        """Check if text is a valid URL."""
        if not text:
            return False
        parsed = urlparse(text)
        return parsed.scheme in ("http", "https") and bool(parsed.netloc)

    def _set_selected_file(self, file_path):
        """Set the selected file and update the UI."""
        path = Path(file_path)
        if path.suffix.lower() not in self.VALID_EXTENSIONS:
            self.ui.status_label.setText("Invalid file type. Please select a PDF or MD file.")
            self.ui.status_label.setStyleSheet("color: red;")
            return False

        self._selected_file_path = str(path)
        self.ui.selected_file_label.setText(f"Selected: {path.name}")
        self.ui.url_lineedit.clear()  # Clear URL when file is selected
        self.ui.status_label.setText("")
        self.ui.status_label.setStyleSheet("")

        # Auto-fill part number from filename if empty
        if not self.ui.part_number_lineedit.text().strip():
            suggested_name = path.stem.lower().replace(" ", "_").replace("-", "_")
            self.ui.part_number_lineedit.setText(suggested_name)

        self._update_create_pushbutton_state()
        return True

    def _handler_browse_clicked(self):
        """Open file dialog to select a datasheet file."""
        file_path, _ = QFileDialog.getOpenFileName(
            self,
            "Select Datasheet",
            "",
            "Datasheet Files (*.pdf *.md);;PDF Files (*.pdf);;Markdown Files (*.md);;All Files (*)",
        )
        if file_path:
            self._set_selected_file(file_path)

    def _handler_create_clicked(self):
        """Create the datasheet using DatasheetManager."""
        part_number = self.ui.part_number_lineedit.text().strip().lower()
        autocreate_json = self.ui.autocreate_json_checkbox.isChecked()
        url = self.ui.url_lineedit.text().strip()

        # Use file path if available, otherwise use URL
        datasheet_source = self._selected_file_path or url

        if not part_number or not datasheet_source:
            self.ui.status_label.setText("Please provide a file/URL and part number.")
            self.ui.status_label.setStyleSheet("color: red;")
            return

        self.ui.status_label.setText("Creating datasheet...")
        self.ui.status_label.setStyleSheet("color: blue;")
        self.ui.create_pushbutton.setEnabled(False)

        try:
            DatasheetManager.new_datasheet(
                part_number=part_number, datasheet_path=datasheet_source, autocreate_json=autocreate_json
            )
            self.ui.status_label.setText(f"Datasheet '{part_number}' created successfully!")
            self.ui.status_label.setStyleSheet("color: green;")
            self.datasheet_created.emit(part_number)
            self._reset_form()
        except Exception as e:
            self.ui.status_label.setText(f"Error: {str(e)}")
            self.ui.status_label.setStyleSheet("color: red;")
            self._update_create_pushbutton_state()

    def _handler_cancel_clicked(self):
        """Reset the form to initial state."""
        self._reset_form()

    def _handler_part_number_changed(self, _text):
        """Handle part number text changes."""
        self._update_create_pushbutton_state()

    def _handler_url_changed(self, text):
        """Handle URL text changes."""
        if self._is_valid_url(text):
            self._selected_file_path = None
            self.ui.selected_file_label.setText("No file selected")
        self._update_create_pushbutton_state()

    def _reset_form(self):
        """Reset the form to its initial state."""
        self._selected_file_path = None
        self.ui.selected_file_label.setText("No file selected")
        self.ui.url_lineedit.clear()
        self.ui.part_number_lineedit.clear()
        self.ui.autocreate_json_checkbox.setChecked(True)
        self.ui.status_label.setText("")
        self.ui.status_label.setStyleSheet("")
        self._update_create_pushbutton_state()

    def dragEnterEvent(self, event):
        """Handle drag enter events for file drops."""
        if event.mimeData().hasUrls():
            urls = event.mimeData().urls()
            if urls and urls[0].isLocalFile():
                file_path = urls[0].toLocalFile()
                if Path(file_path).suffix.lower() in self.VALID_EXTENSIONS:
                    event.acceptProposedAction()
                    self.ui.drop_frame.setStyleSheet("QFrame { background-color: #e0f0e0; }")
                    return
        event.ignore()

    def dragLeaveEvent(self, event):
        """Handle drag leave events."""
        self.ui.drop_frame.setStyleSheet("")
        event.accept()

    def dropEvent(self, event):
        """Handle file drop events."""
        self.ui.drop_frame.setStyleSheet("")
        if event.mimeData().hasUrls():
            urls = event.mimeData().urls()
            if urls and urls[0].isLocalFile():
                file_path = urls[0].toLocalFile()
                if self._set_selected_file(file_path):
                    event.acceptProposedAction()
                    return
        event.ignore()


def main():
    from bombadil import MainApp

    window = QMainWindow()
    window.setWindowTitle("Datasheet Parser")
    window.setCentralWidget(DatasheetAdderWidget())
    window.show()
    MainApp.exec()


if __name__ == "__main__":
    main()
