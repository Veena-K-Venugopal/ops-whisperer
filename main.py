from fastapi import FastAPI
from fastapi import UploadFile
import io, pandas as pd
from analysis import load_inventory, get_low_stock, get_inventory_value, get_category_summary

app = FastAPI()

@app.get('/')
def root():
    return {"message": "Welcome to Ops-Whisperer!"}

@app.post('/upload')
async def upload_file(file: UploadFile):
    contents = await file.read()
    df = pd.read_csv(io.BytesIO(contents))
    return {"low_stock": get_low_stock(df).to_dict(orient='records'),
            "inventory_value": get_inventory_value(df),
            "category_summary":get_category_summary(df).reset_index().to_dict(orient='records'),
            }