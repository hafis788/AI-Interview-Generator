import streamlit as st
import google.generativeai as genai

# Configure Gemini API key
genai.configure(api_key="AIzaSyAsVZ_B6J-ONViZkrnIpOY05_57RYN-55s")

# Load the correct model
model = genai.GenerativeModel("gemini-1.5-flash")

# Title and input
st.title("💡 AI Interview Question Generator")
st.write("Enter a job role or skills, and AI will generate questions for you!")

job_role = st.text_input("Enter job role or skills:")
if st.button("Generate Questions"):
    if job_role:
        with st.spinner("Generating questions..."):
            try:
                response = model.gcleaenerate_content(f"Generate 5 interview questions for a {job_role}")
                st.markdown("### 📋 Generated Interview Questions:")
                st.write(response.text)
            except Exception as e:
                st.error(f"❌ Error: {e}")
    else:
        st.warning("Please enter a job role or skills.")
