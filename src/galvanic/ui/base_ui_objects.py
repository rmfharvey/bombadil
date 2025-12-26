import abc
from PySide6.QtWidgets import QWidget


# TODO figure out how to use ABCMeta with another inherited class.  I believe tou need to define a newversion o QWidget with some new attributes
class GWidget(QWidget):  # , metaclass=abc.ABCMeta):
    def __init__(self, form, linked_obj=None):
        super().__init__()
        self._obj = linked_obj

        self.ui = form()
        self.ui.setupUi(self)

        self._setup()
        self._connect_signals()

    def _check_common_elements(self):
        has_comment_pushbutton = hasattr(self.ui, "comment_pushbutton")

    ####################################################################################################################
    ### Abstract Methods
    ####################################################################################################################
    # @abc.abstractmethod
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
