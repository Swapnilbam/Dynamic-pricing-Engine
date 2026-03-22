from fastapi import FastAPI 
from pydantic import BaseModel
from src.optimize_price import optimize_pricing  


app = FastAPI(title="Dynamic Pricing AI Engine")
class MarketConditions(BaseModel):
    is_weekend : int
    competitor_price : float 


@app.post("/optimize-price")
def get_optimized_price(data : MarketConditions):

    optimal_p,max_rev,exp_demand = optimize_pricing(data.is_weekend,data.competitor_price)

    return {
        "status" : "Success",
        "market_conditions" : {
            "Weekend" : bool(data.is_weekend),
            "competitor_price_₹" : data.competitor_price
        },
        "AI_recommendation" : {
            "Optimal_Price_₹" : float(optimal_p),
            "Expected_Demand_in_units" : float(exp_demand),
            "Maximum_Revenue_₹" : float(max_rev)
        }
    }
