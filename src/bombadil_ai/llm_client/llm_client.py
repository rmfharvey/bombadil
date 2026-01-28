import abc
from datetime import datetime
from bombadil import global_logger


class CLIENTS:
    GEMINI = "Gemini"
    CLAUDE = "Claude"


class LlmClient(metaclass=abc.ABCMeta):
    _MODEL: str

    def __init__(self):
        self.logger = global_logger
        self._token_logger = TokenLogger()
        print()

    @abc.abstractmethod
    def generate(self, prompt: str, *args, **kwargs) -> str:
        """Basic generate prompt.  Exact method will be handled in inherited classes"""

    @abc.abstractmethod
    def log_transaction_tokens(self, usage_meta, timestamp=None):
        """Logs tokens required for a query"""


class TokenLogger:
    def __init__(self):
        self._transactions = []

    def add_transaction(self, usage_meta, timestamp):
        token_info = {
            "timestamp": timestamp,
            "total_tokens": usage_meta.total_token_count,
            "prompt_tokens": usage_meta.prompt_token_count,
            "cached_tokens": usage_meta.cached_content_token_count,
            "output_tokens": usage_meta.thoughts_token_count,
        }
        self._transactions.append(token_info)
        return token_info


def log_token_usage(func):
    def wrapper(*args, **kwargs):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        response = func(*args, **kwargs)

        # Log token usage
        usage_meta = response.usage_metadata
        args[0].log_transaction_tokens(usage_meta)

        return response

    return wrapper
