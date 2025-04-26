import streamlit as st
import requests
import time

# ------------------------------
# CONFIGURE YOUR GITHUB DETAILS
# ------------------------------
GITHUB_TOKEN = "your-github-personal-access-token"
REPO_OWNER = "your-github-username"
REPO_NAME = "your-repo-name"

# ------------------------------
# Streamlit UI
# ------------------------------
st.set_page_config(page_title="GitHub Actions AutoTesting", page_icon="🛠️", layout="centered")

st.title("🧮 Calculator (GitHub Actions AutoTesting)")
st.write("Perform a calculation and trigger GitHub Action to run tests!")

a = st.number_input("Enter first number (a):", value=0)
b = st.number_input("Enter second number (b):", value=0)
operation = st.selectbox("Choose operation:", ["Add", "Subtract", "Multiply", "Divide"])

if st.button("Submit and Trigger Build"):
    st.info("Triggering GitHub Action... Please wait...")

    headers = {
        "Authorization": f"token {GITHUB_TOKEN}",
        "Accept": "application/vnd.github.v3+json"
    }

    payload = {
        "event_type": "trigger-tests",
        "client_payload": {
            "a": a,
            "b": b,
            "operation": operation.lower()
        }
    }

    # Trigger GitHub Action
    response = requests.post(
        f"https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/dispatches",
        json=payload,
        headers=headers
    )

    if response.status_code == 204:
        st.success("✅ GitHub Action triggered successfully!")
    else:
        st.error(f"❌ Failed to trigger GitHub Action. Status Code: {response.status_code}")
        st.stop()

    # Wait before checking workflow status
    time.sleep(5)

    # Poll GitHub Actions for workflow run status
    build_result = None
    for _ in range(10):  # Retry 10 times
        runs_response = requests.get(
            f"https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/actions/runs",
            headers=headers
        )

        if runs_response.status_code == 200:
            runs_data = runs_response.json()
            latest_run = runs_data["workflow_runs"][0]

            if latest_run["status"] == "completed":
                build_result = latest_run["conclusion"]
                break
            else:
                st.write("🔄 Build is still running...")
                time.sleep(5)
        else:
            st.error(f"❌ Failed to fetch workflow runs. Status Code: {runs_response.status_code}")
            st.stop()

    if build_result == "success":
        st.balloons()
        st.success("🟢 Build Success! All tests passed!")
    elif build_result == "failure":
        st.error("🔴 Build Failed! Check your test results.")
    else:
        st.warning("⚠️ Build status unknown. Please check GitHub manually.")
