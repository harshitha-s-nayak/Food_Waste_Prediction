import streamlit as st
import pandas as pd
import joblib
import plotly.graph_objects as go

st.title("🍽️ Food Waste Prediction System")
st.write("Predict food waste using Machine Learning")
# Load trained model
model = joblib.load("food_waste_model.pkl")
st.subheader("📊 Model Evaluation")

col1, col2 = st.columns(2)

with col1:
    st.metric("MAE", "0.3568 kg")

with col2:
    st.metric("R² Score", "0.9157")
st.subheader("Enter Details")
food_prepared = st.number_input("Food Prepared (kg)", min_value=0.0)
people_served = st.number_input("People Served", min_value=0)
temperature = st.number_input("Temperature (°C)", min_value=0.0)
if st.button("Predict Food Waste"):
    prediction = model.predict(
        [[food_prepared, people_served, temperature]]
    )
    st.success(f"Predicted Food Waste: {prediction[0]:.2f} kg")
    if prediction[0] <= 5:
        st.success("🟢 Low Food Waste")
    elif prediction[0] <= 10:
        st.warning("🟡 Moderate Food Waste")
    else:
        st.error("🔴 High Food Waste")
    #Prediction result chart   
        import plotly.graph_objects as go

# Prediction
prediction = model.predict(
    [[food_prepared, people_served, temperature]]
)

predicted_waste = prediction[0]

st.success(f"Predicted Food Waste: {predicted_waste:.2f} kg")

# Prediction Result Chart
st.subheader("📊 Prediction Result")

fig = go.Figure(go.Indicator(
    mode="gauge+number",
    value=predicted_waste,
    title={"text": "Predicted Food Waste (kg)"},
    number={"suffix": " kg"},
    gauge={
        "axis": {"range": [0, 20]},
        "bar": {"thickness": 0.7},
        "steps": [
            {"range": [0, 5], "color": "lightgreen"},
            {"range": [5, 10], "color": "lightyellow"},
            {"range": [10, 20], "color": "lightcoral"}
        ],
        "threshold": {
            "line": {"width": 4},
            "thickness": 0.75,
            "value": predicted_waste
        }
    }
))

st.plotly_chart(fig, use_container_width=True)