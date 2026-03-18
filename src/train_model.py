import pandas as pd
import os
import joblib
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error,r2_score
from sklearn.linear_model import LinearRegression

def train_demand_model():
    print("Loading data....")

    df = pd.read_csv('data/raw/historical_sales.csv')
    X = df[['is_weekend','competitor_price','our_price']]
    Y = df['units_sold']

    X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size = 0.2,random_state = 42)
    print("Training Machine Learning Model....")

    model = LinearRegression()
    model.fit(X_train,Y_train)
    
    predictions = model.predict(X_test)
    mae = mean_absolute_error(Y_test,predictions)
    r2 = r2_score(Y_test,predictions)

    print("\n--- Model Evaluation ---")
    print(f"Mean Absolute Error : {mae:.2f} units")
    print(f"R-Squared Score : {r2:.4f}")

    print("\n--- Learned Coefficients ---")
    coefficients = pd.DataFrame(model.coef_,X.columns,columns = ['Coefficient'])
    print(coefficients)

    os.makedirs('models',exist_ok = True)
    model_path = ('models/demand_model.joblib')
    joblib.dump(model,model_path)

    print(f"\nModel Successfully saved to {model_path}")

if __name__ == "__main__":
    train_demand_model()