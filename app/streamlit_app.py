import streamlit as st
from calculator import Calculator
import subprocess

# Create a Calculator instance
calc = Calculator()

# Streamlit app UI
st.title("Calculator and Test Runner")

# Input fields for numbers
num1 = st.number_input("Number 1", value=0)
num2 = st.number_input("Number 2", value=0)

# Dropdown for selecting operation
operation = st.selectbox("Choose operation", ["Add", "Subtract", "Multiply", "Divide"])

# Submit button
if st.button("Calculate"):
    # Perform operation based on user selection
    if operation == "Add":
        result = calc.add(num1, num2)
    elif operation == "Subtract":
        result = calc.subtract(num1, num2)
    elif operation == "Multiply":
        result = calc.multiply(num1, num2)
    elif operation == "Divide":
        try:
            result = calc.divide(num1, num2)
        except ValueError as e:
            result = f"Error: {e}"

    # Show result
    st.subheader(f"Result: {result}")

    # Run tests (trigger background test run)
    with st.spinner("Running tests..."):
        try:
            # Trigger the pytest run in the background
            result = subprocess.run(['pytest', '--maxfail=1', '--disable-warnings', '--tb=short'], capture_output=True, text=True)
            
            # Check if tests passed or failed
            if result.returncode == 0:
                st.success("🟢 Tests Passed. Build Successful!")
            else:
                st.error("🔴 Tests Failed. Build Failed!")

        except Exception as e:
            st.error(f"Error: {str(e)}")

