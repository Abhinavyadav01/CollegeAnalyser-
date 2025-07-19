# Importing modules
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import matplotlib.colors as mcolors
import streamlit as st
import plotly.graph_objects as go
from streamlit import session_state

st.set_page_config(
    page_title = "My Project",
    layout = "wide"
)


# Creating page Header
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Archivo+Black&display=swap');
    .heading{
        font-family: 'Archivo Black', sans-serif;
        font-size: 75px;
        display: flex;
        align-items: center;
        background: linear-gradient(90deg, #FCE4EC, #F8BBD0);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        justify-content: center;
        margin-top: 10px;
    }
    </style>
""",unsafe_allow_html=True)
st.markdown('<div class="heading">IIT DASHBOARD 2025</div>',unsafe_allow_html=True)

# Creating sidebar with all its components
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Archivo+Black&display=swap');
    .title {
        font-family: 'Archivo Black', sans-serif;
        font-size: 26px;
        color: white;
    }
    </style>
    """, unsafe_allow_html=True)
st.sidebar.markdown('<div class="title">🧭 IIT NAVIGATOR</div>', unsafe_allow_html=True)
st.sidebar.markdown("<br>", unsafe_allow_html=True)
st.sidebar.markdown("""
    <style>
        
        .hover-text {
            display: block;
            padding: 12px 16px;
            border-radius: 8px;
            font-size: 16px;
            font-weight: 600;
            text-decoration: none !important;
            color: white !important;
            transition: background-color 0.3s ease;
        }

        .hover-text:hover {
            background-color: rgba(0, 0, 0, 0.1);
            cursor: pointer;
        }
    </style>
    <a href="#section1" class="hover-text">🏆 NIRF Ranking</a>
    <a href="#section2" class="hover-text">📍 Institute Location</a>
    <a href="#section3" class="hover-text">🚅 Transport Ease</a>
    <a href="#section4" class="hover-text">🪑 Seat Matrix</a>
    <a href="#section5" class="hover-text">🌳 Campus Area</a>
    <a href="#section6" class="hover-text">🎯 Opening and Closing Ranks</a>
""", unsafe_allow_html=True)



# Section 1 - NIRF Ranking
st.markdown("---")
st.markdown('<div id="section1"></div>', unsafe_allow_html=True)
st.title("🏆 NIRF Ranking")

df = pd.read_csv("NIRF_IIT.csv",header=None, names=['IIT', 'NIRF Rank'])

# Plotting
fig = px.bar(
    df,
    x='IIT',
    y='NIRF Rank',
    color='NIRF Rank',
    color_continuous_scale='YlGnBu_r',  # reverse so lower rank = better color
    title='NIRF Ranks of IITs (2025)',
    height=600
)

fig.update_layout(
    xaxis_title='IIT',
    yaxis_title='NIRF Rank',
    yaxis=dict(autorange=True),  # lower rank at bottom
    coloraxis_showscale=False
)
st.plotly_chart(fig, use_container_width=True)
st.info("IIT Dharwad and IIT Goa are not in plot because they have 100+ NIRF rankings.")



# Section 2 - Institute Location
st.markdown("---") # Horizontal line
st.markdown('<div id="section2"></div>', unsafe_allow_html=True)
st.title("📍 Institute Location")
if 'location' not in st.session_state:
    st.session_state.location = "SELECT"
df = pd.read_csv('IITs_Location_Updated.csv')
map = px.scatter_mapbox(df,
                        lat="Latitude",
                        lon="Longitude",
                        hover_name="Institute",
                        hover_data={"City":True ,"State/UT":True},
                        zoom=3.5,
                        height=1000,
                        mapbox_style="open-street-map",
                        title="📍 IITs Across India")
map.update_layout(height=650, width=90)
left_col, right_col = st.columns(2)  # adjust width ratio
loc_option = ["SELECT","IIT Bhilai","IIT Bhubaneswar","IIT Bombay","IIT Delhi","IIT Dhanbad (ISM)","IIT Dharwad","IIT Gandhinagar",
              "IIT Goa","IIT Guwahati","IIT Hyderabad","IIT Indore","IIT Jammu","IIT Jodhpur","IIT Kanpur","IIT Kharagpur",
              "IIT Madras","IIT Mandi","IIT Nagpur","IIT Palakkad","IIT Patna","IIT Roorkee","IIT Ropar","IIT Tirupati"]
