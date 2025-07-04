import streamlit as st
import pandas as pd

# Load your data
df = pd.read_csv("data.csv")

st.title("📘 Python Course - Student Tracker")

# Display the table
st.dataframe(df)

# ➕ Add a Download button
csv = df.to_csv(index=False).encode('utf-8')

st.download_button(
    label="📥 Download CSV",
    data=csv,
    file_name='student_tracker.csv',
    mime='text/csv'
)
