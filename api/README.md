# ⚡ API Backend (FastAPI)

This folder contains the FastAPI application that serves our trained Machine Learning model (`demand_model.joblib`). It takes real-time market conditions as input and returns the mathematically optimized price point to maximize revenue.

## How to Run Locally

Start the server from the root directory of the project:
```bash
uvicorn api.main:app --reload
