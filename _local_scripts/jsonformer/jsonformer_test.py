from jsonformer import Jsonformer
from transformers import AutoModelForCausalLM, AutoTokenizer

model_dir = "../../src/galvanic_ai/_models/dolly-v2-3b"
model = AutoModelForCausalLM.from_pretrained(model_dir)  # , use_cache=True, device_map="auto")
tokenizer = AutoTokenizer.from_pretrained(model_dir)  # , use_fast=True, use_cache=True)

# json_schema = {
#     "type": "object",
#     "properties": {
#         "name": {"type": "string"},
#         "age": {"type": "number"},
#         "is_student": {"type": "boolean"},
#         "courses": {"type": "array", "items": {"type": "string"}},
#     },
# }

json_schema = {"type": "object", "properties": {"name": {"type": "string"}, "pin_name": {"type": "string"}}}

with open("datasheet.md", "r") as f:
    datasheet = f.read()

prompt = f"""
Generate a list of all pins in the device given by the datasheet, using the following schema for each pin

***DATASHEET START***
{datasheet}
***DATASHEET END***
"""
print("tokenizing prompt...")
jsonformer = Jsonformer(model, tokenizer, json_schema, prompt)
print("generating data...")
generated_data = jsonformer()

print(generated_data)
