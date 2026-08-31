# 🍽️ Food Waste Prediction System

A Machine Learning-based web application that predicts food waste using parameters such as food prepared, people served, and temperature.

## 🚀 Live Demo

[Open Food Waste Prediction System](https://foodwasteprediction-5eyvaceqkogmfvizbcszyh.streamlit.app/)

## 📌 Project Description

Food waste is a major problem that can lead to the unnecessary use of food, money, energy, and other resources.

This project uses Machine Learning to predict the amount of food waste based on important factors related to food service.

The system takes the following inputs:

- Food Prepared (kg)
- People Served
- Temperature (°C)

The trained Machine Learning model processes these inputs and predicts the expected amount of food waste.

The prediction model is integrated into an interactive Streamlit web application.

## 🎯 Objectives

The main objectives of this project are:

- To develop a Machine Learning model for predicting food waste.
- To estimate food waste based on food prepared, people served, and temperature.
- To evaluate the performance of the Machine Learning model.
- To provide an easy-to-use web interface.
- To visualize prediction results using an interactive chart.
- To help support better food planning and reduce unnecessary waste.

## 🛠️ Technologies Used

- **Python** – Programming language
- **Pandas** – Data processing and analysis
- **NumPy** – Numerical operations
- **Scikit-learn** – Machine Learning
- **Plotly** – Interactive data visualization
- **Streamlit** – Web application framework
- **Joblib** – Loading the trained Machine Learning model
- **GitHub** – Version control and project hosting

## 📂 Project Structure

```text
Food_Waste_Prediction/
│
├── dataset/
│   └── food_waste.csv
│
├── app.py
├── food_waste_model.pkl
├── requirements.txt
└── README.md
```

### File Description

| File / Folder | Description |
|---|---|
| `dataset/` | Contains the food waste dataset |
| `food_waste.csv` | Dataset used for the Machine Learning project |
| `app.py` | Streamlit application and prediction interface |
| `food_waste_model.pkl` | Trained Machine Learning model |
| `requirements.txt` | Python libraries required to run the project |
| `README.md` | Project documentation |

## 📊 Model Evaluation

The Machine Learning model is evaluated using the following metrics:

### Mean Absolute Error (MAE)

**MAE = 0.3568 kg**

MAE represents the average absolute difference between the actual food waste and the predicted food waste.

A lower MAE indicates lower prediction error.

### R² Score

**R² Score = 0.9157**

R² Score indicates how well the model explains the variation in the target variable.

A value closer to 1 generally indicates stronger model performance.

## ✨ Features

The application provides the following features:

- 🍽️ Food waste prediction
- 📊 Model evaluation metrics
- 📝 User input form
- 📈 Interactive Plotly visualization
- 🟢 Low waste classification
- 🟡 Moderate waste classification
- 🔴 High waste classification
- ✅ Input validation
- 🌐 Online Streamlit deployment

## 🔄 Working Process

The system follows these steps:

```text
User enters details
        ↓
Food Prepared
People Served
Temperature
        ↓
Input Processing
        ↓
Trained Machine Learning Model
        ↓
Food Waste Prediction
        ↓
Waste Classification
        ↓
Plotly Visualization
        ↓
Prediction Result
```

## ▶️ How to Run the Project Locally

### 1. Clone the Repository

```bash
git clone https://github.com/harshitha-s-nayak/Food_Waste_Prediction.git
```

### 2. Open the Project Folder

```bash
cd Food_Waste_Prediction
```

### 3. Install Required Libraries

```bash
pip install -r requirements.txt
```

### 4. Run the Streamlit Application

```bash
streamlit run app.py
```

The application will open in your web browser.

## 📦 Requirements

The project requires the following Python libraries:

```text
pandas
numpy
scikit-learn
streamlit
plotly
```

## 🌐 Deployment

The application is deployed using **Streamlit Community Cloud**.

The source code is hosted on GitHub and connected to the Streamlit deployment.

### Live Application

[Food Waste Prediction System](https://foodwasteprediction-5eyvaceqkogmfvizbcszyh.streamlit.app/)

## 📈 Example Prediction

The user provides:

```text
Food Prepared: 10 kg
People Served: 10
Temperature: 25 °C
```

The Machine Learning model processes these values and produces an estimated food waste value.

The application then displays:

- Predicted Food Waste
- Waste Level
- Gauge visualization
- Input summary

## 🌱 Benefits

This system can help:

- Improve food preparation planning.
- Reduce unnecessary food waste.
- Support data-driven decision making.
- Provide quick food waste estimates.
- Demonstrate the practical use of Machine Learning.

## 🔮 Future Enhancements

Future versions of the project can include:

- Adding more real-world datasets.
- Including additional prediction parameters.
- Comparing multiple Machine Learning algorithms.
- Improving model validation and accuracy.
- Adding historical prediction analysis.
- Adding more data visualizations.
- Providing downloadable prediction reports.
- Adding a database for storing prediction history.

## ⚠️ Limitations

- Prediction quality depends on the quality and size of the training dataset.
- The current model uses a limited number of input parameters.
- Real-world food waste can be influenced by many additional factors.
- Predictions should be considered estimates rather than exact measurements.

## 👩‍💻 Author

**Harshitha S**

Information Science and Engineering

## 📜 License

This project is developed for educational and academic purposes.
