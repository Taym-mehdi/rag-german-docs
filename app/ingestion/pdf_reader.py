from pypdf import PdfReader


class PDFReader:
    """
    Extracts text from PDF files.
    """

    @staticmethod
    def extract_text(file_path: str) -> str:
        reader = PdfReader(file_path)
        texts = []

        for page in reader.pages:
            text = page.extract_text()
            if text:
                texts.append(text)

        return "\n".join(texts)
