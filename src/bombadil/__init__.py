"""Top-level package for bombadil."""

__author__ = """Ross Harvey"""
__email__ = "rmfharvey@gmail.com"
__version__ = "0.1.0"

from bombadil.utils.colored_logger import colored_logger
from bombadil.ui import MainApp

global_logger = colored_logger("global")
