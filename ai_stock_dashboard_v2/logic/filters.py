import pandas as pd

def apply_filters(df):
    # Apply basic technical + fundamental filter logic
    filtered = df[
        (df["ROCE"] > 15) &
        (df["RSI"] >= 55) & (df["RSI"] <= 70) &
        (df["Volume Surge"] == True) &
        (df["VWAP Signal"] == "Above")
    ]
    return filtered.reset_index(drop=True)
