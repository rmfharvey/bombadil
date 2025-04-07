import os
import fitz  # PyMuPDF
from google import genai
from PyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter

# Replace with your PDF file path
_root = os.path.dirname(__file__)
pdf_path = os.path.join(_root, "../../_test_scripts/datasheet_converter/tps92520-q1.pdf")

GEMINI_KEY = "AIzaSyAj8BET-U5yrjnfODhO7v6GDkB_LS3zK0U"

def extract_text_and_query(pdf_path, llm_model, query):
    """Extracts text from a PDF and queries it with an LLM."""

    # Extract text from PDF
    doc = fitz.open(pdf_path)
    text = ""
    for page in doc.pages():
        text += page.get_text()

    # Query the text with an LLM
    # prompt = f"Answer the following question based on the text:\n{text}\n\nQuestion: {query}"
    response = client.models.generate_content(
        model='gemini-2.0-flash-001', contents=[query, text]
    )

    return response


if __name__ == "__main__":
    # Example Usage:
    client = genai.Client(api_key=GEMINI_KEY)

#     query = """
# Compile register information for this device's serial communication bus (SPI, I2C, etc) and then format that as a json file.
# Register map information is generally given in a section titled "Register Maps" or something similar.
#
# Digital to physical mappings are often in other sections of the datasheets.  Look through the entire datasheet to find these.
# These should be similar in form to a look up table, where each digital value corresponds to a unique physical value, or sometimes are in the form of an equation.
# If they are in the form of an equation, convert that equation to a string.
# All physical values should be given units, if provided
#
# The json file should have two main sections, fields and registers.
#
# **It's possible that a field can span two different registers.  This is often indicated in a datasheet by having a field name which includes the 'field_start_bit' and 'field_end_bit' appended to the end, usually in braces.  e.g. SOME_FIELD[7:9].**
# **In this instance, '7' and '9' are the field start and end bits and they should not be included in the field name, but should be used to indicate that the field spans multiple registers.**
# **This is done by including multiple FieldLocation messages in the relevant Field message.  In the case of a Field spanning multiple registers, each FieldLocation message should include values for the optional field_start_bit and field_end_bit entries.**
#
# The schema and datatypes for each type of data is defined in the serial_bus_proto file.  Use this to determine the json schema.
# When compiling the JSON file, observe the following rules:
# - Do not place field objects within the register objects.  Register objects should only contain the information that's defined in the Register protobuf message.  It is possible for some fields to span multiple registers.
# - All field information should exist with the "field" key in the JSON file.
# - Do not make up new keys which are not present in the protobuf file that defines the schema.  Try to map everything to existing keys.
#
# "PROTOBUF FILE:
# syntax = "proto3";
#
# package embedded_design_tools;
#
# enum PhysicalValueMappingType {     // How does the field value get converted to a physically significant value
#     KEY_VALUE_PAIRS = 0;    // Uses KeyValueMap message
#     EQUATION = 1;           // Uses a function, not described here.  TODO Not sure how to implement this, but likely can't as proto
# }
#
# message FieldLocation {
#     uint32 register_address = 1;    // Which register address does this chunk belong to?
#     uint32 reg_start_bit = 2; // Start bit in register if the field bit descriptor is "3:7", this would be 3
#     uint32 reg_end_bit = 3;   // End bit in register
#
#     optional uint32 field_start_bit = 4; // If the field spans multiple registers, or non-continuous bits, these should be
#     optional uint32 field_end_bit = 5;   //   used to indicate which bits in the field are described by this FieldLocation message
# }
#
# message Register {
#     uint32 address = 1;
#     uint32 init_value = 2;
# //    repeated Field fields = 3;
#     optional bool read_only = 4;    // Defaults to False
#     optional string name = 5;   // Register name
#     optional uint32 bit_width = 6;   // Width of register in bits, default is normally 8
# }
#
# message Field {
#     repeated FieldLocation register_location = 1;
#     optional string name = 2;   // Human readable field name, if provided
#     optional string description = 3;    // Description of what a field does or represents
#     optional bool reserved =  4;    // If the field is reserved and shouldn't be written set to True.  Default is False
#     map<int32, string> digital_physical_map = 5;   // Maps digital field value to a physical value, numerical value strings should include units, i.e. 0b10: "2.3V/us"
# }
# """
    query = """Determine how many physical pins the device in this datasheet has"""
    result = extract_text_and_query(pdf_path, client, query)
    print(result.text)

