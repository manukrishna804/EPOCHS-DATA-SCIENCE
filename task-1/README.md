# 🏨 Hotel Booking Demand - Dataset Exploration

## 📌 Project Overview

This project explores the **Hotel Booking Demand** dataset using **Pandas** in Google Colab. The objective is to understand the dataset, identify potential business problems, frame an appropriate Machine Learning problem, and perform basic exploratory data analysis (EDA).

This project was completed as part of the **EVN DS Epochs 2026 - Day 01 Assignment**.

---

## 📂 Dataset

**Dataset Name:** Hotel Booking Demand

**Source:** https://www.kaggle.com/datasets/jessemostipak/hotel-booking-demand

### Dataset Description

The dataset contains booking information for **City Hotel** and **Resort Hotel** bookings. It includes details such as:

* Hotel type
* Booking lead time
* Arrival date
* Number of adults, children, and babies
* Country of customer
* Market segment
* Deposit type
* Previous cancellations
* Average Daily Rate (ADR)
* Booking cancellation status

The dataset consists of approximately **119,000 booking records** with **32 features**.

---

# 🎯 Objective

The objective of this project is to:

* Understand the dataset and its structure.
* Perform basic exploratory data analysis using Pandas.
* Identify business problems that can be solved using Machine Learning.
* Frame the appropriate Machine Learning problem.
* Identify the target variable and important features.

---

# 💼 Business Problem

Hotels often face significant revenue losses due to booking cancellations. Predicting whether a customer is likely to cancel a reservation can help hotels:

* Improve revenue management.
* Reduce financial losses.
* Optimize room allocation.
* Plan overbooking strategies.
* Send targeted reminders or promotional offers to customers who are likely to cancel.

---

# 🤖 Machine Learning Problem Framing

### Problem Type

**Classification (Binary Classification)**

### Justification

The target variable **`is_canceled`** has two possible values:

* **0** → Booking Not Cancelled
* **1** → Booking Cancelled

Since the objective is to predict one of two classes, this is a **Binary Classification** problem.

---

# 🎯 Target Variable

**`is_canceled`**

---

# 🔑 Key Features

Some important features that may influence booking cancellations include:

* hotel
* lead_time
* arrival_date_month
* market_segment
* deposit_type
* customer_type
* previous_cancellations
* booking_changes
* adr (Average Daily Rate)
* adults
* children
* stays_in_week_nights
* stays_in_weekend_nights

---

# 📊 Exploratory Data Analysis

The following analyses were performed using Pandas:

* Dataset Shape
* Column Information
* Data Types
* Missing Value Analysis
* Summary Statistics
* Duplicate Record Check
* Target Variable Distribution
* Basic Data Visualization

---

# 🔍 Key Observations

### Observation 1

A considerable number of hotel bookings are cancelled, indicating that cancellation prediction is an important business use case.

### Observation 2

Some columns, including **company**, **agent**, and **children**, contain missing values and require preprocessing before building a Machine Learning model.

### Observation 3

The dataset contains both numerical and categorical features, making it suitable for predictive analytics and various Machine Learning algorithms.

---

# 🛠 Technologies Used

* Google Colab
* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn

---

# 📁 Repository Structure

```text
task-1/
│── 📄 README.md
│── 📓 analysis.ipynb
│── 📊 hotel_bookings.csv
```

---

# 🚀 Conclusion

The Hotel Booking Demand dataset provides valuable insights into customer booking behavior and hotel operations. Through exploratory data analysis, a key business problem—predicting booking cancellations—was identified. Since the target variable is binary, this problem is best framed as a **Binary Classification** task. The findings from this analysis provide a strong foundation for developing predictive Machine Learning models in future work.
