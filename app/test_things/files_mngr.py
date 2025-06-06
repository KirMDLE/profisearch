from pathlib import Path
from typing import List
from fastapi import FastAPI, File, HTTPException, UploadFile
from fastapi.responses import StreamingResponse, FileResponse
import uuid
app = FastAPI()

@app.post('/files')
async def file_mngr(uploaded_file: UploadFile):
    file = uploaded_file.file
    filename = uploaded_file.filename
    with open(filename, 'wb') as f:
        f.write(file.read())



@app.post('/multi_files')
async def multi_files_mngr(uploaded_files: List[UploadFile]):
    for uploaded_file in uploaded_files:
        file = uploaded_file.file
        filename = uploaded_file.filename
        with open(f'1_{filename}', 'wb') as f:
            f.write(file.read())



@app.get('/files/{filename}')
async def get_file(filename: str):
    return FileResponse(filename)


def iterfile(filename: str):
    with open(filename, 'rb') as file:
        while chunk := file.read(1024 * 1024):
            yield chunk



@app.get('/files/stream/{filename}')
async def get_stream_file(filename: str):
    return StreamingResponse(iterfile(filename), media_type='video/mp4')


@app.delete('/files/{filename}')
async def delete_file(filename: str):
    path = Path(filename)
    if not path.exists():
        raise HTTPException(status_code=404, detail="File not found")
    try:
        path.unlink()
        return {"detail": f"File '{filename}' deleted"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    

@app.get('/files')
async def list_files():
    files = [f.name for f in Path('.').iterdir() if f.is_file()]
    return {"files": files}