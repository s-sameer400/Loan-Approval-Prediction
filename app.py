import streamlit as st
import pandas as pd
import pickle

# Load trained model from the specified path
model = pickle.load(open("loan_model.pkl", "rb"))
st.title("🏦 Loan Approval Prediction")

st.write("Enter the applicant details below:")

Gender = st.selectbox("Gender", ["Male", "Female"])
Married = st.selectbox("Married", ["Yes", "No"])
Dependents = st.selectbox("Dependents", ["0", "1", "2", "3+"])
Education = st.selectbox("Education", ["Graduate", "Not Graduate"])
Self_Employed = st.selectbox("Self Employed", ["Yes", "No"])
ApplicantIncome = st.number_input("Applicant Income", min_value=0)
CoapplicantIncome = st.number_input("Coapplicant Income", min_value=0)
LoanAmount = st.number_input("Loan Amount", min_value=0)
Loan_Amount_Term = st.number_input("Loan Amount Term", min_value=0)
Credit_History = st.selectbox("Credit History", [1, 0])
Property_Area = st.selectbox("Property Area", ["Urban", "Semiurban", "Rural"])

# Encoding
Gender = 1 if Gender == "Male" else 0
Married = 1 if Married == "Yes" else 0
Education = 1 if Education == "Graduate" else 0
Self_Employed = 1 if Self_Employed == "Yes" else 0

dep = {"0": 0, "1": 1, "2": 2, "3+": 3}
Dependents = dep[Dependents]

area = {"Urban": 2, "Semiurban": 1, "Rural": 0}
Property_Area = area[Property_Area]

if st.button("Predict Loan Status"):

    data = pd.DataFrame([[Gender,
                          Married,
                          Dependents,
                          Education,
                          Self_Employed,
                          ApplicantIncome,
                          CoapplicantIncome,
                          LoanAmount,
                          Loan_Amount_Term,
                          Credit_History,
                          Property_Area]],
                        columns=[
                            "Gender",
                            "Married",
                            "Dependents",
                            "Education",
                            "Self_Employed",
                            "ApplicantIncome",
                            "CoapplicantIncome",
                            "LoanAmount",
                            "Loan_Amount_Term",
                            "Credit_History",
                            "Property_Area"
                        ])

    prediction = model.predict(data)

    if prediction[0] == 1:
        st.success("Loan Approved")
    else:
        st.error("Loan Rejected")
