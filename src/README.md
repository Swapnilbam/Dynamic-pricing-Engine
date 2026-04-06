# ⚙️ Source: Core Logic & Simulations

This folder contains the raw Python scripts responsible for executing the Data Science and mathematical operations. 

## Core Files
* `optimize_price.py`: Contains the `optimize_pricing()` function. This function uses a brute-force iterative simulation, wrapping test variables in Pandas DataFrames, to predict demand across a spectrum of possible prices ($20 - $80). It mathematically calculates which price yields the highest total revenue (Price * Demand).

## Usage
This file is designed with a dual-purpose architecture:
1. **As a Library:** It is safely imported into `api/main.py` without executing standalone code.
2. **As a Script:** It contains an `if __name__ == "__main__":` execution block, allowing developers to run dry-run simulations directly in the terminal without booting up the web servers.