with left_col:
    st.markdown("<br><br><br><br><br><br><br><br><br><br>", unsafe_allow_html=True)
    st.selectbox("Choose  specific  IIT  to  see  its  location", loc_option, index = loc_option.index(st.session_state.location),
                 key = "iitkey_2")
    option = st.session_state.iitkey_2

    # Dictionary with HTML formatting
    texts = {
        "SELECT": "",
        "IIT Bhilai": "<b>CITY :</b> Bhilai<br><b>STATE/UT :</b> Chhattisgarh",
        "IIT Bhubaneswar": "<b>CITY :</b> Bhubaneswar<br><b>STATE/UT :</b> Odisha",
        "IIT Bombay": "<b>CITY :</b> Mumbai<br><b>STATE/UT :</b> Maharashtra",
        "IIT Delhi": "<b>CITY :</b> New Delhi<br><b>STATE/UT :</b> Delhi",
        "IIT Dhanbad (ISM)": "<b>CITY :</b> Dhanbad<br><b>STATE/UT :</b> Jharkhand",
        "IIT Dharwad": "<b>CITY :</b> Dharwad<br><b>STATE/UT :</b> Karnataka",
        "IIT Gandhinagar": "<b>CITY :</b> Gandhinagar<br><b>STATE/UT :</b> Gujarat",
        "IIT Goa": "<b>CITY :</b> Farmagudi<br><b>STATE/UT :</b> Goa",
        "IIT Guwahati": "<b>CITY :</b> Guwahati<br><b>STATE/UT :</b> Assam",
        "IIT Hyderabad": "<b>CITY :</b> Hyderabad<br><b>STATE/UT :</b> Telangana",
        "IIT Indore": "<b>CITY :</b> Indore<br><b>STATE/UT :</b> Madhya Pradesh",
        "IIT Jammu": "<b>CITY :</b> Jammu<br><b>STATE/UT :</b> Jammu and Kashmir",
        "IIT Jodhpur": "<b>CITY :</b> Jodhpur<br><b>STATE/UT :</b> Rajasthan",
        "IIT Kanpur": "<b>CITY :</b> Kanpur<br><b>STATE/UT :</b> Uttar Pradesh",
        "IIT Kharagpur": "<b>CITY :</b> Kharagpur<br><b>STATE/UT :</b> West Bengal",
        "IIT Madras": "<b>CITY :</b> Chennai<br><b>STATE/UT :</b> Tamil Nadu",
        "IIT Mandi": "<b>CITY :</b> Mandi<br><b>STATE/UT :</b> Himachal Pradesh",
        "IIT Nagpur": "<b>CITY :</b> Nagpur<br><b>STATE/UT :</b> Maharashtra",
        "IIT Palakkad": "<b>CITY :</b> Palakkad<br><b>STATE/UT :</b> Kerala",
        "IIT Patna": "<b>CITY :</b> Patna<br><b>STATE/UT :</b> Bihar",
        "IIT Roorkee": "<b>CITY :</b> Roorkee<br><b>STATE/UT :</b> Uttarakhand",
        "IIT Ropar": "<b>CITY :</b> Rupnagar<br><b>STATE/UT :</b> Punjab",
        "IIT Tirupati": "<b>CITY :</b> Tirupati<br><b>STATE/UT :</b> Andhra Pradesh"
    }

    st.markdown(f"<p style='font-size:16px'>{texts[option]}</p>", unsafe_allow_html=True)
# Place map in the right column
with right_col:
    st.plotly_chart(map)
    st.markdown("""
        <div style='margin-top: -85px; font-size: 0.85rem; color: gray; text-align: left;'>
            Use the selectbox to check specific Institute location.
        </div>
    """, unsafe_allow_html=True)



# Section 3 - Transport Ease
st.markdown("---")
st.markdown('<div id="section3"></div>', unsafe_allow_html=True)
st.title("🚅 Transport Ease")

#  Initialize session state keys
if 'transport_mode' not in st.session_state:
    st.session_state.transport_mode = "SELECT"
if 'selected_nits' not in st.session_state:
    st.session_state.selected_nits = []
if 'railway_distance_range' not in st.session_state:
    st.session_state.railway_distance_range = (0.0, 10.0)
cols = st.columns(3)
with cols[1]:
    st.selectbox("Choose mode of transport", ["SELECT", "Railway Distance", "Airport Distance"]
                 , index=["SELECT", "Railway Distance", "Airport Distance"].index(st.session_state.transport_mode)
                 ,key = "iitkey_3t")
    transport = st.session_state.iitkey_3t


