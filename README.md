# Medical Insurance Cost Prediction

This project predicts medical insurance costs based on personal and health-related features using a machine learning model.

## Overview

The goal of this project is to explore how factors such as age, BMI, smoking status, and number of children influence medical insurance charges, and to build a model that can estimate insurance costs for new data.

## Dataset

The dataset (`insurance.csv`) contains the following features:

- Age  
- Sex  
- BMI  
- Number of children  
- Smoking status  
- Region  
- Insurance charges (target variable)

## Project Structure

- `insurance.csv` – Dataset used for training and testing  
- `task_5.ipynb` – Data exploration, preprocessing, and model training  
- `model.pkl` – Saved trained machine learning model  
- `insurance_app.py` – Application script for making predictions  
- `requirements.txt` – Required Python libraries  

## Tools and Technologies

- Python  
- Pandas  
- NumPy  
- Scikit-learn  

## How It Works

1. The dataset is loaded and preprocessed.  
2. A regression model is trained to learn the relationship between input features and insurance charges.  
3. The trained model is saved and used to make predictions on new inputs through the application script.

## Installation

Clone the repository:

```bash
git clone https://github.com/AnthonyChukwuemekaMfon/medical_insurance_cost.git
cd medical_insurance_cost

