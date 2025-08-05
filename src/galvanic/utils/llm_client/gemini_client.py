import os
from datetime import datetime
from google import genai
from google.genai import (types)

from galvanic.utils.llm_client import LlmClient

class GeminiClient:
    _MODEL = "gemini-2.5-flash-lite"

    def __init__(self, key=None, model=None):
        self.api_key = key
        if self.api_key is None:
            self.api_key = os.environ["GEMINI_KEY"]
        self._client = genai.Client(api_key=self.api_key)

        if model is not None:
            self._MODEL = model

    def generate(self, prompt: str, *args, **kwargs) -> str:
        response = self._client.models.generate_content(
            model=self._MODEL,
            contents=prompt,
            # config=types.GenerateContentConfig(cached_content=self._cache.name),
            # config = {"response_mime_type": "application/json"},
        )
        return response