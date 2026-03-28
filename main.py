from fastapi import FastAPI
import io
from fastapi import UploadFile
import pandas as pd

app = FastAPI()

@app.get('/')
def root():
    return {"message": "Welcome to Ops-Whisperer!"}

@app.post('/upload')
async def upload_file(file: UploadFile):
    contents = await file.read()
    df = pd.read_csv(io.BytesIO(contents))
    return df.shape