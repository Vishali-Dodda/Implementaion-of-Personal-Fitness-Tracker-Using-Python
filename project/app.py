import streamlit as st
import numpy as np
import pandas as pd
import time
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

# Load Data
calories = pd.read_csv("calories.csv")
exercise = pd.read_csv("exercise.csv")

# Merge and preprocess data
data = exercise.merge(calories, on="User_ID")
data.drop(columns=["User_ID"], inplace=True)
data["BMI"] = data["Weight"] / ((data["Height"] / 100) ** 2)
data = pd.get_dummies(data, drop_first=True)

# Train-Test Split
X = data.drop("Calories", axis=1)
y = data["Calories"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)

# Train Model
model = RandomForestRegressor(n_estimators=1000, max_features=3, max_depth=6)
model.fit(X_train, y_train)

# Streamlit UI
st.set_page_config(page_title="AI-Powered Fitness Tracker", layout="wide")
st.title("🏋️ AI-Powered Personal Fitness Tracker")
st.write("Enter your details to predict calories burned and get workout recommendations.")

# User Input Sidebar
st.sidebar.header("User Input")
age = st.sidebar.slider("Age", 10, 100, 25)
bmi = st.sidebar.slider("BMI", 15, 40, 22)
duration = st.sidebar.slider("Duration (min)", 0, 60, 20)
heart_rate = st.sidebar.slider("Heart Rate", 60, 180, 85)
body_temp = st.sidebar.slider("Body Temp (C)", 36, 42, 37)
gender = st.sidebar.radio("Gender", ["Male", "Female"])
gender_encoded = 1 if gender == "Male" else 0

# Prepare Data for Prediction
input_data = pd.DataFrame({
    "Age": [age], "BMI": [bmi], "Duration": [duration],
    "Heart_Rate": [heart_rate], "Body_Temp": [body_temp], "Gender_male": [gender_encoded]
})

# Align input data with training columns
input_data = input_data.reindex(columns=X_train.columns, fill_value=0)

# Make Prediction
prediction = model.predict(input_data)[0]
st.subheader("🔥 Calories Burned Prediction")
st.metric(label="Estimated Calories Burned", value=f"{round(prediction, 2)} kcal")

# Workout Suggestions
st.subheader("🏃 Recommended Workouts")
if prediction < 100:
    st.write("💡 Light workout: Yoga, Walking")
elif prediction < 250:
    st.write("🏋️ Moderate workout: Jogging, Cycling")
else:
    st.write("🔥 Intense workout: HIIT, Running")

# Gamification (Achievement Badges)
st.subheader("🏆 Achievements")
if duration >= 30:
    st.success("🎖️ 30-Min Workout Badge Unlocked!")
if prediction >= 200:
    st.success("🔥 High Calorie Burn Badge Unlocked!")

# Visualization
st.subheader("📊 Fitness Data Overview")
fig, ax = plt.subplots()
ax.hist(data["Calories"], bins=20, color='skyblue', edgecolor='black')
ax.axvline(prediction, color='red', linestyle='dashed', linewidth=2)
st.pyplot(fig)

st.write("⚡ Keep pushing your limits and track your progress daily!")
