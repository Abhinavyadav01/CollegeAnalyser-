import pandas as pd
import plotly.express as px
import streamlit as st

# Vibrant colors for all charts
# import pandas as pd
# import plotly.express as px
# import streamlit as st
#
# bright_colors = ['#ff4e50', '#fc913a', '#f9d62e', '#eae374', '#e2f4c7', '#70a1d7', '#97c1a9']
#
# # Load the data
# df = pd.read_csv("NIT_Category_Seats.csv")
#
# # Select NIT
# nits = df['NIT'].unique().tolist()
# selected_nit = st.selectbox("Select NIT to view seat distribution:", ["SELECT"] + nits)
#
# if selected_nit != "SELECT":
#     nit_df = df[df["NIT"] == selected_nit]
#
#     fig = px.pie(
#         nit_df,
#         names='Category',
#         values='Seats',
#         hole=0.4,
#         color_discrete_sequence=bright_colors
#     )
#     fig.update_traces(
#         textinfo='label+percent',
#         textfont_size=13,
#         insidetextorientation='auto',
#         marker=dict(line=dict(color='white', width=2)),
#         pull=[0.05] * len(nit_df),
#         hoverlabel=dict(bgcolor='white', font_size=14, font_color='black')
#     )
#     fig.update_layout(
#         showlegend=False,
#         title={
#             'text': f'✨ <span style="color:#ff4e50;">{selected_nit.upper()}</span> Seat Distribution',
#             'x': 0.5,
#             'xanchor': 'center',
#             'yanchor': 'top'
#         },
#         paper_bgcolor='rgba(0,0,0,0)',
#         plot_bgcolor='rgba(0,0,0,0)',
#         margin=dict(t=52, b=60)
#     )

