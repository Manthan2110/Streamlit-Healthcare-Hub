# 🧠 Streamlit Healthcare Hub 🔍

Welcome to your personal AI-powered doctor’s assistant!  
This **Streamlit web application** combines machine learning with clinical insight to help predict **five major diseases**—just by entering symptoms or medical parameters.

---

## 💻 Web App Preview

![App Preview](https://github.com/user-attachments/assets/your-screenshot.png) <!-- Replace with your screenshot -->

---

## 🧠 Problem Statement

Healthcare accessibility is limited in many areas. Many people either ignore early symptoms or misjudge their seriousness.  
This tool addresses that gap by providing **quick, AI-driven disease risk assessments** that can help users take timely medical action.

> ### ❓ “Can we predict a health condition using basic clinical data or visible symptoms without a hospital visit?”

---

## 🚀 Features

- 💡 Symptom-to-Disease Analyzer with intelligent suggestions
- 🔬 Disease prediction powered by **pre-trained ML models**
- 📥 Option to download diagnosis reports
- 🧑‍⚕️ Doctor-style health recommendations
- 🎨 Custom styled UI with sidebar navigation and hover effects

---

## 🦠 Diseases Covered

| Module | What it Does |
|--------|---------------|
| 🧪 **Infectious/Skin Diseases** | Symptom-based disease classifier with 40+ conditions |
| 🩸 **Diabetes** | Predicts risk using inputs like glucose, BMI, insulin, age |
| 💓 **Heart Disease** | Uses ECG, cholesterol, angina, age, etc. to predict heart risk |
| 🧠 **Parkinson’s** | Detects voice-based markers for early signs of Parkinson’s |
| 🎀 **Breast Cancer** | Predicts malignancy using 12 clinical cell measurements |

---

## 📦 Backend Files Used

| File Name | Purpose |
|-----------|---------|
| `app.py` | Streamlit frontend with routing, CSS, and prediction logic |
| `Random_forest_model.pkl` | Infectious Disease model (symptom-based) |
| `diabetes_model.pkl` | Diabetes ML model |
| `heart_disease_model.pkl` | Heart Disease ML model |
| `parkinsons_model.pkl` | Parkinson's ML model |
| `breast_cancer_model.pkl` | Breast Cancer ML model |

> All ML models are trained via corresponding `.ipynb` files.

---

## 🧠 Machine Learning Models

- Trained using **Random Forest**, **SVM**, and **Logistic Regression**
- Feature selection and normalization applied
- Outputs binary classification (0 = No Disease, 1 = Disease)

---

## 🛠️ Tech Stack

- **Frontend:** Streamlit, Streamlit Option Menu
- **Backend:** Python, scikit-learn, joblib, pickle
- **IDE:** Jupyter Notebook 
- **UI Styling:** Custom CSS with markdown embedding

---

## 💡 Sample Insights

- 📋 Symptom-based model can predict over 40 common diseases
- 🧪 Blood test values help catch **Diabetes** early
- 💓 ECG & heart rate trends help detect **Cardiac risks**
- 🧠 Voice modulation signals help identify **Parkinson’s**
- 🎗️ Cell morphology stats help catch **Breast Cancer**

---

## 📄 Report Generation

Each module provides:
- 📍 Disease Prediction
- 📌 Doctor-style Recommendations
- 🧾 Option to download a `.txt` report

---

## 🚀 How to Run

1. Clone the repo:
```bash
git clone https://github.com/your-username/smart-medical-diagnosis
cd smart-medical-diagnosis
