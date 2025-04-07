import json
import logging
import os
from openai import OpenAI
from google import genai
import pymupdf4llm
import pathlib

from embedded_design_tools.protobuf import PROTOBUF


GEMINI_KEY = "AIzaSyAj8BET-U5yrjnfODhO7v6GDkB_LS3zK0U"

filename = "tps92520-q1.pdf"

### Generate a markdwon version of this datasheet
print(f"Generating markdown from {filename}")

class DatasheetReader:
    logger = logging.getLogger()
    @staticmethod
    def to_markdown(datasheet_path, output_path=None):
        """Convert to

        :param datasheet_path:
        :param output_path:
        :return:
        """
        DatasheetReader.logger.info(f"Converting {datasheet_path} to markdown")
        md_text = pymupdf4llm.to_markdown(datasheet_path)
        if output_path:
            pathlib.Path(datasheet_path.replace('.pdf', '.md')).write_bytes(md_text.encode())
