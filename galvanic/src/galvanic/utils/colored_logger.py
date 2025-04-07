import logging
import colorama
from colorama import Fore, Style

# Initialize colorama (required for Windows)
colorama.init(autoreset=True)


class ColoredFormatter(logging.Formatter):
    """Custom formatter that adds colors based on log level with fixed width"""

    # Define color schemes for different logging levels
    COLORS = {
        'DEBUG': Fore.CYAN,
        'INFO': Fore.GREEN,
        'WARNING': Fore.YELLOW,
        'ERROR': Fore.RED,
        'CRITICAL': Fore.RED + Style.BRIGHT
    }

    # Maximum width for level name field
    LEVEL_NAME_WIDTH = 10

    def __init__(self, fmt=None, datefmt=None):
        super().__init__(fmt, datefmt)

    def format(self, record):
        # Save the original levelname
        levelname = record.levelname

        # Apply color and padding
        if levelname in self.COLORS:
            # Pad the level name to fixed width
            padded_levelname = levelname.ljust(self.LEVEL_NAME_WIDTH)

            # Add color to the padded level name
            colored_levelname = f"{self.COLORS[levelname]}{padded_levelname}{Style.RESET_ALL}"

            # Replace the levelname with the colored and padded version
            record.levelname = colored_levelname

        # Call the original formatter
        result = logging.Formatter.format(self, record)

        # Restore the original levelname
        record.levelname = levelname
        return result


def setup_colored_logger(name=None, level=logging.INFO):
    """Set up and return a logger with colored output and fixed width level names"""
    # Create logger
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Create console handler and set level
    console_handler = logging.StreamHandler()
    console_handler.setLevel(level)

    # Create formatter
    formatter = ColoredFormatter(
        fmt='%(asctime)s | %(levelname)s | %(name)s | %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )

    # Add formatter to handler
    console_handler.setFormatter(formatter)

    # Add handler to logger (if not already added)
    if not logger.handlers:
        logger.addHandler(console_handler)

    return logger
