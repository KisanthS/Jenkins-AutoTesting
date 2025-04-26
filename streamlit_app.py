import streamlit as st
from app.calculator import Calculator

# Set page config
st.set_page_config(page_title="Jenkins AutoTesting", page_icon="🔍", layout="centered")

# Custom CSS for stylish touch
st.markdown("""
    <style>
        .main {
            background-color: #f5f7fa;
            padding: 20px;
            border-radius: 10px;
        }
        .title {
            text-align: center;
            font-size: 2.5em;
            font-weight: bold;
            color: #2c3e50;
            margin-bottom: 20px;
        }
        .stButton > button {
            background-color: #2c3e50;
            color: white;
            padding: 0.75em 1.5em;
            font-size: 1em;
            border-radius: 8px;
        }
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown('<div class="title">🔍 Jenkins AutoTesting Web App</div>', unsafe_allow_html=True)

# Input form
with st.form("calculator_form"):
    a = st.number_input("Enter first number (a)", step=1.0)
    b = st.number_input("Enter second number (b)", step=1.0)
    operation = st.selectbox("Select operation", ("Add", "Subtract", "Multiply", "Divide"))
    submitted = st.form_submit_button("Run Build")

if submitted:
    calc = Calculator()
    try:
        if operation == "Add":
            result = calc.add(a, b)
        elif operation == "Subtract":
            result = calc.subtract(a, b)
        elif operation == "Multiply":
            result = calc.multiply(a, b)
        elif operation == "Divide":
            result = calc.divide(a, b)

        # If calculation successful
        st.success(f"✅ Build Success!\n\nResult of {operation.lower()} is: **{result}**")
        st.balloons()

    except Exception as e:
        # If any error occurs (like divide by zero)
        st.error(f"❌ Build Failed!\n\nError: {str(e)}")
