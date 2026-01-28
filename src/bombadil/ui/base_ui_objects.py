import abc
from PySide6.QtWidgets import QWidget


class QABCMeta(abc.ABCMeta, type(QWidget)):
    """Metaclass that combines ABCMeta with Qt's metaclass for abstract base classes.
    Order matters: ABCMeta first to ensure _abc_impl is properly initialized"""

    pass


class GWidget(QWidget, metaclass=QABCMeta):
    def __init__(self, form, linked_obj=None):
        super().__init__()
        self._comment = None
        self._obj = linked_obj

        self.ui = form()
        self.ui.setupUi(self)

        self._setup()
        self._connect_signals()

    def _check_common_elements(self):
        has_comment_pushbutton = hasattr(self.ui, "comment_pushbutton")
        if has_comment_pushbutton:
            self.ui.comment_pushbutton.clicked.connect(self._handler_comment_button_clicked)

    ####################################################################################################################
    ### Abstract Methods
    ####################################################################################################################
    @abc.abstractmethod
    def _setup(self):
        """Setup UI elements that are specific to the inherited class"""

    @abc.abstractmethod
    def _connect_signals(self):
        """Connect all signals to handler functions that are specific to the inherited class"""

    ####################################################################################################################
    ### Properties
    ####################################################################################################################
    @property
    def obj(self):
        return self._obj

    ####################################################################################################################
    ### Signal Handlers
    ####################################################################################################################
    def _handler_comment_button_clicked(self):
        """Open a comment dialog when the comment button is clicked"""
        # TODO open comment QDialog window with a text frame and "ok" pushbottonropmt . prompt the user to add a comment, then assign to self._comment
