# Save this code as app.py
import streamlit as st
from textblob import TextBlob
import pandas as pd

# Title and Description
st.title("Customer Feedback Sentiment Analyzer")
st.write("Paste your customer feedback below to analyze sentiment.")

# Input Section
feedback = st.text_area("Enter Feedback", height=150)

# Analyze Sentiment Button
if st.button("Analyze Sentiment"):
    if feedback.strip():
        blob = TextBlob(feedback)
        polarity = blob.sentiment.polarity
        sentiment = (
            "Positive" if polarity > 0 else "Negative" if polarity < 0 else "Neutral"
        )
        st.write(f"Sentiment: **{sentiment}**")
        st.write(f"Polarity Score: {polarity}")
    else:
        st.warning("Please enter some feedback!")

# Batch Analysis (Optional)
uploaded_file = st.file_uploader("Upload a CSV file for batch analysis")
if uploaded_file:
    df = pd.read_csv(uploaded_file)
    df["Sentiment"] = df["Customer Feedback"].apply(
        lambda x: "Positive" if TextBlob(x).sentiment.polarity > 0 else "Negative" if TextBlob(x).sentiment.polarity < 0 else "Neutral"
    )
    st.write("Results:")
    st.dataframe(df)
    st.download_button(
        label="Download Results",
        data=df.to_csv(index=False),
        file_name="sentiment_results.csv",
        mime="text/csv",
    )

    import matplotlib.pyplot as plt
import seaborn as sns
from io import BytesIO

if not df.empty:  # Check if data exists
    sentiment_counts = df["Sentiment"].value_counts()
    
    # Create Bar Plot
    plt.figure(figsize=(8, 5))
    sns.barplot(x=sentiment_counts.index, y=sentiment_counts.values)
    plt.title("Sentiment Distribution")
    plt.xlabel("Sentiment")
    plt.ylabel("Count")
    
    # Save Plot to Buffer
    buf = BytesIO()
    plt.savefig(buf, format="png")
    buf.seek(0)
    
    # Display in Streamlit
    st.image(buf)
