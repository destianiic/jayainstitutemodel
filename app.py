import streamlit as st
import pandas as pd
import joblib

# Load model and tools
model = joblib.load("model.pkl")
scaler = joblib.load("scaler.pkl")
feature_names = joblib.load("feature_names.pkl")

st.set_page_config(page_title="Student Performance Predictor", page_icon="🎓")

st.title("🎓 Student Performance Predictor")
st.markdown("Predict whether a student will **Dropout**, **Graduate**, or is still **Enrolled** based on academic and demographic data.")

st.divider()

# Define input sections
with st.expander("🧑‍🎓 Demographic & Enrollment Details", expanded=True):
    col1, col2, col3 = st.columns(3)
    
    with col1:
        marital_status = st.selectbox("Marital Status", {
            1: "Single", 2: "Married", 3: "Widowed", 4: "Divorced", 5: "Other"
        }.items(), format_func=lambda x: x[1])
        application_mode = st.selectbox("Application Mode", list(range(1, 18)))
        application_order = st.number_input("Application Order", 1, 20)
    
    with col2:
        course = st.selectbox("Course", list(range(33)))
        daytime_evening = st.selectbox("Attendance", {1: "Daytime", 0: "Evening"}.items(), format_func=lambda x: x[1])
        prev_qual = st.selectbox("Previous Qualification", list(range(1, 19)))
    
    with col3:
        prev_qual_grade = st.number_input("Previous Qualification Grade", 0.0, 200.0)
        nacionality = st.selectbox("Nationality", list(range(1, 22)))
        gender = st.selectbox("Gender", {0: "Female", 1: "Male"}.items(), format_func=lambda x: x[1])

with st.expander("👨‍👩‍👧 Family & Financial Information"):
    col1, col2, col3 = st.columns(3)
    with col1:
        mother_qual = st.selectbox("Mother's Qualification", list(range(1, 10)))
        father_qual = st.selectbox("Father's Qualification", list(range(1, 10)))
        mother_job = st.selectbox("Mother's Occupation", list(range(1, 11)))
    
    with col2:
        father_job = st.selectbox("Father's Occupation", list(range(1, 11)))
        admission_grade = st.number_input("Admission Grade", 0.0, 200.0)
        scholarship = st.selectbox("Scholarship Holder", {0: "No", 1: "Yes"}.items(), format_func=lambda x: x[1])
    
    with col3:
        debtor = st.selectbox("Debtor", {0: "No", 1: "Yes"}.items(), format_func=lambda x: x[1])
        tuition_up_to_date = st.selectbox("Tuition Up-to-date?", {0: "No", 1: "Yes"}.items(), format_func=lambda x: x[1])
        age_enrollment = st.number_input("Age at Enrollment", 17, 70)

    displaced = st.selectbox("Displaced", {0: "No", 1: "Yes"}.items(), format_func=lambda x: x[1])
    ed_special_needs = st.selectbox("Special Educational Needs", {0: "No", 1: "Yes"}.items(), format_func=lambda x: x[1])
    international = st.selectbox("International Student", {0: "No", 1: "Yes"}.items(), format_func=lambda x: x[1])

with st.expander("📚 Academic Performance"):
    st.markdown("**1st Semester**")
    col1, col2, col3 = st.columns(3)
    with col1:
        c1_credit = st.number_input("Credited Units", 0)
        c1_enrolled = st.number_input("Enrolled Units", 0)
    with col2:
        c1_eval = st.number_input("Evaluations", 0)
        c1_approved = st.number_input("Approved Units", 0)
    with col3:
        c1_grade = st.number_input("Grade", 0.0, 20.0)
        c1_wo_eval = st.number_input("Units w/o Evaluation", 0)

    st.markdown("**2nd Semester**")
    col1, col2, col3 = st.columns(3)
    with col1:
        c2_credit = st.number_input("Credited Units", 0)
        c2_enrolled = st.number_input("Enrolled Units", 0)
    with col2:
        c2_eval = st.number_input("Evaluations", 0)
        c2_approved = st.number_input("Approved Units", 0)
    with col3:
        c2_grade = st.number_input("Grade", 0.0, 20.0)
        c2_wo_eval = st.number_input("Units w/o Evaluation", 0)

with st.expander("📈 Economic Indicators"):
    col1, col2, col3 = st.columns(3)
    with col1:
        unemployment = st.number_input("Unemployment Rate (%)", 0.0, 100.0)
    with col2:
        inflation = st.number_input("Inflation Rate (%)", -10.0, 100.0)
    with col3:
        gdp = st.number_input("GDP", 0.0, 1_000_000.0)

# Extract just the values
marital_status = marital_status[0]
daytime_evening = daytime_evening[0]
gender = gender[0]
scholarship = scholarship[0]
debtor = debtor[0]
tuition_up_to_date = tuition_up_to_date[0]
displaced = displaced[0]
ed_special_needs = ed_special_needs[0]
international = international[0]

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

# Scale input
scaled_input = input_data.copy()
scaled_input[scaled_input.columns] = scaler.transform(input_data)

# Predict
if st.button("🎯 Predict Student Outcome"):
    prediction = model.predict(scaled_input)[0]
    labels = {0: "❌ Dropout", 1: "📖 Enrolled", 2: "🎓 Graduate"}
    explanation = labels.get(prediction, "Unknown")
    st.success(f"**Predicted Outcome:** {explanation}")

# Footer
st.divider()
st.markdown("Made with ❤️ using Streamlit")
