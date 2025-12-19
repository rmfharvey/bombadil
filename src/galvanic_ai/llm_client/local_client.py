from llama_cpp import Llama


# from galvanic_ai.llm_client.llm_client import LlmClient, log_token_usage
#
#
# class LlamaCppClient(LlmClient):
#     def generate(self, prompt: str, *args, **kwargs) -> str:
#         """Basic generate prompt.  Exact method will be handled in inherited classes"""
#
#     def log_transaction_tokens(self, usage_meta, timestamp=None):
#         """Logs tokens required for a query"""
#         return NotImplemented


if __name__ == "__main__":
    llm = Llama(model_path="../_models/qwen3_0.6b/Qwen3-0.6B-BF16.gguf")
    print("")
    print()
