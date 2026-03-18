import numpy as np
import pandas as pd
import os

def generate_ecommerce_data(days = 1000):
    np.random.seed(42)
    days_of_year = np.arange(1,days + 1)
    is_weekend = np.where(days_of_year % 7 >=5, 1,0)

    competitor_price = np.random.normal(50,5,days)
    our_price = competitor_price + np.random.normal(0,3,days)

    base_demand = 200
    price_elasticity = -2.5 * our_price
    competitor_effect = 1.5 * competitor_price
    weekend_boost = 50 * is_weekend
    noise = np.random.normal(50,5,days)
    
    demand  = base_demand + price_elasticity + competitor_effect + weekend_boost + noise 
    demand = np.maximum(demand,0) 

    df = pd.DataFrame({
        'day' : days_of_year,
        'is_weekend' : is_weekend,
        'competitor_price' : np.round(competitor_price,2),
        'our_price' : np.round(our_price,2),
        'units_sold' : np.round(demand,0).astype(int)
    })

    return df

if __name__ == "__main__":
    os.makedirs('data/raw',exist_ok = True)

    dataset = generate_ecommerce_data()
    dataset.to_csv('data/raw/historical_sales.csv',index = False)
    print("Dataset generated successfully at data/raw/historical_sales.csv")
    print(dataset.head())