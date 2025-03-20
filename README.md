---

# 🏋️ AI-Powered Personal Fitness Tracker  

## 📌 Overview  
The **AI-Powered Personal Fitness Tracker** is a web-based application that helps users track their fitness progress, predict calories burned, and receive personalized workout recommendations. It leverages **Machine Learning (RandomForestRegressor)** for calorie prediction and provides an interactive **Streamlit UI** for an engaging user experience.  

## 🚀 Features  
- **Calorie Prediction:** Predicts the estimated calories burned based on user inputs like age, BMI, exercise duration, heart rate, and body temperature.  
- **Workout Recommendations:** Suggests workout intensity based on the predicted calorie burn.  
- **Gamification & Achievements:** Unlock badges for completing workouts and burning high calories.  
- **Data Visualization:** Displays fitness trends and calorie distribution using interactive charts.  
- **User-Friendly Interface:** A responsive and visually appealing Streamlit-based web application.  

## 🏗️ Technologies Used  
- **Python**  
- **Streamlit** (for the web interface)  
- **Pandas & NumPy** (for data handling)  
- **Scikit-Learn** (for machine learning)  
- **Matplotlib** (for data visualization)  

## 🔍 Dataset  
The application uses two datasets:  
- **calories.csv** – Contains calorie burn data for different individuals.  
- **exercise.csv** – Includes exercise-related attributes such as weight, height, heart rate, and duration.  

## ⚙️ How It Works  
1. **Data Preprocessing:**  
   - Merges **exercise.csv** and **calories.csv** based on User ID.  
   - Computes **BMI** using weight and height.  
   - Encodes categorical variables (gender).  
2. **Model Training:**  
   - Splits the data into training and testing sets.  
   - Uses a **Random Forest Regressor** with optimized hyperparameters to predict calories burned.  
3. **User Input & Prediction:**  
   - Users enter their details in the sidebar.  
   - The model predicts the estimated calories burned.  
   - Based on the prediction, suitable workout recommendations are displayed.  
4. **Gamification & Visualization:**  
   - Achievements are unlocked based on workout duration and calorie burn.  
   - A histogram of calorie distribution is shown, with the user’s prediction highlighted.  

## ▶️ Running the Application  
1. Clone the repository:  
   ```bash
   git clone https://github.com/your-repo-name.git
   cd your-repo-name
   ```
2. Install dependencies:  
   ```bash
   pip install streamlit numpy pandas matplotlib scikit-learn
   ```
3. Run the Streamlit app:  
   ```bash
   streamlit run app.py
   ```
4. Open the displayed local URL to interact with the fitness tracker.  

## 📌 Screenshots  
![image](https://github.com/user-attachments/assets/c05acfbf-f0ed-4ca4-8c36-48015780f818)

![image](https://github.com/user-attachments/assets/b1a38709-5a5c-4c82-952c-b99f521b7aaf)

