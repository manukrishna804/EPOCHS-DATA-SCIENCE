# 📞 Customer Churn Prediction

## Participant Details

**Name:** Manu Krishna

**MUID:** manukrishnack-1@mulearn



---

## Project Overview

Customer Churn Prediction is a Machine Learning web application that predicts whether a customer is likely to discontinue a service based on customer demographics, subscription details, spending behavior, and service usage.

The application is powered by a **Random Forest Classifier** trained on the Customer Churn Dataset and deployed using **Streamlit Community Cloud**, allowing users to interact with the model through an intuitive web interface and receive real-time predictions.

---

## Dataset

**Customer Churn Dataset**

Source:
https://www.kaggle.com/datasets/muhammadshahidazeem/customer-churn-dataset

---

## Features

- Predict customer churn in real time
- Interactive Streamlit interface
- Dropdown menus for categorical inputs
- Numeric input fields for customer details
- Prediction confidence using model probabilities
- Displays customer churn or retention prediction
- Responsive and user-friendly interface

---

## Machine Learning Workflow

1. Data preprocessing
2. Handling missing values
3. Label encoding of categorical features
4. Train-test split
5. Random Forest Classifier training
6. Model evaluation
7. Model serialization using Joblib
8. Integration with Streamlit
9. Deployment on Streamlit Community Cloud

---

## Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Joblib
- Streamlit
- Git
- GitHub

---

## Project Structure

```
task-9/
└── car-price-prediction/
    ├── app.py
    ├── requirements.txt
    ├── README.md
    └── model/
        ├── model.pkl
        └── label_encoders.pkl
```

---

## Deployment Approach

The machine learning model was trained locally using Scikit-learn and serialized using Joblib.

The Streamlit application loads the saved model and label encoders, collects user inputs, performs preprocessing, generates predictions, and displays the results in real time.

The complete project was pushed to GitHub and deployed using Streamlit Community Cloud.

---

## Key Observations

- Random Forest achieved very high prediction accuracy on the cleaned dataset.
- Proper preprocessing significantly improved model reliability.
- Customer spending, tenure, subscription type, and support interactions contribute to churn prediction.
- Streamlit enables rapid deployment of machine learning models with minimal backend development.

---

## Challenges Faced

- Handling missing values in the dataset
- Encoding categorical variables correctly
- Saving and loading trained models
- Managing relative file paths during deployment
- Deploying an application stored inside a subfolder of a GitHub repository
- Ensuring compatibility between local execution and Streamlit Community Cloud

---

## Future Improvements

- Improve UI/UX with custom themes
- Display feature importance
- Add batch prediction using CSV upload
- Support multiple machine learning models
- Visualize prediction confidence with charts
- Deploy using Docker for portability
- Add user authentication and prediction history

---

## Installation

Clone the repository

```bash
git clone <repository-url>
```

Move to the project directory

```bash
cd task-9/car-price-prediction
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

## Deployment

**Platform:** Streamlit Community Cloud

Deployment Link:https://epochs-data-science-mikttceq2uaasvl3xxsq7r.streamlit.app/

---
