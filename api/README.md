# ⚡ API Backend (FastAPI)

This folder contains the FastAPI application that serves our trained Machine Learning model. It dynamically loads `demand_model.joblib` from the `models/` directory, takes real-time market conditions as input, and returns the mathematically optimized price point.

## How to Run Locally

Start the server from the root directory of the project:
```bash
uvicorn api.main:app --reload
