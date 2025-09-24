import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from collections import Counter
from wordcloud import WordCloud

# ----------------------
# Part 1: Data Loading & Basic Exploration
# ----------------------

@st.cache_data
def load_data():
    df = pd.read_csv("metadata.csv")
    return df

df = load_data()

st.title("CORD-19 Data Explorer")
st.write("Simple exploration of COVID-19 research papers (metadata.csv)")

st.subheader("Dataset Overview")
st.write("Shape of dataset:", df.shape)
st.write(df.head())

# ----------------------
# Part 2: Data Cleaning & Preparation
# ----------------------

# Handle missing publish_time safely
df["publish_time"] = pd.to_datetime(df["publish_time"], errors="coerce")
df["year"] = df["publish_time"].dt.year

# Abstract word count feature
df["abstract_word_count"] = df["abstract"].fillna("").apply(lambda x: len(str(x).split()))

# ----------------------
# Part 3: Data Analysis & Visualization
# ----------------------

st.subheader("Filters")
min_year, max_year = int(df["year"].min()), int(df["year"].max())
year_range = st.slider("Select year range", min_year, max_year, (2020, 2021))
filtered = df[df["year"].between(year_range[0], year_range[1])]

st.subheader("Analysis & Visualizations")

# Publications per year
year_counts = filtered["year"].value_counts().sort_index()
fig, ax = plt.subplots()
ax.bar(year_counts.index, year_counts.values)
ax.set_title("Publications by Year")
ax.set_xlabel("Year")
ax.set_ylabel("Count")
st.pyplot(fig)

# Top journals
top_journals = (
    filtered["journal"]
    .dropna()
    .value_counts()
    .head(10)
)
fig, ax = plt.subplots()
sns.barplot(x=top_journals.values, y=top_journals.index, ax=ax)
ax.set_title("Top Journals Publishing COVID-19 Research")
ax.set_xlabel("Number of Papers")
st.pyplot(fig)

# Word cloud of titles
titles = " ".join(filtered["title"].dropna().astype(str).values)
if titles:
    wordcloud = WordCloud(width=800, height=400, background_color="white").generate(titles)
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.imshow(wordcloud, interpolation="bilinear")
    ax.axis("off")
    st.pyplot(fig)

# Distribution by source_x
source_counts = filtered["source_x"].dropna().value_counts().head(10)
fig, ax = plt.subplots()
ax.bar(source_counts.index, source_counts.values)
ax.set_title("Publications by Source")
ax.set_ylabel("Count")
plt.xticks(rotation=45, ha="right")
st.pyplot(fig)

# ----------------------
# Part 4: Show Sample of Data
# ----------------------

st.subheader("Sample of Filtered Data")
st.write(filtered.head())

# ----------------------
# Part 5: Reflection / Notes
# ----------------------

st.subheader("Notes")
st.markdown("""
- Data loaded from **metadata.csv** of the CORD-19 dataset.
- Cleaned and prepared basic features (year, abstract word count).
- Visualized trends over time, top journals, title keywords, and sources.
- Interactive filters allow focused exploration.
""")
