import streamlit as st
import plotly.express as px
from nltk.sentiment import SentimentIntensityAnalyzer
from glob import glob

files = glob("**/*.txt")


def get_sentiment_scores(text):
    dates_lst = []
    positivity_lst = []
    negativity_lst = []
    for file in files:
        with open(file, "r") as f:
            text = f.read()
            analyser = SentimentIntensityAnalyzer()
            scores = analyser.polarity_scores(text)

        dates_lst.append(file.split(".")[0].removeprefix("diary\\"))
        positivity_lst.append(scores["pos"])
        negativity_lst.append(scores["neg"])
    return dates_lst, positivity_lst, negativity_lst


dates, positivity, negativity = get_sentiment_scores(files)

st.title("Diary Tone")


def generate_line_chart(x, y, x_label):
    figure = px.line(x=x, y=y, labels={"x": x_label, "y": "Date"})
    st.plotly_chart(figure)


# Positivity
st.subheader("Positivity")
generate_line_chart(positivity, dates, "Positivity")

# Negativity
st.subheader("Negativity")
generate_line_chart(negativity, dates, "Negativity")
