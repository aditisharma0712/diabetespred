import pickle
import streamlit as st

model= pickle.load(open('model.sav', 'rb'))
def predict_diabetes(input_data):
    input_data = [input_data]
    prediction = model.predict(input_data)
    return prediction[0]

def main():
    st.title("Diabetes Prediction App")
    st.write("Enter the following details to predict diabetes:")

    pregnancies = st.number_input("Number of Pregnancies", min_value=0, max_value=20, value=0)
    glucose = st.number_input("Glucose Level", min_value=0, max_value=200, value=100)
    blood_pressure = st.number_input("Blood Pressure (mm Hg)", min_value=0, max_value=200, value=70)
    skin_thickness = st.number_input("Skin Thickness (mm)", min_value=0, max_value=100, value=20)
    insulin = st.number_input("Insulin Level", min_value=0, max_value=500, value=80)
    bmi = st.number_input("BMI", min_value=0.0, max_value=50.0, value=25.0)
    diabetes_pedigree_function = st.number_input("Diabetes Pedigree Function", min_value=0.0, max_value=2.5, value=0.5)
    age = st.number_input("Age", min_value=0, max_value=120, value=30)      

    if st.button("Predict"):
        input_data = [pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, diabetes_pedigree_function, age]
        prediction = predict_diabetes(input_data)
        if prediction == 1:
            st.success("The model predicts that you have diabetes.")
        else:
            st.success("The model predicts that you do not have diabetes.")


if __name__ == "__main__":
    main()