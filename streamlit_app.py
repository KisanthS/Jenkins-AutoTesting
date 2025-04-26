import streamlit as st
import time
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
        footer {
            visibility: hidden;
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
    submitted = st.form_submit_button("Trigger Build 🚀")  # updated button text

if submitted:
    calc = Calculator()

    start_time = time.time()  # Start timer

    try:
        if operation == "Add":
            result = calc.add(a, b)
        elif operation == "Subtract":
            result = calc.subtract(a, b)
        elif operation == "Multiply":
            result = calc.multiply(a, b)
        elif operation == "Divide":
            result = calc.divide(a, b)

        elapsed_time = time.time() - start_time  # End timer

        # If calculation successful
        st.success(f"✅ Build Success!")
        st.write(f"Result of **{operation.lower()}**: **{result}**")
        st.write(f"⏱️ Build completed in **{elapsed_time:.2f} seconds**.")

        # Confetti animation
        st.snow()  # ❄️ snow looks a bit like confetti on Streamlit!

    except Exception as e:
        elapsed_time = time.time() - start_time  # End timer if error
        # If any error occurs (like divide by zero)
        st.error(f"❌ Build Failed!")
        st.write(f"Error: {str(e)}")
        st.write(f"⏱️ Build failed in **{elapsed_time:.2f} seconds**.")
