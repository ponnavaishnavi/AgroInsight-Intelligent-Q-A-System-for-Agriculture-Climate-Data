# 📘 AgroInsight: Intelligent Q&A System for Agriculture + Climate Data
# Run all cells in order in Google Colab

# Step 1: Install required libraries
!pip install pandas streamlit pyngrok openpyxl

# Step 2: Import modules
import pandas as pd
import numpy as np
import re
import json

# Step 3: Load example datasets (from data.gov.in or local)
# You can replace these with real CSVs from data.gov.in
agri_data = pd.DataFrame({
    "State": ["Tamil Nadu", "Tamil Nadu", "Andhra Pradesh", "Andhra Pradesh"],
    "Year": [2018, 2019, 2018, 2019],
    "Crop": ["Rice", "Rice", "Rice", "Rice"],
    "Production (Tonnes)": [520000, 560000, 610000, 640000]
})

climate_data = pd.DataFrame({
    "State": ["Tamil Nadu", "Tamil Nadu", "Andhra Pradesh", "Andhra Pradesh"],
    "Year": [2018, 2019, 2018, 2019],
    "Average Rainfall (mm)": [970, 1020, 890, 940]
})

print("✅ Datasets loaded successfully!")
display(agri_data.head(), climate_data.head())

# Step 4: Define a simple Q&A function
def agroinsight_query(query):
    # Extract states, crop, and year info
    states = re.findall(r"(Tamil Nadu|Andhra Pradesh|Karnataka|Kerala)", query, flags=re.IGNORECASE)
    crop_match = re.search(r"(rice|wheat|maize|pulses|sugarcane)", query, flags=re.IGNORECASE)
    crop = crop_match.group(1).capitalize() if crop_match else None

    # Filter data
    df_agri = agri_data[(agri_data["Crop"] == crop)] if crop else agri_data
    df_agri = df_agri[df_agri["State"].isin(states)] if states else df_agri
    df_clim = climate_data[climate_data["State"].isin(states)] if states else climate_data

    # Merge and compute
    merged = pd.merge(df_agri, df_clim, on=["State", "Year"])
    summary = merged.groupby("State").mean(numeric_only=True).round(2).reset_index()

    answer = f"Here’s the comparison of {crop} production and rainfall:\n\n"
    for _, row in summary.iterrows():
        answer += f"🌾 {row['State']} – Avg Production: {row['Production (Tonnes)']} tonnes | Avg Rainfall: {row['Average Rainfall (mm)']} mm\n"
    answer += "\n📊 Sources:\n• Ministry of Agriculture & Farmers Welfare datasets (data.gov.in)\n• India Meteorological Department (IMD) datasets (data.gov.in)"
    return answer

# Step 5: Test it inside Colab
query = "Compare rainfall and rice production in Tamil Nadu and Andhra Pradesh"
print(agroinsight_query(query))
