import streamlit as st
import subprocess
import pytest
import os
from app.calculator import Calculator

# Streamlit UI
st.set_page_config(page_title="Jenkins AutoTesting UI", page_icon="🛠️", layout="centered")

st.title("🛠️ Jenkins AutoTesting Webpage")
st.subheader("Enter your inputs and trigger the tests!")

number1 = st.number_input("Enter Number 1", format="%.2f")
number2 = st.number_input("Enter Number 2", format="%.2f")
operation = st.selectbox("Select Operation", ["Add", "Subtract", "Multiply", "Divide"])

if st.button("Submit"):
    calc = Calculator()

    try:
        if operation == "Add":
            result = calc.add(number1, number2)
        elif operation == "Subtract":
            result = calc.subtract(number1, number2)
        elif operation == "Multiply":
            result = calc.multiply(number1, number2)
        elif operation == "Divide":
            result = calc.divide(number1, number2)
        
        st.success(f"✅ Result of {operation}: {result}")
        
        # Run tests after calculation
        with st.spinner("Running automated tests..."):
            test_result = subprocess.run(["pytest", "--maxfail=1", "--disable-warnings"], capture_output=True, text=True)
        
        if test_result.returncode == 0:
            st.success("🟢 All tests passed! Build Success!")
            st.balloons()
        else:
            st.error("🔴 Some tests failed! Build Failed!")
            st.code(test_result.stdout + test_result.stderr)
    
    except Exception as e:
        st.error(f"❌ Error: {e}")
