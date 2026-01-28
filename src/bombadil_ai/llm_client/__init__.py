from bombadil_ai.llm_client.gemini_client import GeminiClient
from bombadil_ai.llm_client.claude_client import ClaudeClient
from bombadil import global_logger


class CLIENTS:
    GEMINI = "Gemini"
    CLAUDE = "Claude"


def get_client(client_type):
    client_list = {CLIENTS.GEMINI: GeminiClient, CLIENTS.CLAUDE: ClaudeClient}
    client_class = client_list.get(client_type)

    if client_class is None:
        global_logger.warning(f"Client type {client_type} not found")
        return None
    else:
        return client_class()
