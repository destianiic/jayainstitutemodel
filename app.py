import streamlit as st
import pandas as pd
import joblib

# Load model and tools
model = joblib.load("model.pkl")
scaler = joblib.load("scaler.pkl")
feature_names = joblib.load("feature_names.pkl")

st.title("🎓 Student Performance Predictor")

# Define input fields
marital_status = st.selectbox("Marital Status", [1, 2, 3, 4, 5])
application_mode = st.selectbox("Application Mode", list(range(1, 18)))
application_order = st.number_input("Application Order", 1, 20)
course = st.selectbox("Course", list(range(33)))
daytime_evening = st.selectbox("Attendance", [1, 0])
prev_qual = st.selectbox("Previous Qualification", list(range(1, 19)))
prev_qual_grade = st.number_input("Previous Qualification Grade", 0.0, 200.0)
nacionality = st.selectbox("Nationality", list(range(1, 22)))
mother_qual = st.selectbox("Mother's Qualification", list(range(1, 10)))
father_qual = st.selectbox("Father's Qualification", list(range(1, 10)))
mother_job = st.selectbox("Mother's Occupation", list(range(1, 11)))
father_job = st.selectbox("Father's Occupation", list(range(1, 11)))
admission_grade = st.number_input("Admission Grade", 0.0, 200.0)
displaced = st.selectbox("Displaced", [0, 1])
ed_special_needs = st.selectbox("Educational Special Needs", [0, 1])
debtor = st.selectbox("Debtor", [0, 1])
tuition_up_to_date = st.selectbox("Tuition Fees Up to Date", [0, 1])
gender = st.selectbox("Gender", [0, 1])  # 0 = female, 1 = male
scholarship = st.selectbox("Scholarship Holder", [0, 1])
age_enrollment = st.number_input("Age at Enrollment", 17, 70)
international = st.selectbox("International Student", [0, 1])

# Academic performance fields
c1_credit = st.number_input("1st Sem Credited Units", 0)
c1_enrolled = st.number_input("1st Sem Enrolled Units", 0)
c1_eval = st.number_input("1st Sem Evaluations", 0)
c1_approved = st.number_input("1st Sem Approved Units", 0)
c1_grade = st.number_input("1st Sem Grade", 0.0, 20.0)
c1_wo_eval = st.number_input("1st Sem Units w/o Evaluation", 0)

c2_credit = st.number_input("2nd Sem Credited Units", 0)
c2_enrolled = st.number_input("2nd Sem Enrolled Units", 0)
c2_eval = st.number_input("2nd Sem Evaluations", 0)
c2_approved = st.number_input("2nd Sem Approved Units", 0)
c2_grade = st.number_input("2nd Sem Grade", 0.0, 20.0)
c2_wo_eval = st.number_input("2nd Sem Units w/o Evaluation", 0)

unemployment = st.number_input("Unemployment Rate", 0.0, 100.0)
inflation = st.number_input("Inflation Rate", -10.0, 100.0)
gdp = st.number_input("GDP", 0.0, 1_000_000.0)

# Assemble input dataframe
input_data = pd.DataFrame([[
    marital_status, application_mode, application_order, course,
    daytime_evening, prev_qual, prev_qual_grade, nacionality,
    mother_qual, father_qual, mother_job, father_job,
    admission_grade, displaced, ed_special_needs, debtor,
    tuition_up_to_date, gender, scholarship, age_enrollment,
    international, c1_credit, c1_enrolled, c1_eval, c1_approved,
    c1_grade, c1_wo_eval, c2_credit, c2_enrolled, c2_eval,
    c2_approved, c2_grade, c2_wo_eval, unemployment, inflation, gdp
]], columns=feature_names)

# Scale numerical values
scaled_input = input_data.copy()
scaled_input[scaled_input.columns] = scaler.transform(input_data)

# Predict
if st.button("Predict"):
    prediction = model.predict(scaled_input)[0]
    labels = {0: "Dropout", 1: "Enrolled", 2: "Graduate"}
    explanation = labels.get(prediction, "Unknown")
    
    st.success(f"🎯 Predicted Performance: {prediction} — {explanation}")
