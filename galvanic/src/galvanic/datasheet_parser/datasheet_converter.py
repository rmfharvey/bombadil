import pymupdf4llm
import pathlib
from galvanic import colored_logger


class DatasheetReader:
    logger = colored_logger("DatasheetReader")

    @staticmethod
    def to_markdown(datasheet_path, output_path=None):
        """Convert PDF datasheet to markdown.

        :param datasheet_path:
        :param output_path:
        :return:
        """
        # # Check if path is a url, if so, download
        # result = urlparse(datasheet_path)
        # is_url = all([result.scheme, result.netloc])
        # try:
        #     if is_url:
        #         response = requests.get(datasheet_path, stream=True)
        #         assert response.status_code == "200", f"Failed to get file from {datasheet_path}"
        #         with tempfile.NamedTemporaryFile() as tmp:
        #             datasheet_path = tempfile.name
        #             for chunk in response.iter_content(chunk_size=1024):
        #                 if chunk:
        #                     tmp.write(chunk)
        # except AssertionError as err:
        #     DatasheetReader.logger.error(err)

        DatasheetReader.logger.info(f"Converting {datasheet_path} to markdown")
        md_text = pymupdf4llm.to_markdown(datasheet_path)

        if output_path:
            pathlib.Path(output_path).write_bytes(md_text.encode())

        return md_text
