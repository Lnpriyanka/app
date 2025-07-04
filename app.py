import streamlit as st
import pandas as pd

st.title("🎓 My Python Course Tracker")

# Load CSV file from the repo
df = pd.read_csv("data.csv")

st.subheader("📋 Full Student Data")
st.dataframe(df)

# Filter: Passed Students
st.subheader("✅ Passed Students")
st.dataframe(df[df["Status"] == "Passed"])

# Filter: Completed OOP
st.subheader("🧠 Students Who Completed OOP")
st.dataframe(df[df["Completed OOP"] == "Yes"])

# Bar chart of scores
st.subheader("📊 Score Chart")
st.bar_chart(df.set_index("Student Name")["Score (%)"])
