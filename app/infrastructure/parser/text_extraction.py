from pypdf import PdfReader
from app.core.exceptions import TextExtractionError

#### EXTRACTIN TEXT FROM THE DOC
async def extract_text_pypdf(pdf_path):
    try:
        reader = PdfReader(pdf_path)
        text = ""
        for page in reader.pages:
            text += page.extract_text() + "\n"
    except Exception as e:
        raise TextExtractionError(detail=str(e)) from e
    return text
