import abc
from galvanic import global_logger

class CLIENTS:
    GEMINI = "Gemini"
    OPENAI = "OpenAI"

class LlmClient(metaclass=abc.ABCMeta):
    _MODEL: str

    def __init__(self):
        self.logger = global_logger
        print()

    @abc.abstractmethod
    def generate(self, prompt: str, *args, **kwargs) -> str:
        """Basic generate prompt.  Exact method will be handled in inherited classes"""
