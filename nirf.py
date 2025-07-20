import streamlit as st
import pandas as pd
import plotly.express as px

# Sample data (replace this with your actual CSV or list)


df = pd.read_csv("NIT_Data/NIRF_NIT.csv",header=None, names=['NIT', 'NIRF Rank'])
df = df.head(21)


# Plotting
fig = px.bar(
    df,
    x='NIT',
    y='NIRF Rank',
    color='NIRF Rank',
    color_continuous_scale='YlGnBu_r',  # reverse so lower rank = better color
    title='NIRF Ranks of NITs (2025)',
    height=600
)

fig.update_layout(
    xaxis_title='NIT',
    yaxis_title='NIRF Rank',
    yaxis=dict(autorange=True),  # lower rank at bottom
    coloraxis_showscale=False
)




