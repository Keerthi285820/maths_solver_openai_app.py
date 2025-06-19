import streamlit as st
from openai import OpenAI  # ✅ CORRECT for v1.0.0+

# Load API key from Streamlit secrets
client = OpenAI(api_key=st.secrets["openai_api_key"])

# UI
st.set_page_config(page_title="Math Solver", page_icon="🧠")
st.title("📐 Universal Math Solver")
st.markdown("Ask me any **math or statistics problem**, and I’ll give you step-by-step solutions!")

# Input
question = st.text_area("🧠 Your question:")

# Solve button
if st.button("Solve"):
    if not question.strip():
        st.warning("⚠️ Please type your question.")
    else:
        with st.spinner("Solving..."):
            try:
                response = client.chat.completions.create(
                    model="gpt-4",
                    messages=[
                        {"role": "system", "content": "You are a helpful math tutor. Give step-by-step solutions using LaTeX where needed."},
                        {"role": "user", "content": question}
                    ],
                    temperature=0.3,
                )
                answer = response.choices[0].message.content
                st.markdown("### ✅ Solution:")
                st.markdown(answer)
            except Exception as e:
                st.error(f"❌ Error: {e}")
