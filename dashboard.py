import streamlit as st
import pandas as pd
import json
import time

st.title("🌾 Smart Agriculture Dashboard")

placeholder = st.empty()

while True:
    try:
        data = []
        with open("processed_data.json", "r") as f:
            for line in f:
                data.append(json.loads(line.strip()))
        df = pd.DataFrame(data[-20:])  # show last 20 entries
        placeholder.line_chart(df[["temperature", "moisture"]])
    except FileNotFoundError:
        st.warning("Waiting for data...")
    time.sleep(3)

