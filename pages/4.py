import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Example data
data = {
    "Date": ["16 Mar, 2019", "16 Mar, 2019", "16 Mar, 2019", "16 Mar, 2019", "15 Mar, 2019"],
    "Name": ["Elvis Presley", "Paul McCartney", "Tom Scholz", "Michael Jackson", "Bruce Springsteen"],
    "Ship To": ["Tupelo, MS", "London, UK", "Boston, MA", "Gary, IN", "Long Branch, NJ"],
    "Payment Method": ["VISA **** 3719", "VISA **** 2574", "MC **** 1253", "AMEX **** 2000", "VISA **** 5919"],
    "Sale Amount": [312.44, 586.99, 100.81, 654.39, 212.79]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Title
st.title("Enhanced Streamlit App")

# Control Panel with Sections
st.sidebar.header("Control Panel")

# Prior Belief Section
st.sidebar.subheader("Prior Belief about the Click Rate")
prior_sessions = st.sidebar.number_input("Number of prior sessions", value=500, min_value=1)
prior_click_rate = st.sidebar.slider("Prior click rate", min_value=0.0, max_value=1.0, value=0.05)

# Decision Criteria Section
st.sidebar.subheader("Decision Criteria")
worst_click_rate = st.sidebar.slider("Worst-case click rate threshold", min_value=0.0, max_value=1.0, value=0.1)
max_acceptable_prob = st.sidebar.slider("Max acceptable worst-case probability", min_value=0.0, max_value=1.0, value=0.05)

# Display Editable Data Table
st.subheader("Recent Orders")
edited_df = st.data_editor(df)

# Display the edited DataFrame
st.write("Edited DataFrame:")
st.write(edited_df)

# Dummy graph for demonstration
fig, ax = plt.subplots()
ax.plot(np.random.randn(100).cumsum())
ax.set_title("Sample Graph with Increased Font Size", fontsize=16)
ax.set_xlabel("X-axis Label", fontsize=14)
ax.set_ylabel("Y-axis Label", fontsize=14)
st.pyplot(fig)

# Final Decision Highlight
st.subheader("Results and Decision")
st.markdown("""
<div style="background-color: #f0f0f0; padding: 10px; border-radius: 5px;">
    <strong>Final decision:</strong> <span style="color: red;">NO GO</span>
</div>
""", unsafe_allow_html=True)

# Feedback Mechanism
st.sidebar.header("Feedback")
feedback = st.sidebar.text_area("Your feedback or suggestions")
if st.sidebar.button("Submit"):
    st.sidebar.write("Thank you for your feedback!")