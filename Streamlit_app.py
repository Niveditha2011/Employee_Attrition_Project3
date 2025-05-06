# import streamlit as st
# import pandas as pd
# import pickle

# # Load the trained Random Forest model
# model_path = 'Employee_attrition_trained_model.sav'
# model = pickle.load(open(model_path, 'rb'))

# # Define all the required input features (same as training)
# feature_columns = [
#     'Age', 'DailyRate', 'DistanceFromHome', 'Education', 'EnvironmentSatisfaction',
#     'Gender', 'HourlyRate', 'JobInvolvement', 'JobLevel', 'JobSatisfaction',
#     'MonthlyIncome', 'MonthlyRate', 'NumCompaniesWorked', 'OverTime',
#     'PercentSalaryHike', 'PerformanceRating', 'RelationshipSatisfaction', 'StockOptionLevel',
#     'TotalWorkingYears', 'TrainingTimesLastYear', 'WorkLifeBalance', 'YearsAtCompany',
#     'YearsInCurrentRole', 'YearsSinceLastPromotion', 'YearsWithCurrManager',
#     'Non-Travel', 'Travel_Frequently', 'Travel_Rarely',
#     'Department_Human Resources', 'Department_Research & Development', 'Department_Sales',
#     'Education_Human Resources', 'Education_Life Sciences', 'Education_Marketing',
#     'Education_Medical', 'Education_Other', 'Education_Technical Degree',
#     'Role_Healthcare Representative', 'Role_Human Resources', 'Role_Laboratory Technician',
#     'Role_Manager', 'Role_Manufacturing Director', 'Role_Research Director',
#     'Role_Research Scientist', 'Role_Sales Executive', 'Role_Sales Representative',
#     'MaritalStatus_Divorced', 'MaritalStatus_Married', 'MaritalStatus_Single'
# ]

# # Page configuration
# st.set_page_config(page_title="Employee Attrition Predictor", layout="wide")
# st.title("🔍 Employee Attrition Prediction App")

# st.markdown("""
# Enter employee details below. The model will predict the likelihood of attrition (i.e., whether the employee may leave the company).
# """)

# # Input widgets
# age = st.slider("Age", 10, 60, 30)
# dailyrate = st.slider("Daily Rate", 100, 1500, 500)
# distance = st.slider("Distance From Home (km)", 1, 30, 5)
# education = st.selectbox("Education Level", [1, 2, 3, 4, 5])
# env_satisfaction = st.slider("Environment Satisfaction (1–4)", 1, 4, 3)
# gender = st.selectbox("Gender", ["Male", "Female"])
# hourlyrate = st.slider("Hourly Rate", 30, 100, 60)
# job_involvement = st.slider("Job Involvement (1–4)", 1, 4, 3)
# job_level = st.slider("Job Level", 1, 5, 2)
# job_satisfaction = st.slider("Job Satisfaction (1–4)", 1, 4, 3)
# monthly_income = st.slider("Monthly Income", 1000, 20000, 5000)
# monthly_rate = st.slider("Monthly Rate", 1000, 25000, 10000)
# num_companies = st.slider("Number of Companies Worked", 0, 10, 1)
# overtime = st.selectbox("OverTime", ["Yes", "No"])
# percent_hike = st.slider("Percent Salary Hike", 0, 100, 15)
# performance_rating = st.selectbox("Performance Rating", [1, 2, 3, 4])
# relationship_satisfaction = st.slider("Relationship Satisfaction (1–4)", 1, 4, 3)
# stock_option = st.selectbox("Stock Option Level", [0, 1, 2, 3])
# total_working_years = st.slider("Total Working Years", 0, 40, 10)
# training_times = st.slider("Training Times Last Year", 0, 10, 3)
# work_life_balance = st.slider("Work-Life Balance (1–4)", 1, 4, 3)
# years_at_company = st.slider("Years At Company", 0, 40, 5)
# years_in_role = st.slider("Years In Current Role", 0, 20, 3)
# years_since_promo = st.slider("Years Since Last Promotion", 0, 15, 2)
# years_with_mgr = st.slider("Years With Current Manager", 0, 15, 2)
# travel = st.selectbox("Business Travel", ["Non-Travel", "Travel_Frequently", "Travel_Rarely"])
# department = st.selectbox("Department", ["Human Resources", "Research & Development", "Sales"])
# ed_field = st.selectbox("Education Field", [
#     "Human Resources", "Life Sciences", "Marketing",
#     "Medical", "Other", "Technical Degree"])
# job_role = st.selectbox("Job Role", [
#     "Healthcare Representative", "Human Resources", "Laboratory Technician",
#     "Manager", "Manufacturing Director", "Research Director",
#     "Research Scientist", "Sales Executive", "Sales Representative"])
# marital_status = st.selectbox("Marital Status", ["Divorced", "Married", "Single"])

