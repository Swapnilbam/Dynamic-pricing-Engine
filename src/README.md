# Dynamic Pricing Optimization Engine 🚀

**A Machine Learning Capstone Project**

This project is an AI-driven pricing engine designed for e-commerce. It uses historical sales data, competitor pricing, and demand forecasting to calculate the absolute optimal price point that maximizes overall revenue.

## 🏗️ Current Architecture (`src/` folder)

Currently, the core Machine Learning and optimization logic is complete:

* **`data_generator.py`**: A simulator that generates a synthetic e-commerce dataset, hardcoding hidden economic rules like price elasticity and competitor effects.
* **`train_model.py`**: The predictive engine. It uses a Linear Regression model to analyze the synthetic data, successfully reverse-engineering the hidden mathematical rules with a high R-squared accuracy.
* **`optimize_price.py`**: The prescriptive engine. It simulates thousands of pricing scenarios against the trained ML model to output the exact price that will yield the maximum projected revenue.

## ⚙️ How to Run Locally

1. Clone this repository.
2. Create a virtual environment and install the required dependencies (pandas, scikit-learn, joblib).
3. Run the scripts sequentially:
   ```bash
   python src/data_generator.py
   python src/train_model.py
   python src/optimize_price.py
