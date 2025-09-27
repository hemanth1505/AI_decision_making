import streamlit as st
from ai_model import get_ai_decision
from rl_model import ReinforcementLearningAgent
from xai_model import explain_decision
import pandas as pd

# Load sample logs
df = pd.read_csv("logs.csv")

# Initialize RL Agent
rl_agent = ReinforcementLearningAgent()

# Streamlit UI
st.title("🛡️AI-Decision making")

# Show sample logs
st.subheader("🔍 Security Alerts")
st.dataframe(df)

# User Input
st.subheader("💡Enter for AI Decision.")
user_input = st.text_input("Type your alert (e.g., 'Brute-force attack detected'):")

if st.button("Analyze"):
    decision = get_ai_decision(user_input)
    explanation = explain_decision(decision)

    # RL Agent chooses action
    action = rl_agent.choose_action(user_input)

    st.success(f"✅ AI Decision: {decision}")
    st.info(f"📌 Explanation: {explanation}")
    st.warning(f"⚠️ Recommended Action: {['Ignore', 'Take Immediate Action'][action]}")
