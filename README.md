# 📈 Dynamic Pricing AI Engine

An end-to-end Machine Learning pipeline and decoupled web application that simulates market conditions and mathematically calculates the optimal pricing strategy to maximize projected revenue.

## 🚀 Architecture Overview

This project uses a decoupled microservice architecture:
1. **The Core Engine (`/src`):** A custom mathematical simulation algorithm utilizing Pandas and Scikit-Learn to brute-force demand predictions against a trained ML model.
2. **The Backend API (`/api`):** A RESTful FastAPI server that loads the ML model into memory and serves predictions via the `/optimize-price` endpoint.
3. **The Frontend Dashboard (`/frontend`):** An interactive Streamlit web UI that allows users to adjust market parameters (competitor pricing, day of the week) and visualize the AI's real-time recommendations.

## 🛠️ Tech Stack
* **Machine Learning:** Scikit-Learn, Pandas, NumPy, Joblib
* **Backend API:** FastAPI, Uvicorn, Pydantic
* **Frontend UI:** Streamlit, Requests
* **Language:** Python 3.x

## 💻 How to Run the Application Locally

Because this application relies on a decoupled architecture, you must run the Backend and the Frontend simultaneously in two separate terminals.

### Step 1: Start the AI Backend (Terminal 1)
1. Open a terminal in the root directory.
2. Activate your virtual environment: `.\venv\Scripts\activate` (Windows)
3. Start the FastAPI server:
   ```bash
   uvicorn api.main:app --reload

### Built by Swapnil Bam
