import pandas as pd
import numpy as np
import joblib

def optimize_pricing(is_weekend,competitor_price):
    try:
        model = joblib.load('models/demand_model.joblib')
    except FileNotFoundError:
        return "Error : Model not Found. Did you run train_model.py first?"

    possible_prices = np.arange(20,80,1)


    best_price = 0
    max_revenue = 0  
    expected_demand_at_best = 0  

    for test_price in possible_prices:
        scenario = pd.DataFrame({
            'is_weekend' : [is_weekend],
            'competitor_price' : [competitor_price],
            'our_price' : [test_price]
        })

        predicted_demand = model.predict(scenario)[0]

        predicted_demand = max(0,predicted_demand)

        revenue = test_price * predicted_demand 
        if revenue > max_revenue:
            max_revenue = revenue 
            best_price = test_price
            expected_demand_at_best = predicted_demand 

    return best_price,max_revenue,expected_demand_at_best 

if __name__ == "__main__":

    test_weekend = 1 
    test_competitor_price = 80.0

    print(f"--- Running Pricing Simulation ---")
    print(f"Market Conditions : Weekend = {test_weekend}, Competitor_price = ${test_competitor_price}")

    best_price,max_rev,expected_demand = optimize_pricing(test_weekend,test_competitor_price)

    print(f"\n✅ Simulation Complete. Results : ")
    print(f"Recommended Price : ${best_price}")
    print(f"Expected Demand : {expected_demand:.0f} Units")
    print(f"Projected Revenue : ${max_rev:.2f}")



