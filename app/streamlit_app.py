import streamlit as st
import subprocess
from calculator import Calculator

# Streamlit UI settings
st.set_page_config(page_title="AutoTesting Dashboard", page_icon="🛠️", layout="centered")

# Custom CSS for better look
st.markdown("""
    <style>
        .main {
            background-color: #f5f7fa;
        }
        .stButton>button {
            color: white;
            background-color: #4CAF50;
            border-radius: 8px;
            height: 3em;
            width: 100%;
            font-size: 1.2em;
        }
        .stSelectbox>div>div {
            font-size: 1.1em;
        }
        .stNumberInput>div>div>input {
            font-size: 1.1em;
        }
        .stTextInput>div>div>input {
            font-size: 1.1em;
        }
    </style>
""", unsafe_allow_html=True)

# Title and Description
st.title("🛠️ Jenkins AutoTesting Dashboard")
st.markdown("<h4 style='color: #6c757d;'>Give input ➔ Get result ➔ Auto-run tests ➔ See Build Status!</h4>", unsafe_allow_html=True)
st.write("---")

# Input Section
st.header("🔢 Provide Inputs")
col1, col2 = st.columns(2)

with col1:
    number1 = st.number_input("Enter Number 1", format="%.2f", key="num1")
with col2:
    number2 = st.number_input("Enter Number 2", format="%.2f", key="num2")

operation = st.selectbox("➕ Choose an Operation", ["Add", "Subtract", "Multiply", "Divide"])

# Submit Button
submit_button = st.button("🚀 Submit and Run Tests")

if submit_button:
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

        st.success(f"✅ **Result of {operation}: {result}**")
        st.write("---")
        
        # Running Tests
        with st.spinner("🧪 Running automated tests... Please wait..."):
            test_result = subprocess.run(["pytest", "--maxfail=1", "--disable-warnings"], capture_output=True, text=True)
        
        if test_result.returncode == 0:
            st.success("🟢 **All tests passed! Build Success!** 🎉")
            st.balloons()
        else:
            st.error("🔴 **Some tests failed! Build Failed!** ❌")
            with st.expander("🔍 See Test Details"):
                st.code(test_result.stdout + test_result.stderr)
    
    except Exception as e:
        st.error(f"❌ **Error Occurred:** {e}")
