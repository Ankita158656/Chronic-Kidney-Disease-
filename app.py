import streamlit as st
import joblib
import numpy as np

# Load the saved Logistic Regression model
model = joblib.load("best_model_logistic_regression.pkl")

# Function to make predictions
def predict_ckd(features):
    features = np.array(features).reshape(1, -1)
    prediction = model.predict(features)[0]
    probability = model.predict_proba(features)[0][1] * 100
    return "Positive" if prediction == 1 else "Negative", probability

# Streamlit UI
st.title("Chronic Kidney Disease Prediction")
st.write("Enter patient details to check for CKD risk.")

# User inputs based on selected features
ethnicity = st.selectbox("Ethnicity", ["Group A", "Group B", "Group C"])
physical_activity = st.selectbox("Physical Activity", ["Low", "Moderate", "High"])
systolic_bp = st.number_input("Systolic Blood Pressure", min_value=80, max_value=200, value=120)
fasting_blood_sugar = st.number_input("Fasting Blood Sugar (mg/dL)", min_value=50, max_value=400, value=90)
serum_creatinine = st.number_input("Serum Creatinine (mg/dL)", min_value=0.1, max_value=15.0, value=1.2)
bun_levels = st.number_input("BUN Levels (mg/dL)", min_value=5, max_value=100, value=20)
gfr = st.number_input("Glomerular Filtration Rate (GFR)", min_value=10, max_value=120, value=90)
protein_in_urine = st.selectbox("Protein in Urine", [0, 1, 2, 3, 4, 5])
sodium = st.number_input("Serum Sodium (mmol/L)", min_value=100, max_value=200, value=140)
cholesterol_total = st.number_input("Total Cholesterol (mg/dL)", min_value=100, max_value=300, value=180)
cholesterol_hdl = st.number_input("HDL Cholesterol (mg/dL)", min_value=20, max_value=100, value=50)
ace_inhibitors = st.selectbox("Taking ACE Inhibitors?", ["No", "Yes"])
nsaids_use = st.selectbox("Frequent NSAIDs Use?", ["No", "Yes"])
antidiabetic_meds = st.selectbox("Taking Antidiabetic Medications?", ["No", "Yes"])
occupational_exposure = st.selectbox("Occupational Exposure to Chemicals?", ["No", "Yes"])

# Convert categorical inputs to numerical values
ethnicity_dict = {"Group A": 0, "Group B": 1, "Group C": 2}
physical_activity_dict = {"Low": 0, "Moderate": 1, "High": 2}

ethnicity = ethnicity_dict[ethnicity]
physical_activity = physical_activity_dict[physical_activity]
ace_inhibitors = 1 if ace_inhibitors == "Yes" else 0
nsaids_use = 1 if nsaids_use == "Yes" else 0
antidiabetic_meds = 1 if antidiabetic_meds == "Yes" else 0
occupational_exposure = 1 if occupational_exposure == "Yes" else 0

# Prediction button
if st.button("Predict"):
    features = [
        ethnicity, physical_activity, systolic_bp, fasting_blood_sugar, serum_creatinine,
        bun_levels, gfr, protein_in_urine, sodium, cholesterol_total, cholesterol_hdl,
        ace_inhibitors, nsaids_use, antidiabetic_meds, occupational_exposure
    ]
    
    result, probability = predict_ckd(features)

    st.subheader(f"Prediction: {result}")
    st.write(f"Confidence: {probability:.2f}%")

    if result == "Positive":
        st.error("High risk of CKD. Please consult a doctor.")
    else:
        st.success("Low risk of CKD. Maintain a healthy lifestyle!")
