import streamlit as st
import subprocess
import pytest
import os
from calculator import Calculator

# Streamlit UI settings
st.set_page_config(page_title="Jenkins AutoTesting UI 🚀", page_icon="🛠️", layout="centered")

# Custom CSS to make UI beautiful
st.markdown("""
    <style>
    .main {
        background-color: #f0f2f6;
        padding: 20px;
        border-radius: 15px;
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        font-size: 18px;
        padding: 10px 24px;
        border: none;
        border-radius: 12px;
        transition-duration: 0.4s;
    }
    .stButton>button:hover {
        background-color: #45a049;
    }
    .success-box {
        background-color: #d4edda;
        color: #155724;
        padding: 15px;
        border-radius: 10px;
        margin-top: 20px;
        font-size: 18px;
    }
    .error-box {
        background-color: #f8d7da;
        color: #721c24;
        padding: 15px;
        border-radius: 10px;
        margin-top: 20px;
        font-size: 18px;
    }
    </style>
""", unsafe_allow_html=True)

# App Title
st.title("🛠️ Jenkins AutoTesting Webpage")
st.caption("✨ Trigger your builds and view results live!")

# Input Section
with st.container():
    st.subheader("🔢 Enter Inputs")
    number1 = st.number_input("Enter Number 1", format="%.2f")
    number2 = st.number_input("Enter Number 2", format="%.2f")
    operation = st.selectbox("Select Operation", ["Add ➕", "Subtract ➖", "Multiply ✖️", "Divide ➗"])

# Submit Button
if st.button("🚀 Submit"):
    calc = Calculator()

    try:
        # Perform Calculation
        if operation.startswith("Add"):
            result = calc.add(number1, number2)
        elif operation.startswith("Subtract"):
            result = calc.subtract(number1, number2)
        elif operation.startswith("Multiply"):
            result = calc.multiply(number1, number2)
        elif operation.startswith("Divide"):
            result = calc.divide(number1, number2)

        st.success(f"✅ Result of {operation}: {result}")

        # Run Tests
        with st.spinner("🔍 Running automated tests... Please wait!"):
            test_result = subprocess.run(["pytest", "--maxfail=1", "--disable-warnings"], capture_output=True, text=True)

        if test_result.returncode == 0:
            st.markdown('<div class="success-box">🎉 All Tests Passed! Build Success! 🎯</div>', unsafe_allow_html=True)
            st.balloons()
        else:
            st.markdown('<div class="error-box">❌ Some Tests Failed! Build Failed! 🔥</div>', unsafe_allow_html=True)
            st.code(test_result.stdout + test_result.stderr, language='bash')

    except Exception as e:
        st.markdown(f'<div class="error-box">🚨 Error occurred: {e}</div>', unsafe_allow_html=True)
