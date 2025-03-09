import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

all_df = pd.read_csv("all_data.csv")

all_df["date"] = pd.to_datetime(all_df["date"])

st.title("Bike Sharing Dashboard")

st.subheader("Bike Rentals by Season")
fig, ax = plt.subplots(figsize=(12, 6))
sns.barplot(x='season', y= 'count', data=all_df, palette="magma")
ax.set_xlabel("Season")
ax.set_ylabel("Rentals")
st.pyplot(fig)

st.subheader("Bike Rentals by Month and Weather Condition")
fig, ax = plt.subplots(figsize=(12, 6))
sns.scatterplot(x="month", y="count", hue="weather_condition", data=all_df)
ax.set_xlabel("Date")
ax.set_ylabel("Number of Rentals")
st.pyplot(fig)

st.subheader("Distribution of registered and casual rentals")
sns.scatterplot(x='casual', y="registered", data=all_df)
ax.set_xlabel("Casual")
ax.set_ylabel("Registered")
st.pyplot(fig)