🌾 AgroInsight – Intelligent Q&A System for Agriculture & Climate Data
🧠 Overview

AgroInsight is a prototype built for the Build for Bharat Fellowship 2026 (Project Samarth).
It is an intelligent Question-Answering system designed to help policymakers, researchers, and citizens explore and analyze open government datasets from data.gov.in
.

The system answers complex natural language questions about agricultural production and climate patterns, combining multiple inconsistent datasets from different ministries — particularly:

Ministry of Agriculture & Farmers Welfare

India Meteorological Department (IMD)

🚀 Objective

Government datasets often exist in siloed formats (CSV, JSON, XML) with different structures and coded values.
AgroInsight bridges these silos to enable real-time reasoning across them.

Example Queries:

“Compare rainfall and rice production in Tamil Nadu and Andhra Pradesh for the last 5 years.”

“Find the district with the lowest maize production in Karnataka and correlate it with rainfall data.”

🧩 System Design
Component	Description
Frontend (UI)	Built using Streamlit for a simple Q&A chat interface.
Backend (Logic)	Implemented in Python using FastAPI / Pandas for query parsing and data fusion.
Data Sources	Live or static datasets from data.gov.in – Agriculture & IMD.
Query Understanding	Basic NLP via Regex and keyword matching (can be extended using spaCy / LLM).
Output	Natural language summary + table comparison + dataset citations.
⚙️ Tech Stack

Language: Python

Libraries: Pandas, NumPy, Streamlit, Pyngrok, FastAPI

Data Format: CSV (can be adapted for API/JSON sources)

Hosting: Google Colab / Streamlit Cloud

📊 Prototype Features

✅ Loads and integrates real agriculture and climate datasets
✅ Answers user questions in natural language
✅ Provides summarized comparisons and insights
✅ Cites the exact data sources used
✅ Designed with data sovereignty and privacy in mind

🧪 How to Run in Google Colab

Open the notebook:
AgroInsight_Prototype.ipynb

Run all code cells in order.

Modify the query inside the notebook:

query = "Compare rainfall and rice production in Tamil Nadu and Andhra Pradesh"
print(agroinsight_query(query))


To use the Streamlit chat UI (optional), run the Streamlit cell and open the ngrok URL shown.

🎥 Demo Video

🔗 Loom Video (2 min)

A walkthrough showing datasets, code logic, and live query demonstration.

🧾 Sample Output
Here’s the comparison of Rice production and rainfall:

🌾 Tamil Nadu – Avg Production: 540000 tonnes | Avg Rainfall: 995 mm
🌾 Andhra Pradesh – Avg Production: 625000 tonnes | Avg Rainfall: 915 mm

📊 Sources:
• Ministry of Agriculture & Farmers Welfare datasets (data.gov.in)
• India Meteorological Department (IMD) datasets (data.gov.in)

💡 Future Enhancements

Integrate live API access from data.gov.in instead of static CSVs.

Add semantic search using embeddings or LLMs for better query understanding.

Implement district-level drilldowns for micro-analysis.

Deploy on a secure cloud with access control and offline mode for government use.

👩‍💻 Created By

Ponna Vaishnavi
📧 ponnavaishnavi0511@gmail.com
