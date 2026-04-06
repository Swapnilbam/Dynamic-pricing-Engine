**`/api/README.md`**
```markdown
# 🧠 Backend: FastAPI Engine

This folder contains the RESTful API that acts as the bridge between the web dashboard and the Machine Learning model.

## Core Files
* `main.py`: Initializes the FastAPI application, loads the `.joblib` model into system memory using absolute pathing to prevent crash errors, and defines the POST endpoint.

## API Endpoints

### `POST /optimize-price`
Expects a JSON payload containing current market conditions and returns the mathematically optimal price point.

**Expected Input:**
```json
{
  "is_weekend": 1,
  "competitor_price": 80.0
}
