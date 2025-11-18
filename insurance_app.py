# Importing dependencies
import streamlit as st
import pandas as pd
import joblib

# Loading the saved model and columns
saved_model = joblib.load(open("model.pkl", "rb"))
X_columns = joblib.load(open("X_columns.pkl", "rb"))

# Loading the dataset
insurance_df = pd.read_csv("insurance.csv")

# Creating a function for prediction
def insurance_prediction(input_data):
    # Converting to a dataframe
    input_df = pd.DataFrame([input_data], columns=X_columns)
    # Making predictions
    prediction = saved_model.predict(input_df)
    return prediction[0]

def main():
    # Giving a title for the app
    st.title("Medical Insurance Cost Web App")
    
    # Getting user input
    lastname = st.text_input("Enter your last name: ")
    firstname = st.text_input("Enter your first name: ")
    
    age = st.number_input("Age:", 18, 63, 19)
    
    sex_list = ["Male", "Female"]
    sex = st.radio("Sex:", sex_list).lower()
    
    bmi = st.slider("BMI:", 10.0, 50.0, 26.0, step=0.1)
    
    children = st.number_input("Number of children:", 0, 5, 1)
    
    smoker = st.radio("Do you smoke?", ["Yes", "No"]).lower()
    
    region_list = insurance_df["region"].unique().tolist()
    region = st.selectbox("Select region:", region_list)
    
    # Code for prediction
    insurance_pred = ""
     # Creating a button to generate the predictive result
    if st.button("Prediction result"):
        if firstname.strip() == "" or lastname.strip() == "":
            st.warning("Please, enter your full name before generating prediction!")
        else:
            insurance_pred = insurance_prediction([age, sex, bmi, children, smoker, region])
            st.success(f"{lastname} {firstname}, your medical insurance cost is ${round(insurance_pred)}")
    
if __name__ == "__main__":
    main()