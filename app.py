import streamlit as st
from groq import Groq

# 1. Page Configuration (The Look)
st.set_page_config(page_title="Global Problem Solver", page_icon="🌍")
st.title("🚀 The Next-Gen AI Solver")
st.markdown("### Solving the issues other AIs can't.")

# 2. Sidebar for the Free Key
with st.sidebar:
    st.header("Configuration")
    st.write("To keep this free, we use the Groq API.")
    api_key = st.text_input("Enter your Free Groq API Key:", type="password")
    st.info("Get your free key at: https://console.groq.com/keys")

# 3. The AI Logic (The Brain)
def generate_ai_response(user_text, key):
    client = Groq(api_key=key)
    
    # SYSTEM PROMPT: This is what makes your AI better than others.
    # It tells the AI to be honest, factual, and logical.
    system_instructions = (
        "You are an Elite AI designed to fix the flaws of standard models. "
        "1. Never lie or hallucinate. If you don't know, say so. "
        "2. Be direct. No 'As an AI language model' fluff. "
        "3. Provide step-by-step solutions for complex issues."
    )
    
    completion = client.chat.completions.create(
        model="llama3-70b-8192", # Using one of the world's most powerful free-tier models
        messages=[
            {"role": "system", "content": system_instructions},
            {"role": "user", "content": user_text}
        ]
    )
    return completion.choices[0].message.content

# 4. The User Interface
user_input = st.text_area("Describe the problem or issue you want to solve:", 
                          placeholder="e.g., Why do other AIs give me wrong coding advice?")

if st.button("Generate Better Solution"):
    if not api_key:
        st.error("❌ Please paste your Free Groq API Key in the sidebar first!")
    elif not user_input:
        st.warning("⚠️ Please enter a problem to solve.")
    else:
        with st.spinner("Thinking differently..."):
            try:
                answer = generate_ai_response(user_input, api_key)
                st.success("✅ Solution Found!")
                st.markdown("---")
                st.write(answer)
            except Exception as e:
                st.error(f"Error: {e}")
