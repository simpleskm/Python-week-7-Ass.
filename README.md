# CORD-19 Data Explorer

A simple Streamlit application to explore the **CORD-19 metadata.csv** dataset. The app provides basic data cleaning, analysis, and visualizations of COVID-19 research papers.

---

## 🚀 Features
- Load and explore the `metadata.csv` dataset
- Handle missing values and prepare features (e.g., year, abstract word count)
- Interactive filters for year range selection
- Visualizations:
  - Publications by year
  - Top journals publishing COVID-19 research
  - Word cloud of paper titles
  - Distribution of papers by source
- Display a sample of filtered data

---

## 🛠️ Requirements
- Python 3.7+
- pandas
- matplotlib
- seaborn
- streamlit
- wordcloud

Install dependencies:
```bash
pip install pandas matplotlib seaborn streamlit wordcloud
```

---

## 📂 Dataset
Download the **metadata.csv** file from the [CORD-19 dataset](https://www.kaggle.com/allen-institute-for-ai/CORD-19-research-challenge) and place it in the project directory.

---

## ▶️ Usage
Run the Streamlit app with:
```bash
streamlit run cord19_app.py
```

Then open the provided local URL in your browser (usually `http://localhost:8501`).

---

## 📊 Example Visualizations
- Number of publications per year
- Top publishing journals
- Word cloud of titles
- Distribution by source

---

## 📘 Notes
- Start with a subset of the dataset if loading is slow
- Uses `st.cache_data` to speed up repeated data loading
- This project is for educational purposes and basic exploration
