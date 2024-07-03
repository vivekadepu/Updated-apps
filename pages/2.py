import streamlit as st
from streamlit_echarts import st_echarts

# Data for the Nightingale rose chart
data = [
    {"value": 40, "name": "Section A"},
    {"value": 33, "name": "Section B"},
    {"value": 28, "name": "Section C"},
    {"value": 22, "name": "Section D"},
    {"value": 20, "name": "Section E"},
    {"value": 18, "name": "Section F"},
    {"value": 15, "name": "Section G"},
    {"value": 12, "name": "Section H"}
]

# Colors for each section
color_scheme = [
    "#4caf50", "#ffeb3b", "#f44336", "#9c27b0",
    "#00bcd4", "#ff9800", "#e91e63", "#8bc34a"
]

# Options for the ECharts Nightingale rose chart
options = {
    "title": {
        "text": "Nightingale Rose Chart",
        "left": "center"
    },
    "tooltip": {
        "trigger": "item"
    },
    "legend": {
        "bottom": "5%",
        "left": "center",
        "data": [item["name"] for item in data],
        "selected": {item["name"]: True for item in data}
    },
    "series": [
        {
            "name": "Data",
            "type": "pie",
            "radius": ["30%", "70%"],
            "center": ["50%", "50%"],
            "roseType": "radius",
            "itemStyle": {
                "borderRadius": 5
            },
            "label": {
                "show": False
            },
            "emphasis": {
                "label": {
                    "show": True
                }
            },
            "data": data,
            "color": color_scheme
        }
    ]
}

# Render the chart in Streamlit
st_echarts(options=options, height="500px")
