import streamlit as st
import pandas as pd

st.set_page_config(page_title="Python Course Dashboard", layout="centered")

st.title("📘 Python Course - Student Tracker")

# Load CSV
df = pd.read_csv("data.csv")

# Full data
st.subheader("📋 Full Student Data")
st.dataframe(df)

# Passed filter
st.subheader("🎓 Passed Students")
passed = df[df["Status"] == "Passed"]
st.dataframe(passed)

# OOP Completed filter
st.subheader("🧠 Students Who Completed OOP")
oop = df[df["Completed OOP"] == "Yes"]
st.dataframe(oop)

# Score Chart
st.subheader("📈 Score Chart")
st.bar_chart(df.set_index("Student Name")["Score (%)"])
