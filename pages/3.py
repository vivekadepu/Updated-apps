import streamlit as st
import pandas as pd

# Initial data
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
st.title("Recent Orders")

# Editable data table
edited_df = st.data_editor(df)

# Display the edited DataFrame
st.write("Edited DataFrame:")
st.write(edited_df)