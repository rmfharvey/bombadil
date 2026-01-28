import os
from datetime import datetime

from google import genai
from google.genai import types

from bombadil_ai.llm_client.llm_client import LlmClient, log_token_usage


class GeminiClient(LlmClient):
    # _MODEL = "gemini-2.5-pro-preview-06-05"
    _MODEL = "gemini-2.5-flash-lite"

    def __init__(self, key=None, model=None):
        super().__init__()
        self.api_key = key
        self._cached_items = {}
        if self.api_key is None:
            self.api_key = os.environ["GEMINI_KEY"]
        self._client = genai.Client(api_key=self.api_key)

        if model is not None:
            self._MODEL = model

    def add_cache(self, cache_item_name, contents, instructions=None, persistence=3600):
        if instructions is None:
            instructions = "Answer subsequent queries using this cached content"
        self.logger.info(f"Caching info for {cache_item_name}")
        self._cached_items[cache_item_name] = self._client.caches.create(
            model=self._MODEL,
            config=types.CreateCachedContentConfig(
                display_name=cache_item_name,  # used to identify the cache
                system_instruction=instructions,
                contents=contents,
                ttl=f"{persistence}s",
            ),
        )

    @log_token_usage
    def generate(self, prompt, cache_name=None, *args, **kwargs):
        kw = {
            "model": self._MODEL,
            "contents": prompt,
        }

        if cache_name in self._cached_items:
            kw["config"] = types.GenerateContentConfig(cached_content=self._cached_items[cache_name].name)

        response = self._client.models.generate_content(*args, **{**kwargs, **kw})
        return response

    def log_transaction_tokens(self, usage_meta, timestamp=None):
        """Logs tokens required for a query

        :param GenerateContentResponseUsageMetadata usage_meta:  Usage metadata
        """
        if timestamp is None:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        token_info = self._token_logger.add_transaction(usage_meta, timestamp)
        self.logger.info(
            "Total Token Count: {t[total_tokens]}\n\tInput: {t[prompt_tokens]}\n\tOutput: {t[output_tokens]}\n\tCached: {t[cached_tokens]}".format(
                t=token_info
            )
        )
