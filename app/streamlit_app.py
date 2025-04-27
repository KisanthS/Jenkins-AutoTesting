import streamlit as st
import requests
import time
from calculator import Calculator

# --- Streamlit UI Settings ---
st.set_page_config(page_title="Jenkins AutoTesting", page_icon="⚙️", layout="centered")

# --- Title and Description ---
st.markdown("<h1 style='text-align: center; color: #4CAF50;'>🛠️ Calculator & AutoTest Runner 🚀</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Trigger GitHub Actions and see real-time build status!</p>", unsafe_allow_html=True)
st.markdown("---")

# --- Input Section ---
st.subheader("🔢 Input Your Values")
with st.container():
    col1, col2 = st.columns(2)
    with col1:
        num1 = st.number_input("Enter Number 1", value=0, step=1, format="%d")
    with col2:
        num2 = st.number_input("Enter Number 2", value=0, step=1, format="%d")

operation = st.selectbox("🔧 Choose Operation", ["Add", "Subtract", "Multiply", "Divide"])

st.markdown("---")

# --- Submit Button ---
submit_button = st.button("🚀 Run Calculation & Tests", use_container_width=True)

if submit_button:
    start_time = time.time()

    calc = Calculator()

    try:
        # Perform the chosen calculation
        if operation == "Add":
            result = calc.add(num1, num2)
        elif operation == "Subtract":
            result = calc.subtract(num1, num2)
        elif operation == "Multiply":
            result = calc.multiply(num1, num2)
        elif operation == "Divide":
            result = calc.divide(num1, num2)

        st.success(f"🎯 **Result:** `{result}`")

        # --- GitHub Info ---
        GITHUB_TOKEN = st.secrets["github"]["token"]
        REPO_OWNER = st.secrets["github"]["repo_owner"]
        REPO_NAME = st.secrets["github"]["repo_name"]
        WORKFLOW_FILE = st.secrets["github"]["workflow_file"]

        headers = {
            "Authorization": f"Bearer {GITHUB_TOKEN}",
            "Accept": "application/vnd.github+json"
        }

        # --- Trigger GitHub Action ---
        dispatch_url = f"https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/actions/workflows/{WORKFLOW_FILE}/dispatches"
        dispatch_payload = {"ref": "main"}
        dispatch_response = requests.post(dispatch_url, headers=headers, json=dispatch_payload)

        if dispatch_response.status_code == 204:
            st.success("✅ GitHub Action triggered successfully!")
        else:
            st.error(f"❌ Failed to trigger GitHub Action. Status: {dispatch_response.status_code}")
            st.stop()

        # --- Poll GitHub for Workflow Run Status ---
        st.info("⏳ Waiting for build to start...")

        time.sleep(5)  # Give GitHub a few seconds to start

        runs_url = f"https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/actions/runs"
        build_status_placeholder = st.empty()
        progress_bar = st.progress(0)

        build_completed = False
        progress = 0

        while not build_completed:
            runs_response = requests.get(runs_url, headers=headers)
            if runs_response.status_code == 200:
                runs_data = runs_response.json()
                latest_run = runs_data["workflow_runs"][0]

                status = latest_run["status"]  # queued, in_progress, completed
                conclusion = latest_run["conclusion"]  # success, failure, cancelled

                if status == "completed":
                    build_completed = True
                    total_time = time.time() - start_time  # ⏱️
                    minutes, seconds = divmod(int(total_time), 60)

                    if conclusion == "success":
                        build_status_placeholder.success(f"✅ Build Passed in {minutes}m {seconds}s! 🎉")
                    else:
                        build_status_placeholder.error(f"❌ Build Failed in {minutes}m {seconds}s ❗")
                    progress_bar.empty()
                else:
                    build_status_placeholder.info(f"🔄 Build {status.capitalize()}... Please wait")
                    progress = (progress + 10) % 100
                    progress_bar.progress(progress)

                time.sleep(5)
            else:
                build_status_placeholder.error("❌ Failed to fetch workflow runs.")
                st.stop()

    except Exception as e:
        st.error(f"Error: {e}")
        st.markdown("### 🔴 Tests Failed. Build Failed! ❌", unsafe_allow_html=True)
