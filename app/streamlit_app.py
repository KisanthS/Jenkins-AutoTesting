import streamlit as st
import subprocess
from app.calculator import Calculator

# Set up page configuration
st.set_page_config(page_title="Jenkins AutoTesting UI 🚀", page_icon="🛠️", layout="centered")

# Custom CSS for more stylish look
st.markdown("""
    <style>
        .main {
            background-color: #F5F7FA;
            padding: 20px;
            border-radius: 12px;
        }
        .stButton>button {
            background-color: #4CAF50;
            color: white;
            border: none;
            padding: 10px 24px;
            text-align: center;
            text-decoration: none;
            display: inline-block;
            font-size: 18px;
            margin: 4px 2px;
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
        }
        .error-box {
            background-color: #f8d7da;
            color: #721c24;
            padding: 15px;
            border-radius: 10px;
            margin-top: 20px;
        }
    </style>
""", unsafe_allow_html=True)

st.title("🛠️ Jenkins AutoTesting Web UI")
st.caption("A Smart Way to Test Your Builds Instantly!")

with st.container():
    st.subheader("✨ Provide Inputs")
    number1 = st.number_input("Enter Number 1", format="%.2f")
    number2 = st.number_input("Enter Number 2", format="%.2f")
    operation = st.selectbox("Choose an Operation", ["Add ➕", "Subtract ➖", "Multiply ✖️", "Divide ➗"])

submit_btn = st.button("🚀 Submit and Run Tests")

if submit_btn:
    calc = Calculator()

    try:
        if operation.startswith("Add"):
            result = calc.add(number1, number2)
        elif operation.startswith("Subtract"):
            result = calc.subtract(number1, number2)
        elif operation.startswith("Multiply"):
            result = calc.multiply(number1, number2)
        elif operation.startswith("Divide"):
            result = calc.divide(number1, number2)
        
        st.success(f"✅ **Result of {operation}: {result}**")

        # Spinner while running tests
        with st.spinner("🔍 Running automated tests... please wait"):
            test_result = subprocess.run(["pytest", "--maxfail=1", "--disable-warnings"], capture_output=True, text=True)

        if test_result.returncode == 0:
            st.markdown('<div class="success-box">🎉 All Tests Passed! Build Success! 🎯</div>', unsafe_allow_html=True)
            st.balloons()
        else:
            st.markdown('<div class="error-box">❌ Some Tests Failed! Build Failed! 🔥</div>', unsafe_allow_html=True)
            st.code(test_result.stdout + test_result.stderr, language='bash')

    except Exception as e:
        st.markdown('<div class="error-box">🚨 Error occurred: {}</div>'.format(e), unsafe_allow_html=True)
