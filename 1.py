import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from io import BytesIO

# Function to create a sample chart
def create_chart():
    data = {'X': [1, 2, 3, 4, 5], 'Y': [10, 20, 15, 25, 30]}
    df = pd.DataFrame(data)
    fig, ax = plt.subplots()
    ax.plot(df['X'], df['Y'])
    ax.set_title('Chart_name')
    return fig, df

# Sidebar layout
page = st.sidebar.radio("Navigation", ["Page 1", "Page 2", "Page 3"])

# Checkbox and combobox in the sidebar
st.sidebar.checkbox("Checkbox 01")
st.sidebar.checkbox("Checkbox 02")
st.sidebar.selectbox("ComboBox", ["Option 1", "Option 2", "Option 3"])

# Main layout
st.title("My_app_name")
st.write("Some description or text about the app. This text can be multiline and explain the features or purpose of the application.")

fig, df = create_chart()

# Display the chart
st.subheader("Chart_name")
st.pyplot(fig)

# Download button
buffer = BytesIO()
df.to_csv(buffer, index=False)
buffer.seek(0)
st.download_button(
    label="Download Chart data",
    data=buffer,
    file_name="chart_data.csv",
    mime="text/csv"
)
