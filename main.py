from typing import Annotated, Union
from fastapi import FastAPI, File, UploadFile
# import model

app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "Hello World"}

@app.post("/files/")
async def create_file(file: Annotated[bytes | None, File()] = None):
    if not file:
        return {"message": "No file sent"}
    else:
        return {"file_size": len(file)}


@app.post("/uploadfile/")
async def create_upload_file(image: UploadFile):
    content = image.file.read()
    if not image:
        return {"message": "No upload file sent"}
    else:
        return {"filename": image.filename}