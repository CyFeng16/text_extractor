import shutil
import tempfile

from fastapi import FastAPI, File, UploadFile
from starlette.responses import JSONResponse

from func import extract_text

app = FastAPI()


@app.post("/extract_text")
async def extract_text_endpoint(
    file: UploadFile = File(...),
) -> JSONResponse:
    """
    Receives an image file and extracts text from it using PaddleOCR.
    """
    try:
        # Create a temporary file within a with-statement for automatic cleanup
        with tempfile.NamedTemporaryFile(delete=False) as temp_file:
            shutil.copyfileobj(file.file, temp_file)
            # Ensure the file's current position is at the start
            temp_file.seek(0)
            # Note: The temp_file.name contains the full path to the temporary file
            # Use the temporary file's path to extract text from the image
            result = extract_text(temp_file.name)
        # The temporary file is automatically deleted upon exiting the with block
        return JSONResponse(
            status_code=200,
            content=result,
        )
    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={"status": "error", "message": str(e)},
        )
