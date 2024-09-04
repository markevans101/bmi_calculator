import streamlit as st

# Title of the app
st.title("BMI Calculator")

# Instructions
st.write("Enter your height and weight to calculate your BMI.")

# Input fields
height_in_inches = st.number_input("Enter your height in inches (e.g., 70):", min_value=20.0, max_value=100.0, step=0.1)
weight_in_pounds = st.number_input("Enter your weight in pounds (e.g., 150):", min_value=1.0, max_value=500.0, step=0.1)

# Convert height and weight to metric units
height_in_meters = height_in_inches * 0.0254
weight_in_kg = weight_in_pounds * 0.453592

# Calculate BMI
if height_in_meters > 0:
    bmi = weight_in_kg / (height_in_meters ** 2)

    # Display the result
    st.write(f"Your BMI is: {bmi:.2f}")

    # Provide health feedback
    if bmi < 18.5:
        st.write("You are underweight.")
    elif 18.5 <= bmi < 24.9:
        st.write("You have a normal weight.")
    elif 25 <= bmi < 29.9:
        st.write("You are overweight.")
    else:
        st.write("You are in the obese range.")