# # Binary and one-hot encodings
# gender_val = 1 if gender == "Male" else 0
# overtime_val = 1 if overtime == "Yes" else 0
# travel_opts = ["Non-Travel", "Travel_Frequently", "Travel_Rarely"]
# travel_encoded = {t: int(t == travel) for t in travel_opts}
# department_opts = ["Department_Human Resources", "Department_Research & Development", "Department_Sales"]
# department_encoded = {col: int(col.split("_")[1] == department) for col in department_opts}
# ed_field_opts = [
#     "Education_Human Resources", "Education_Life Sciences", "Education_Marketing",
#     "Education_Medical", "Education_Other", "Education_Technical Degree"]
# ed_field_encoded = {col: int(col.split("_")[1] == ed_field) for col in ed_field_opts}
# role_opts = [
#     "Role_Healthcare Representative", "Role_Human Resources", "Role_Laboratory Technician",
#     "Role_Manager", "Role_Manufacturing Director", "Role_Research Director",
#     "Role_Research Scientist", "Role_Sales Executive", "Role_Sales Representative"]
# role_encoded = {col: int(col.split("_")[1] == job_role) for col in role_opts}
# marital_opts = ["MaritalStatus_Divorced", "MaritalStatus_Married", "MaritalStatus_Single"]
# marital_encoded = {col: int(col.split("_")[1] == marital_status) for col in marital_opts}

# # Construct full input dictionary
# input_dict = {
#     'Age': age, 'DailyRate': dailyrate, 'DistanceFromHome': distance,
#     'Education': education, 'EnvironmentSatisfaction': env_satisfaction,
#     'Gender': gender_val, 'HourlyRate': hourlyrate, 'JobInvolvement': job_involvement,
#     'JobLevel': job_level, 'JobSatisfaction': job_satisfaction,
#     'MonthlyIncome': monthly_income, 'MonthlyRate': monthly_rate,
#     'NumCompaniesWorked': num_companies, 'OverTime': overtime_val,
#     'PercentSalaryHike': percent_hike, 'PerformanceRating': performance_rating,
#     'RelationshipSatisfaction': relationship_satisfaction, 'StockOptionLevel': stock_option,
#     'TotalWorkingYears': total_working_years, 'TrainingTimesLastYear': training_times,
#     'WorkLifeBalance': work_life_balance, 'YearsAtCompany': years_at_company,
#     'YearsInCurrentRole': years_in_role, 'YearsSinceLastPromotion': years_since_promo,
#     'YearsWithCurrManager': years_with_mgr,
#     **travel_encoded, **department_encoded, **ed_field_encoded,
#     **role_encoded, **marital_encoded
# }

# # Final DataFrame for prediction
# input_df = pd.DataFrame([input_dict])[feature_columns]

# if st.button("Predict Attrition"):
#     probability = model.predict_proba(input_df)[0][1]
#     threshold = 0.4  # custom threshold
#     predicted_label = 1 if probability > threshold else 0

#     st.subheader("Prediction Result")
#     st.write(f"🧠 Predicted Attrition: {'Yes' if predicted_label == 1 else 'No'}")
#     st.write(f"🔢 Probability of Leaving: {probability:.2f}")


import streamlit as st
import pandas as pd
import pickle

