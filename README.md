# README_DATAMINING_UAS_KEL10

# Customer Churn Prediction and Customer Segmentation Using XGBoost and K-Means

## 📌 Project Overview

This project was developed as part of the Final Project for the Data Mining course. The objective of this project is to predict customer churn and perform customer segmentation using machine learning techniques.

The classification task was conducted using Random Forest and XGBoost algorithms, while customer segmentation was performed using K-Means clustering. The best classification model was then deployed into a web application using Streamlit.

---

## 🎯 Objectives

* Predict customers who are likely to churn.
* Segment customers based on their characteristics.
* Develop an interactive web application for customer churn prediction and customer segmentation.

---

## 📊 Dataset

Dataset: **Bank Customer Churn Dataset**

The dataset contains customer information such as:

* Credit Score
* Geography
* Gender
* Age
* Tenure
* Balance
* Number of Products
* Has Credit Card
* Active Member Status
* Estimated Salary
* Satisfaction Score
* Point Earned
* Customer Churn Status (Exited)

---

## ⚙️ Methods Used

### Classification

* Random Forest
* Random Forest (Hyperparameter Tuning)
* XGBoost
* XGBoost (Hyperparameter Tuning)

### Clustering

* K-Means Clustering

### Framework

* CRISP-DM (Cross Industry Standard Process for Data Mining)

---

## 🏆 Best Model Performance

### XGBoost Tuned

| Metric   | Score  |
| -------- | ------ |
| Accuracy | 86.95% |
| ROC-AUC  | 87.78% |

---

## 👥 Customer Segmentation

Three customer segments were identified:

1. **Nasabah Aktif Multi-Produk**
2. **Nasabah Bernilai Tinggi Tidak Aktif**
3. **Nasabah Bernilai Tinggi Aktif**

---

## 💻 Streamlit Application Features

* Home
* Dataset Overview
* Prediction / Analysis
* Visualization
* About

---

## 📁 Project Structure

```text
Customer-Churn-Prediction/
│
├── dataset/
│   └── Bank_Customer_Churn_Clustered.csv
│
├── notebook/
│   └── analysis.ipynb
│
├── models/
│   ├── xgb_model.pkl
│   ├── scaler.pkl
│   ├── cluster_model.pkl
│   └── cluster_scaler.pkl
│
├── images/
│   ├── Top_10.png
│   ├── Matriks.png
│   └── Clustering.png
│
├── pages/
│   ├── 1_Dataset.py
│   ├── 2_Prediction.py
│   ├── 3_Visualization.py
│   └── 4_About.py
│
├── app.py
├── requirements.txt
└── README.md
```

---

## 🚀 Running the Application

Install the required libraries:

```bash
pip install -r requirements.txt
```

Run the Streamlit application:

```bash
streamlit run app.py
```

---

## 👨‍🎓 Authors

1. **Michal Rivaldo Fresca Kurniawan** (24051214167)
2. **Moh Viki Nur Arifin** (24051214167)

Data Mining Final Project.
