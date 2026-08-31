import streamlit as st
import joblib
import plotly.graph_objects as go

# --------------------------------------------------
# PAGE CONFIGURATION
# --------------------------------------------------

st.set_page_config(
    page_title="Food Waste Prediction System",
    page_icon="🍽️",
    layout="centered"
)

# --------------------------------------------------
# TITLE
# --------------------------------------------------

st.title("🍽️ Food Waste Prediction System")
st.write("Predict food waste using Machine Learning")

st.divider()

# --------------------------------------------------
# LOAD TRAINED MODEL
# --------------------------------------------------

try:
    model = joblib.load("food_waste_model.pkl")
except Exception as e:
    st.error("Unable to load the trained model.")
    st.stop()

# --------------------------------------------------
# MODEL EVALUATION
# --------------------------------------------------

st.subheader("📊 Model Evaluation")

col1, col2 = st.columns(2)

with col1:
    st.metric("MAE", "0.3568 kg")

with col2:
    st.metric("R² Score", "0.9157")

st.caption(
    "MAE indicates the average prediction error, while R² indicates "
    "how well the model explains the variation in food waste."
)

st.divider()

# --------------------------------------------------
# USER INPUT
# --------------------------------------------------

st.subheader("📝 Enter Details")

food_prepared = st.number_input(
    "Food Prepared (kg)",
    min_value=0.0,
    value=10.0,
    step=0.5
)

people_served = st.number_input(
    "People Served",
    min_value=0,
    value=10,
    step=1
)

temperature = st.number_input(
    "Temperature (°C)",
    min_value=0.0,
    value=25.0,
    step=0.5
)

# --------------------------------------------------
# PREDICTION
# --------------------------------------------------

if st.button("🔮 Predict Food Waste", use_container_width=True):

    # Basic validation
    if food_prepared <= 0:
        st.error("Please enter a food prepared value greater than 0.")
        st.stop()

    if people_served <= 0:
        st.error("Please enter the number of people served.")
        st.stop()

    # Make prediction
    prediction = model.predict(
        [[food_prepared, people_served, temperature]]
    )

    # Convert prediction to a normal number
    predicted_waste = float(prediction[0])

    # Food waste cannot be negative
    predicted_waste = max(0.0, predicted_waste)

    # --------------------------------------------------
    # DISPLAY PREDICTION
    # --------------------------------------------------

    st.success(
        f"🍽️ Predicted Food Waste: {predicted_waste:.2f} kg"
    )

    # --------------------------------------------------
    # WASTE CLASSIFICATION
    # --------------------------------------------------

    if predicted_waste <= 5:
        st.success("🟢 Low Food Waste")
        waste_status = "Low"

    elif predicted_waste <= 10:
        st.warning("🟡 Moderate Food Waste")
        waste_status = "Moderate"

    else:
        st.error("🔴 High Food Waste")
        waste_status = "High"

    # --------------------------------------------------
    # PREDICTION RESULT
    # --------------------------------------------------

    st.subheader("📊 Prediction Result")

    # Dynamic gauge range
    gauge_max = max(20, predicted_waste * 1.2)

    fig = go.Figure(
        go.Indicator(
            mode="gauge+number",
            value=predicted_waste,
            title={
                "text": "Predicted Food Waste (kg)"
            },
            number={
                "suffix": " kg"
            },
            gauge={
                "axis": {
                    "range": [0, gauge_max]
                },

                "bar": {
                    "thickness": 0.7
                },

                "steps": [
                    {
                        "range": [0, min(5, gauge_max)],
                        "color": "lightgreen"
                    },

                    {
                        "range": [
                            min(5, gauge_max),
                            min(10, gauge_max)
                        ],
                        "color": "lightyellow"
                    },

                    {
                        "range": [
                            min(10, gauge_max),
                            gauge_max
                        ],
                        "color": "lightcoral"
                    }
                ],

                "threshold": {
                    "line": {
                        "color": "black",
                        "width": 4
                    },

                    "thickness": 0.75,

                    "value": predicted_waste
                }
            }
        )
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    # --------------------------------------------------
    # SUMMARY
    # --------------------------------------------------

    st.subheader("📋 Prediction Summary")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Food Prepared",
            f"{food_prepared:.1f} kg"
        )

    with col2:
        st.metric(
            "People Served",
            f"{people_served}"
        )

    with col3:
        st.metric(
            "Temperature",
            f"{temperature:.1f} °C"
        )

    st.info(
        f"**Waste Level:** {waste_status}  \n"
        f"**Predicted Waste:** {predicted_waste:.2f} kg"
    )

# --------------------------------------------------
# FOOTER
# --------------------------------------------------

st.divider()

st.caption(
    "Food Waste Prediction System | "
    "Machine Learning + Python + Streamlit"
)