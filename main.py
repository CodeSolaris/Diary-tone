import streamlit as st
import plotly.express as px
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

def get_sentiment_scores(text):
    sid_obj = SentimentIntensityAnalyzer()
    sentiment_dict = sid_obj.polarity_scores(text)
    sentiment_dict.pop("compound")
    return sentiment_dict
st.title("Diary Tone")
st.write("Positivity")

figure = px.line(x=positivity, y=dates, labels={"x": "Positivity", "y": "Date"})
plotly_chart = st.plotly_chart(figure=None)

st.write("Negativity")