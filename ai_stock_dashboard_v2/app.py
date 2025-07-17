import streamlit as st
import pandas as pd
from logic.filters import apply_filters

st.set_page_config(page_title="📊 AI Stock Screener", layout="wide")

st.title("📈 AI-Based Intraday Stock Screener")
st.markdown("इस Dashboard में आपको मिलेंगे सिर्फ वही stocks जो Fundamental + Technical दोनों से पास हैं।")

# Load sample data
data = pd.DataFrame({
    "Stock": ["ABC Ltd", "XYZ Corp", "LMN Tech"],
    "Price": [320, 145, 210],
    "ROCE": [18.2, 21.5, 13.4],
    "RSI": [60, 67, 72],
    "Volume Surge": [True, True, False],
    "VWAP Signal": ["Above", "Above", "Below"]
})

# Apply filters from logic
filtered_df = apply_filters(data)

st.subheader("📊 Filtered Stocks Table")
st.dataframe(filtered_df, use_container_width=True)
