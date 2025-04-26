import streamlit as st
import os
import xml.etree.ElementTree as ET

st.set_page_config(page_title="Jenkins AutoTesting Dashboard", page_icon="🧪", layout="centered")

st.title("🧪 Jenkins Automated Testing Dashboard")
st.subheader("Automated Unit Testing with Jenkins, Pytest, and Streamlit")

st.markdown("---")

# Load Test Results
def parse_test_results(xml_file):
    try:
        tree = ET.parse(xml_file)
        root = tree.getroot()
        total_tests = int(root.attrib.get('tests', 0))
        failures = int(root.attrib.get('failures', 0))
        errors = int(root.attrib.get('errors', 0))
        skipped = int(root.attrib.get('skipped', 0))
        passed = total_tests - failures - errors - skipped
        return total_tests, passed, failures + errors, skipped
    except Exception as e:
        st.error(f"Error parsing test-results.xml: {e}")
        return 0, 0, 0, 0

# Display Test Stats
if os.path.exists('test-results.xml'):
    total_tests, passed_tests, failed_tests, skipped_tests = parse_test_results('test-results.xml')
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.metric("✅ Passed", passed_tests)
        st.metric("❌ Failed", failed_tests)
        
    with col2:
        st.metric("🔢 Total Tests", total_tests)
        st.metric("⏩ Skipped", skipped_tests)
        
    st.success("Latest test results loaded successfully!")

else:
    st.warning("⚠️ Test results not found. Please run tests first.")

st.markdown("---")

st.caption("🚀 Built by [YourName] | Powered by Jenkins + Streamlit + Pytest")