if transport == "Railway Distance":
    data = {
        'IIT Name': ["IIT Bhilai","IIT Bhubaneswar","IIT Bombay","IIT Delhi","IIT Dhanbad (ISM)","IIT Dharwad","IIT Gandhinagar",
              "IIT Goa","IIT Guwahati","IIT Hyderabad","IIT Indore","IIT Jammu","IIT Jodhpur","IIT Kanpur","IIT Kharagpur",
              "IIT Madras","IIT Mandi","IIT Nagpur","IIT Palakkad","IIT Patna","IIT Roorkee","IIT Ropar","IIT Tirupati"],
        'Railway Distance (km)': [17.4, 22.9, 10.2, 12.3, 14.6, 6.4, 19.8, 9.7, 18.6, 15.3, 25.0, 21.2, 16.8, 11.1, 13.5, 8.6, 9.2, 20.3, 23.4, 12.7, 10.5, 7.9, 14.1]


    }
    df = pd.DataFrame(data)

    # Store original min and max
    orig_min_dist = float(df["Railway Distance (km)"].min())
    orig_max_dist = float(df["Railway Distance (km)"].max())

    # NIT selector
    all_options = ["All"] + sorted(df["IIT Name"].unique().tolist())
    st.multiselect("Select IIT(s):", options=all_options, default=st.session_state.selected_nits,key = "iitkey_3m")
    selected = st.session_state.iitkey_3m
    # Distance slider
    st.slider("Select Railway Distance Range (km):",
                min_value=0.0 +0,
                max_value=round(orig_max_dist ,1),
                value=(orig_min_dist-1, orig_max_dist),
                step=0.1, key ="iitkey_3s")

    distance_range = st.session_state.iitkey_3s
    # Check if slider was touched (not at full range)
    slider_changed = (distance_range[0] > orig_min_dist) or (distance_range[1] < orig_max_dist)

    # Filtering logic
    filtered_df = df.copy()

    if "All" in selected:
        filtered_df = df.copy()
        show_plot = True
    elif selected:
        filtered_df = filtered_df[filtered_df["IIT Name"].isin(selected)]
        show_plot = True
    elif slider_changed:
        # If no NIT selected but slider changed, show all IITs in that range
        show_plot = True
    else:
        # No selection, and slider not moved → show nothing
        st.info("Please select IIT(s) or adjust the distance slider to see the chart.")
        show_plot = False

    # Apply slider filtering always
    if show_plot :
        filtered_df = filtered_df[
            (filtered_df["Railway Distance (km)"] >= distance_range[0]) &
            (filtered_df["Railway Distance (km)"] <= distance_range[1])
        ]

    # If empty result
    if show_plot and filtered_df.empty:
        st.warning("No IITs match the selected filters.")
    elif show_plot:
        filtered_df = filtered_df.sort_values(by="Railway Distance (km)", ascending=True)

        # Lollipop Plot
        railway = go.Figure()

        # Invisible anchor
        railway.add_trace(go.Scatter(
            x=[0]*len(filtered_df),
            y=filtered_df['IIT Name'],
            mode='markers',
            marker=dict(color='rgba(0,0,0,0)'),
            showlegend=False
        ))

        # Lines
        railway.add_trace(go.Scatter(
            x=filtered_df['Railway Distance (km)'],
            y=filtered_df['IIT Name'],
            mode='lines',
            line=dict(color='lightgray', width=2),
            showlegend=False
        ))
        global_min = df['Railway Distance (km)'].min()
        global_max = df['Railway Distance (km)'].max()
        # Dots
        railway.add_trace(go.Scatter(
            x=filtered_df['Railway Distance (km)'],
            y=filtered_df['IIT Name'],
            mode='markers',
            marker=dict(
                size=14,
                color=filtered_df['Railway Distance (km)'],
                colorscale='RdYlGn_r',
                cmin=global_min,   # 👈 force color scale to cover full range
                cmax=global_max,
                colorbar=dict(
                    thickness=18,
                    len=0.85,
                    yanchor='middle',
                    y=0.5
                ),
                line=dict(width=1, color='black')
            ),
            name='Distance (km)'
        ))

        plot_height = max(550, len(filtered_df) * 40)  # 40 px per IIT for breathing space

        railway.update_layout(
            title="🚉 Railway Distance Lollipop Chart",
            xaxis_title="Distance to Nearest Railway Station (km)",
            yaxis=dict(
                categoryorder='array',
                categoryarray=filtered_df['IIT Name'],
                automargin=True  # prevent cutting labels
            ),
            plot_bgcolor='rgba(0,0,0,0)',
            height=plot_height,
            margin=dict(l=160, r=30)  # extra left margin for long IIT names
        )


        st.plotly_chart(railway, use_container_width=True)

