# 🚗 Car Price Prediction Web Application


- **Participant Name:** Manu Krishna C.K.
- **MUID:** manukrishnack-1@mulearn

---

# 📌 Project Overview

This project is a Machine Learning-powered web application that predicts the estimated selling price of a used car based on its specifications.

The application uses a Random Forest Regression model trained on the CarDekho Used Car Dataset. Users can enter various car details such as vehicle age, kilometers driven, mileage, engine capacity, fuel type, seller type, transmission type, and more to receive an estimated selling price instantly.

The application is built using **Streamlit** and deployed on **Streamlit Community Cloud**.

---

# 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Joblib
- Streamlit
- Git & GitHub

---

# 📂 Dataset

**Dataset:** CarDekho Used Car Price Prediction Dataset

Target Variable:

- `selling_price`

Features Used:

- Vehicle Age
- Kilometers Driven
- Mileage
- Engine Capacity
- Maximum Power
- Number of Seats
- Car Name
- Brand
- Model
- Seller Type
- Fuel Type
- Transmission Type

---

# 🤖 Machine Learning Model

- Algorithm: **Random Forest Regressor**
- Data Preprocessing:
  - Removed unnecessary columns
  - Handled missing values
  - One-Hot Encoding using `pd.get_dummies()`
- Train-Test Split
- Model Serialization using Joblib

---

# 🌐 Deployment Approach

The deployment process involved the following steps:

1. Trained the Machine Learning model using Google Colab.
2. Saved the trained model (`car_price_model.pkl`) and feature columns (`feature_columns.pkl`) using Joblib.
3. Developed the user interface using Streamlit.
4. Uploaded the complete project to GitHub.
5. Deployed the application on Streamlit Community Cloud.
6. Tested the deployed application with different user inputs to verify predictions.

---

# 📊 Key Observations

- Random Forest Regression produced reliable predictions for used car prices.
- One-Hot Encoding improved handling of categorical variables.
- Streamlit enabled rapid development of an interactive prediction interface.
- Deployment through Streamlit Community Cloud was straightforward after organizing the project files correctly.

---

# ⚠️ Challenges Faced

- Handling categorical features during deployment.
- Resolving feature mismatch errors between the trained model and the web application.
- Ensuring that the feature columns used during prediction exactly matched those used during model training.
- Configuring project structure correctly for Streamlit deployment.

---

# 🚀 Future Improvements

- Add image upload functionality for vehicle inspection.
- Include model performance metrics within the application.
- Support additional vehicle features for improved prediction accuracy.
- Improve UI with interactive charts and visual analytics.
- Deploy using Docker and cloud platforms like Render or Railway.

---

# 📁 Project Structure

```
task-9/
│── app.py
│── requirements.txt
│── README.md
│── car_price_model.pkl
│── feature_columns.pkl
│── cardekho_dataset.csv
└── Car_Price_Prediction.ipynb
```

---

# ▶️ How to Run Locally

Clone the repository

```bash
git clone <https://github.com/manukrishna804/EPOCHS-DATA-SCIENCE.git>
```

Navigate to the project

```bash
cd task-9
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
streamlit run app.py
```

---

# 🔗 GitHub Repository

**GitHub:**  
<https://github.com/manukrishna804/EPOCHS-DATA-SCIENCE.git>

---

# 🌐 Deployment Link

**Live Application:**  
<https://epochs-data-science-vyqckgwncyfwq7vaustr8w.streamlit.app/>

---

# 🙏 Acknowledgements

This project was completed as part of **Epochs '26 – Assignment 9 (Machine Learning Model Deployment)**.