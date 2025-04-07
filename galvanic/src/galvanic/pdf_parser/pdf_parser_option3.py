import json
import os
from openai import OpenAI
from google import genai
import pymupdf4llm
import pathlib

from embedded_design_tools.protobuf import PROTOBUF


GEMINI_KEY = "AIzaSyAj8BET-U5yrjnfODhO7v6GDkB_LS3zK0U"

filename = "tps92520-q1.pdf"

### Generate a markdwon version of this datasheet
# print(f"Generating markdown from {filename}")
# md_text = pymupdf4llm.to_markdown(filename)
# pathlib.Path(filename.replace('.pdf', '.md')).write_bytes(md_text.encode())
### Or open previously generated
with open(filename.replace('.pdf', '.md'), 'r') as f:
    md_text = f.read()

prompt = """
Use the following datasheet to compile register information for this device's serial communication bus (SPI, I2C, etc) and then format that as a json file.
Register map information is generally given in a section titled "Register Maps" or something similar.

Digital to physical mappings are often in other sections of the datasheets.  Look through the entire datasheet to find these.
These should be similar in form to a look up table, where each digital value corresponds to a unique physical value, or sometimes are in the form of an equation.
If they are in the form of an equation, make sure to still include this equation as a string.
All physical values should be given units, if provided.

The json file should have two main sections, fields and registers.

It's possible that a field can span two different registers.  This is often indicated in a datasheet by having a field name which includes the 'field_start_bit' and 'field_end_bit' appended to the end, usually in braces.  e.g. SOME_FIELD[7:9].
In this instance, '7' and '9' are the field start and end bits and they should not be included in the field name, but should be used to indicate that the field spans multiple registers.
This is done by including multiple FieldLocation messages in the relevant Field message.  In the case of a Field spanning multiple registers, each FieldLocation message should include values for the optional field_start_bit and field_end_bit entries.

The schema and datatypes for each type of data is defined in the protobuf file.  Use this to determine the json schema.
When compiling the JSON file, observe the following rules:
- Do not place field objects within the register objects.  Register objects should only contain the information that's defined in the Register protobuf message.  It is possible for some fields to span multiple registers.
- All field information should exist with the "field" key in the JSON file.
- Do not make up new keys which are not present in the protobuf file that defines the schema.  Try to map everything to existing keys.

Return the raw json and do not format as a markdown code block
"""

protobuf = PROTOBUF.serial_bus.register


print(f"Analyzing {filename} to {prompt}")
def gemini():
    client = genai.Client(api_key=GEMINI_KEY)
    response = client.models.generate_content(
        # model='gemini-1.5-flash', # Misses a lot of info
        # model='gemini-2.0-flash-001', # Gets more info but limits response length due to output token restrictions
        model='gemini-2.5-pro-exp-03-25',
        # model='gemini-2.0-flash',
        contents=list({
            "prompt": prompt,
            "datasheet": md_text,
            "protobuf": protobuf
        }.values()),
        config={
            'response_mime_type': 'application/json',
        },
    )
    registers = json.loads(response.text.strip(" shame\n```json").strip("```"))
    return registers

def open_ai():
    client = OpenAI(api_key='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')

    response = client.responses.create(
        model="gpt-4o",
        input=[
            {"role": "system", "content": prompt},
            {"role": "user", "content": md_text},
            # {"role": "user", "content": protobuf},
        ]
    )
    registers = json.loads(response.output_text)
    return registers

registers = gemini()
# registers = open_ai()

with open(filename.replace('.pdf', '.json'), 'w') as f:
    f.write(json.dumps(registers, sort_keys=True, separators=(',', ':'), indent=2))
print()

# TODO next steps.  Split up into multiple queries to get around token limits