elif transport == "Airport Distance":
    data = {
        'IIT Name': ["IIT Bhilai","IIT Bhubaneswar","IIT Bombay","IIT Delhi","IIT Dhanbad (ISM)","IIT Dharwad","IIT Gandhinagar",
              "IIT Goa","IIT Guwahati","IIT Hyderabad","IIT Indore","IIT Jammu","IIT Jodhpur","IIT Kanpur","IIT Kharagpur",
              "IIT Madras","IIT Mandi","IIT Nagpur","IIT Palakkad","IIT Patna","IIT Roorkee","IIT Ropar","IIT Tirupati"],
        'Airport Distance (km)': [35.7, 42.6, 7.6, 16.8, 39.2, 48.9, 37.4, 33.3, 44.5, 19.1, 52.0, 41.8, 24.9, 14.2, 19.7, 26.5, 22.0, 36.4, 47.1, 28.6, 20.3, 18.9, 31.7]



    }
    df = pd.DataFrame(data)
    # Store original min and max
    orig_min_dist = float(df["Airport Distance (km)"].min())
    orig_max_dist = float(df["Airport Distance (km)"].max())

    # NIT selector
    all_options = ["All"] + sorted(df["IIT Name"].unique().tolist())
    st.multiselect("Select IIT(s):", options=all_options, default=st.session_state.selected_nits,key = "iitkey_3m")
    selected = st.session_state.iitkey_3m
    # Distance slider
    st.slider("Select Airport Distance Range (km):",
                min_value=0.0 ,
                max_value=round(orig_max_dist ,1),
                value=(orig_min_dist-6, orig_max_dist),
                step=0.1, key ="iitkey_3s")

    distance_range = st.session_state.iitkey_3s
    # Check if slider was touched (not at full range)
    slider_changed = (distance_range[0] > orig_min_dist) or (distance_range[1] < orig_max_dist)

    # Filtering logic
    filtered_df = df.copy()

    if "All" in selected:
        filtered_df = df.copy()
        show_plot = True
    elif selected:
        filtered_df = filtered_df[filtered_df["IIT Name"].isin(selected)]
        show_plot = True
    elif slider_changed:
        # If no IIT selected but slider changed, show all IITs in that range
        show_plot = True
    else:
        # No selection, and slider not moved → show nothing
        st.info("Please select IIT(s) or adjust the distance slider to see the chart.")
        show_plot = False

    # Apply slider filtering always
    if show_plot :
        filtered_df = filtered_df[
            (filtered_df["Airport Distance (km)"] >= distance_range[0]) &
            (filtered_df["Airport Distance (km)"] <= distance_range[1])
        ]

    # If empty result
    if show_plot and filtered_df.empty:
        st.warning("No IITs match the selected filters.")
    elif show_plot:
        filtered_df = filtered_df.sort_values(by="Airport Distance (km)", ascending=True)

        # Lollipop Plot
        Airport = go.Figure()

        # Invisible anchor
        Airport.add_trace(go.Scatter(
            x=[0]*len(filtered_df),
            y=filtered_df['IIT Name'],
            mode='markers',
            marker=dict(color='rgba(0,0,0,0)'),
            showlegend=False
        ))

        # Lines
        Airport.add_trace(go.Scatter(
            x=filtered_df['Airport Distance (km)'],
            y=filtered_df['IIT Name'],
            mode='lines',
            line=dict(color='lightgray', width=2),
            showlegend=False
        ))
        global_min = df['Airport Distance (km)'].min()
        global_max = df['Airport Distance (km)'].max()
        # Dots
        Airport.add_trace(go.Scatter(
            x=filtered_df['Airport Distance (km)'],
            y=filtered_df['IIT Name'],
            mode='markers',
            marker=dict(
                size=14,
                color=filtered_df['Airport Distance (km)'],
                colorscale='RdYlGn_r',
                cmin=global_min,   # 👈 force color scale to cover full range
                cmax=global_max,
                colorbar=dict(
                    thickness=18,
                    len=0.85,
                    yanchor='middle',
                    y=0.5
                ),
                line=dict(width=1, color='black')
            ),
            name='Distance (km)'
        ))

        plot_height = max(550, len(filtered_df) * 40)  # 40 px per IIT for breathing space

        Airport.update_layout(
            title="🚉 Airport Distance Lollipop Chart",
            xaxis_title="Distance to Nearest Airport (km)",
            yaxis=dict(
                categoryorder='array',
                categoryarray=filtered_df['IIT Name'],
                automargin=True  # prevent cutting labels
            ),
            plot_bgcolor='rgba(0,0,0,0)',
            height=plot_height,
            margin=dict(l=160, r=30)  # extra left margin for long IIT names
        )


        st.plotly_chart(Airport, use_container_width=True)

else :
    pass
