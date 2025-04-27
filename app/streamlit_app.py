import streamlit as st
from calculator import Calculator
import subprocess
import time
import os

# Streamlit Page Config
st.set_page_config(page_title="Jenkins-AutoTesting", page_icon="🛠️", layout="centered")

# UI Decorations
st.title("🔧 Jenkins-AutoTesting Calculator")
st.markdown("## Enter your numbers and select an operation:")
st.divider()

# Input Fields
number1 = st.number_input("Enter Number 1:", format="%.2f")
number2 = st.number_input("Enter Number 2:", format="%.2f")

operation = st.selectbox("Select Operation:", ["Add", "Subtract", "Multiply", "Divide"])

if st.button("🚀 Submit and Run Tests"):
    with st.spinner('Calculating... and Running Tests 🔄'):
        calc = Calculator()
        
        # Perform the selected operation
        try:
            if operation == "Add":
                result = calc.add(number1, number2)
            elif operation == "Subtract":
                result = calc.subtract(number1, number2)
            elif operation == "Multiply":
                result = calc.multiply(number1, number2)
            elif operation == "Divide":
                result = calc.divide(number1, number2)
            
            st.success(f"✅ Result: **{result}**")
        
        except Exception as e:
            st.error(f"❌ Error: {str(e)}")
            result = None

        # --- Run Pytest locally ---
        time.sleep(1)
        with open('pytest_output.txt', 'w') as f:
            subprocess.run(['pytest', '--tb=short', '--maxfail=1'], stdout=f, stderr=subprocess.STDOUT)
        
        with open('pytest_output.txt', 'r') as f:
            pytest_result = f.read()

        # --- Show Build Status based on tests ---
        if "failed" in pytest_result.lower():
            st.error("🔴 **Tests Failed. Build Failed!**")
            st.balloons()
        else:
            st.success("🟢 **Tests Passed. Build Successful!**")
            st.balloons()

        st.divider()

        with st.expander("🔎 See Detailed Test Logs"):
            st.code(pytest_result)
