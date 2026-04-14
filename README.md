# Ops-Whisperer

An AI-assisted operations intelligence system for small retail businesses.
Upload your inventory data and get actionable metrics back — no dashboard required.

## Phase 1 — MVP Analytics API

Upload a CSV of inventory data and receive a structured JSON summary including:
- Low stock alerts
- Total inventory value
- Category-level breakdown

## Tech Stack

- Python 3.11
- FastAPI
- Pandas
- Uvicorn

## Run Locally

1. Clone the repo
2. Create and activate a virtual environment:
    - python -m venv .venv
    - source .venv/Scripts/activate  # Git Bash on Windows
3. Install dependencies:
    - pip install fastapi uvicorn pandas python-multipart
4. Start the server:
    - uvicorn main:app --reload
5. Visit `http://127.0.0.1:8000/docs` to test the upload endpoint

## CSV Format

Your CSV should have these columns:
`item_name, category, quantity, unit_price, last_restock_date`