import os
from PyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter

# Replace with your PDF file path
_root = os.path.dirname(__file__)
pdf_path = os.path.join(_root, "tps92520-q1.pdf")

# Open the PDF
with open(pdf_path, 'rb') as file:
    pdf_reader = PdfReader(file)

    # Extract text from each page
    text = ""
    for page_num in range(len(pdf_reader.pages)):
        page = pdf_reader.pages[page_num]
        text += page.extract_text()


# Initialize the text splitter
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)

# Split the text into chunks
chunks = text_splitter.split_text(text)
print()