# Load trained model
model = pickle.load(open('Employee_attrition_trained_model.sav', 'rb'))

# Feature columns used in the model
feature_columns = [
    'Age', 'DailyRate', 'DistanceFromHome', 'Education', 'EnvironmentSatisfaction',
    'Gender', 'HourlyRate', 'JobInvolvement', 'JobLevel', 'JobSatisfaction',
    'MonthlyIncome', 'MonthlyRate', 'NumCompaniesWorked', 'OverTime',
    'PercentSalaryHike', 'PerformanceRating', 'RelationshipSatisfaction', 'StockOptionLevel',
    'TotalWorkingYears', 'TrainingTimesLastYear', 'WorkLifeBalance', 'YearsAtCompany',
    'YearsInCurrentRole', 'YearsSinceLastPromotion', 'YearsWithCurrManager',
    'Non-Travel', 'Travel_Frequently', 'Travel_Rarely',
    'Department_Human Resources', 'Department_Research & Development', 'Department_Sales',
    'Education_Human Resources', 'Education_Life Sciences', 'Education_Marketing',
    'Education_Medical', 'Education_Other', 'Education_Technical Degree',
    'Role_Healthcare Representative', 'Role_Human Resources', 'Role_Laboratory Technician',
    'Role_Manager', 'Role_Manufacturing Director', 'Role_Research Director',
    'Role_Research Scientist', 'Role_Sales Executive', 'Role_Sales Representative',
    'MaritalStatus_Divorced', 'MaritalStatus_Married', 'MaritalStatus_Single'
]

# Page setup
st.set_page_config(page_title="Employee Attrition Predictor", layout="wide")
st.title("🔍 Employee Attrition Prediction App")
st.markdown("""
Enter employee details below. The model will predict the likelihood of attrition (i.e., whether the employee may leave the company).
""")

# Input fields
age = st.slider("Age", 10, 60, 30)
dailyrate = st.slider("Daily Rate", 100, 1500, 500)
distance = st.slider("Distance From Home (km)", 1, 30, 5)
education = st.selectbox("Education Level", [1, 2, 3, 4, 5])
env_satisfaction = st.slider("Environment Satisfaction (1–4)", 1, 4, 3)
gender = st.selectbox("Gender", ["Male", "Female"])
hourlyrate = st.slider("Hourly Rate", 30, 100, 60)
job_involvement = st.slider("Job Involvement (1–4)", 1, 4, 3)
job_level = st.slider("Job Level", 1, 5, 2)
job_satisfaction = st.slider("Job Satisfaction (1–4)", 1, 4, 3)
monthly_income = st.slider("Monthly Income", 1000, 20000, 5000)
monthly_rate = st.slider("Monthly Rate", 1000, 25000, 10000)
num_companies = st.slider("Number of Companies Worked", 0, 10, 1)
overtime = st.selectbox("OverTime", ["Yes", "No"])
percent_hike = st.slider("Percent Salary Hike", 0, 100, 15)
performance_rating = st.selectbox("Performance Rating", [1, 2, 3, 4])
relationship_satisfaction = st.slider("Relationship Satisfaction (1–4)", 1, 4, 3)
stock_option = st.selectbox("Stock Option Level", [0, 1, 2, 3])
total_working_years = st.slider("Total Working Years", 0, 40, 10)
training_times = st.slider("Training Times Last Year", 0, 10, 3)
work_life_balance = st.slider("Work-Life Balance (1–4)", 1, 4, 3)
years_at_company = st.slider("Years At Company", 0, 40, 5)
years_in_role = st.slider("Years In Current Role", 0, 20, 3)
years_since_promo = st.slider("Years Since Last Promotion", 0, 15, 2)
years_with_mgr = st.slider("Years With Current Manager", 0, 15, 2)

travel = st.selectbox("Business Travel", ["Non-Travel", "Travel_Frequently", "Travel_Rarely"])
department = st.selectbox("Department", ["Human Resources", "Research & Development", "Sales"])
ed_field = st.selectbox("Education Field", [
    "Human Resources", "Life Sciences", "Marketing",
    "Medical", "Other", "Technical Degree"])
