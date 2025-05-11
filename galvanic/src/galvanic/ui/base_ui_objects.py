from PyQt6.QtWidgets import QWidget


class GWidget(QWidget):
    def __init__(self, form):
        super().__init__()
        self.ui = form()
        self.ui.setupUi(self)
