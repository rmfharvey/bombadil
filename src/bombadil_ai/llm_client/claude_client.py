import os
from datetime import datetime

import anthropic

from bombadil_ai.llm_client.llm_client import LlmClient, log_token_usage


class ClaudeUsageMetadata:
    """Adapter to convert Claude's usage format to match the expected TokenLogger format."""

    def __init__(self, usage):
        self.prompt_token_count = usage.input_tokens
        self.thoughts_token_count = usage.output_tokens
        self.cached_content_token_count = getattr(usage, "cache_read_input_tokens", 0) or 0
        self.total_token_count = self.prompt_token_count + self.thoughts_token_count


class ClaudeResponse:
    """Wrapper for Claude response to provide compatible interface."""

    def __init__(self, response):
        self._response = response
        self.usage_metadata = ClaudeUsageMetadata(response.usage)

    @property
    def text(self):
        """Returns the text content from the response."""
        for block in self._response.content:
            if block.type == "text":
                return block.text
        return ""


class ClaudeClient(LlmClient):
    _MODEL = "claude-sonnet-4-20250514"

    def __init__(self, key=None, model=None):
        super().__init__()
        self.api_key = key
        if self.api_key is None:
            self.api_key = os.environ["ANTHROPIC_API_KEY"]
        self._client = anthropic.Anthropic(api_key=self.api_key)

        if model is not None:
            self._MODEL = model

    @log_token_usage
    def generate(self, prompt, system_prompt=None, max_tokens=4096, *args, **kwargs):
        """Generate a response from Claude.

        :param str prompt: The user prompt to send to Claude
        :param str system_prompt: Optional system prompt for context
        :param int max_tokens: Maximum tokens in the response (default 4096)
        :return: ClaudeResponse wrapper containing the API response
        """
        messages = [{"role": "user", "content": prompt}]

        request_kwargs = {
            "model": self._MODEL,
            "max_tokens": max_tokens,
            "messages": messages,
            **kwargs,
        }

        if system_prompt is not None:
            request_kwargs["system"] = system_prompt

        response = self._client.messages.create(**request_kwargs)
        return ClaudeResponse(response)

    def log_transaction_tokens(self, usage_meta, timestamp=None):
        """Logs tokens required for a query.

        :param ClaudeUsageMetadata usage_meta: Usage metadata
        """
        if timestamp is None:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        token_info = self._token_logger.add_transaction(usage_meta, timestamp)
        self.logger.info(
            "Total Token Count: {t[total_tokens]}\n\tInput: {t[prompt_tokens]}\n\tOutput: {t[output_tokens]}\n\tCached: {t[cached_tokens]}".format(
                t=token_info
            )
        )
