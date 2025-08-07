from functools import wraps
import json
from textwrap import dedent
from galvanic_ai.llm_client import get_client, CLIENTS
from galvanic_altium.project import AltiumProject


def requires_llm_client(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        if args[0]._llm_client is None:
            args[0].logger.warning(f"No LLM CLient initialized for {args[0].name}")
            return False
        return f(*args, **kwargs)

    return wrapper


class Controller:
    def __init__(self, project_guid, name=None):
        self.project = AltiumProject(guid=project_guid)

        self.name = name

        # Set up LLM CLient
        self.add_llm_client("Gemini")

    # TODO add llm client and semantic querying

    def add_llm_client(self, client_type):
        self._llm_client = get_client(CLIENTS.GEMINI)

        # Context caching
        if self._llm_client:
            instructions = """
            This content includes part and connectivity information for an electronic PCBA.  
            All connectivity between components is in the 'nets' field.  
            All component and pin functionality info is in the 'components' field.  
            You shall answer any questions based this content."
            """
            self._llm_client.add_cache(
                cache_item_name="project_metadata",
                instructions=dedent(instructions),
                contents=json.dumps(self.project.get_config()),
            )

    @requires_llm_client
    def query(self, prompt):
        response = self._llm_client.generate(prompt, cache_name="project_metadata")
        return response.text

    @requires_llm_client
    def chat(self):
        end_chat = False

        print(
            "Starting chat.  'quit' to end.\n\nController: Hello friendo.  What do you want to know about this project?"
        )
        while not end_chat:
            prompt = input("You: ")
            print(prompt)
            end_chat = prompt.lower().strip() == "quit"
            if not end_chat:
                response = self._llm_client.generate(prompt, cache_name="project_metadata")
                print(f"Controller: {response.text}")
        print("Chat ended.")
