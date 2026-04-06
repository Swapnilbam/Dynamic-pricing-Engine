# 🖥️ Frontend: Streamlit Dashboard

This folder contains the user interface for the Dynamic Pricing Engine. It is completely decoupled from the ML logic and relies entirely on HTTP requests to communicate with the FastAPI backend.

## Core Files
* `app.py`: The main Streamlit script. It constructs the UI, packages user inputs into JSON, handles the `requests.post()` call to the local API, and parses the response into metric visualizers.

## Configuration
By default, the dashboard looks for the API at `http://localhost:8000/optimize-price`. If your Uvicorn server boots up on a different port (e.g., 8001), you must update the `API_URL` variable inside `app.py` before running the dashboard.
