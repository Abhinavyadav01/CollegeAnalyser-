import pandas as pd
import plotly.express as px
import streamlit as st

# Vibrant colors for all charts
bright_colors = ['#ff4e50', '#fc913a', '#f9d62e', '#eae374', '#e2f4c7', '#70a1d7', '#97c1a9']

def plot_seat_distribution(df, nit_name):
    fig = px.pie(
        df,
        names='Category',
        values='Seats',
        hole=0.4,
        color_discrete_sequence=bright_colors
    )
    fig.update_traces(
        textinfo='label+percent',
        textfont_size=13,
        insidetextorientation='auto',
        marker=dict(line=dict(color='white', width=2)),
        pull=[0.05] * len(df),
        hoverlabel=dict(bgcolor='white', font_size=14, font_color='black')
    )
    fig.update_layout(
        showlegend=False,
        title={
            'text': f'✨ <span style="color:#ff4e50;">{nit_name.upper()}</span> Seat Distribution',
            'x': 0.5,
            'xanchor': 'center',
            'yanchor': 'top'
        },
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        margin=dict(t=52, b=60)
    )
    st.plotly_chart(fig, use_container_width=True)
