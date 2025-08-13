from functools import wraps
import json
from textwrap import dedent

from galvanic.signal import COLORS
from galvanic import colored_logger
from galvanic.utils.passive_naming_schema.capacitor import compile_capacitor_pn_list
from galvanic_ai.llm_client import get_client, CLIENTS
from galvanic_altium.project import AltiumProject
from galvanic_datasheets import DatasheetManager


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
        self.name = name
        self.logger = colored_logger(self.name if self.name else __name__)  # WIll fix this later when a name gets added
        self.datasheets = {}

        self.project = AltiumProject(guid=project_guid)
        self.datasheets = self.add_datasheets()
        # Set up LLM CLient
        self.add_llm_client(CLIENTS.GEMINI)

    def add_datasheets(self, create_new_if_missing=False):
        _RELEVANT_PREFIXES = ["U"]  # Prefixes to get datasheets for

        datasheets = {}
        for des_type, components in self.project.bom.components_by_type.items():
            if des_type not in _RELEVANT_PREFIXES:
                continue  # If not a relevant type, skip
            for des, cmp in components.items():
                if not cmp.has_avl:  # No AVL
                    self.logger.warning(f"No AVL exists for {cmp}")

                mfg, pn = cmp.avl[0]
                if pn in datasheets:
                    continue  # Don't reload if datasheet is already loaded

                ds = DatasheetManager.get_datasheet(pn, create_new_if_missing)
                if ds is None:
                    continue

                # cmp.datasheet = ds
                datasheets[pn] = ds
        return datasheets

    def get_config(self):
        return {
            "project": self.project.get_config(),
            "datasheets": self.datasheets,
        }

    def add_llm_client(self, client_type):
        self._llm_client = get_client(client_type)

        # Context caching
        if self._llm_client:
            instructions = """
            This content includes component and connectivity information for an electronic PCBA.
            All connectivity between components is in the 'nets' field.
            Basic component and pin functionality info is in the 'components' field.  
            Datasheets are in the 'datasheets' field.  These contain detailed information for each component.
            Datasheets are indexed by Manufacturer Part Number.  Any request for a datasheet will usually use this manufacturer part number/dict key. 
            Component datasheet information includes the following:
                - High level device information
                - Names, types, descriptions, etc of all pins on the device. These can be useful for finding misconnected pins
                - Serial bus register and field information
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
            end_chat = prompt.lower().strip() == "quit"
            if not end_chat:
                response = self._llm_client.generate(prompt, cache_name="project_metadata")
                print(f"Controller: {response.text}")
        print("Chat ended.")
