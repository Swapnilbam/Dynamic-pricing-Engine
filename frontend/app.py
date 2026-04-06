import streamlit as st 
import requests 

st.set_page_config(page_title = "Dynamic Pricing Engine", layout="centered")
st.title("📈 AI Dyanmic Dashboard")
st.write("Adjust the market conditions below to see the AI'S real-time pricing recommendations")

col1,col2 = st.columns(2) 

with col1:
    day_type = st.selectbox("Day of the Week",["Weekday","Weekend"])
    is_weekend = 1 if day_type == "Weekend" else 0  

with col2:
    competitor_price = st.number_input("Copetitor's price ($)", min_value = 10.0, max_value = 150.0, value = 50.0,step = 1.0) 


if st.button("Optimize Price 🚀"):
    api_data = {
        "is_weekend" : is_weekend,
        "competitor_price": competitor_price 
    }

    API_URL = "http://localhost:8000/optimize-price"
    try:
        with st.spinner("AI is calculating the optimal sweet spot..."):
           
            response = requests.post(API_URL, json=api_data)
            
           
            if response.status_code == 200:
                result = response.json()
                
                
                st.success("Simulation Complete!")
                
                metric_col1, metric_col2, metric_col3 = st.columns(3)
                
                metric_col1.metric("Recommended Price($)", f"${result["AI_recommendation"]["optimal_price"]:.2f}")
                metric_col2.metric("Expected Demand in Units", f"{result["AI_recommendation"]["expected_demand"]:.0f} units")
                metric_col3.metric("Projected Revenue($)", f"${result["AI_recommendation"]["projected_revenue"]:.2f}")
                
            else:
                st.error("Error: Could not calculate price. Check your API terminal!")
                
    except requests.exceptions.ConnectionError:
        st.error("🚨 Connection Error: Your FastAPI server is not running! Open a second terminal and run 'uvicorn api.main:app --reload'")