job_role = st.selectbox("Job Role", [
    "Healthcare Representative", "Human Resources", "Laboratory Technician",
    "Manager", "Manufacturing Director", "Research Director",
    "Research Scientist", "Sales Executive", "Sales Representative"])
marital_status = st.selectbox("Marital Status", ["Divorced", "Married", "Single"])

# Binary and one-hot encoding
gender_val = 1 if gender == "Male" else 0
overtime_val = 1 if overtime == "Yes" else 0

travel_encoded = {t: int(t == travel) for t in ["Non-Travel", "Travel_Frequently", "Travel_Rarely"]}
department_encoded = {col: int(col.split("_", 1)[1] == department) for col in [
    "Department_Human Resources", "Department_Research & Development", "Department_Sales"]}
ed_field_encoded = {col: int(col.split("_", 1)[1] == ed_field) for col in [
    "Education_Human Resources", "Education_Life Sciences", "Education_Marketing",
    "Education_Medical", "Education_Other", "Education_Technical Degree"]}
role_encoded = {col: int(col.split("_", 1)[1] == job_role) for col in [
    "Role_Healthcare Representative", "Role_Human Resources", "Role_Laboratory Technician",
    "Role_Manager", "Role_Manufacturing Director", "Role_Research Director",
    "Role_Research Scientist", "Role_Sales Executive", "Role_Sales Representative"]}
marital_encoded = {col: int(col.split("_", 1)[1] == marital_status) for col in [
    "MaritalStatus_Divorced", "MaritalStatus_Married", "MaritalStatus_Single"]}

# Combine all inputs
input_dict = {
    'Age': age, 'DailyRate': dailyrate, 'DistanceFromHome': distance,
    'Education': education, 'EnvironmentSatisfaction': env_satisfaction,
    'Gender': gender_val, 'HourlyRate': hourlyrate, 'JobInvolvement': job_involvement,
    'JobLevel': job_level, 'JobSatisfaction': job_satisfaction,
    'MonthlyIncome': monthly_income, 'MonthlyRate': monthly_rate,
    'NumCompaniesWorked': num_companies, 'OverTime': overtime_val,
    'PercentSalaryHike': percent_hike, 'PerformanceRating': performance_rating,
    'RelationshipSatisfaction': relationship_satisfaction, 'StockOptionLevel': stock_option,
    'TotalWorkingYears': total_working_years, 'TrainingTimesLastYear': training_times,
    'WorkLifeBalance': work_life_balance, 'YearsAtCompany': years_at_company,
    'YearsInCurrentRole': years_in_role, 'YearsSinceLastPromotion': years_since_promo,
    'YearsWithCurrManager': years_with_mgr,
    **travel_encoded, **department_encoded, **ed_field_encoded,
    **role_encoded, **marital_encoded
}

# Predict
input_df = pd.DataFrame([input_dict])[feature_columns]

if st.button("Predict Attrition"):
    probability = model.predict_proba(input_df)[0][1]
    threshold = 0.4
    predicted_label = 1 if probability > threshold else 0

    # Interpret risk level
    if probability > 0.7:
        risk = "High"
    elif probability > 0.4:
        risk = "Moderate"
    else:
        risk = "Low"

    # Show prediction
    st.subheader("🧠 Prediction Result")
    st.write(f"**Predicted Attrition:** {'Yes' if predicted_label == 1 else 'No'}")
    st.write(f"**Probability of Leaving:** {probability:.2f}")
    st.write(f"**Attrition Risk Level:** {risk}")

    # Add model details
    st.markdown("##### ℹ️ Model Info")
    st.markdown("- Model: Random Forest Classifier")
    st.markdown(f"- Classification Threshold: `{threshold}`")

    # Optional: Download CSV
    output_csv = input_df.copy()
    output_csv["Predicted Attrition"] = "Yes" if predicted_label == 1 else "No"
    output_csv["Attrition Probability"] = probability
    st.download_button("📥 Download Prediction as CSV", output_csv.to_csv(index=False), "prediction.csv")
