import streamlit as st
import time
from app.calculator import Calculator

# Set page configuration
st.set_page_config(page_title="🚀 Jenkins AutoTesting WebApp", page_icon="🔍", layout="centered")

# Custom CSS for polished design
st.markdown("""
    <style>
        .main {
            background-color: #f7f9fc;
            padding: 20px;
            border-radius: 12px;
        }
        .title {
            text-align: center;
            font-size: 2.8em;
            font-weight: bold;
            color: #2c3e50;
            margin-bottom: 20px;
        }
        .stButton>button {
            background-color: #2c3e50;
            color: white;
            padding: 10px 24px;
            font-size: 1.1em;
            border-radius: 10px;
            transition: background-color 0.3s;
        }
        .stButton>button:hover {
            background-color: #1a252f;
        }
        footer {
            visibility: hidden;
        }
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown('<div class="title">🚀 Jenkins AutoTesting WebApp</div>', unsafe_allow_html=True)

# Main Form
with st.form("calculator_form"):
    a = st.number_input("Enter first number (a)", step=1.0, format="%.2f")
    b = st.number_input("Enter second number (b)", step=1.0, format="%.2f")
    operation = st.selectbox("Select operation", ("Add", "Subtract", "Multiply", "Divide"))
    submitted = st.form_submit_button("Trigger Build 🚀")

if submitted:
    calc = Calculator()

    start_time = time.time()

    try:
        if operation == "Add":
            result = calc.add(a, b)
        elif operation == "Subtract":
            result = calc.subtract(a, b)
        elif operation == "Multiply":
            result = calc.multiply(a, b)
        elif operation == "Divide":
            result = calc.divide(a, b)

        elapsed_time = time.time() - start_time

        st.success("✅ Build Success!")
        st.metric(label=f"Result of {operation}", value=f"{result:.2f}")
        st.info(f"⏱️ Build completed in {elapsed_time:.2f} seconds.")

        st.balloons()  # celebration 🎈

    except Exception as e:
        elapsed_time = time.time() - start_time
        st.error("❌ Build Failed!")
        st.warning(f"Error: {str(e)}")
        st.info(f"⏱️ Build failed in {elapsed_time:.2f} seconds.")
