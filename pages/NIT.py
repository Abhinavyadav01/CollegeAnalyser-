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
        font-size: 70px;
        display: flex;
        align-items: center;
        justify-content: center;
        margin-top: 10px;
    }
    </style>
""",unsafe_allow_html=True)
st.markdown('<div class="heading">NIT DASHBOARD 2025</div>',unsafe_allow_html=True)

# Creating sidebar with all its components
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Archivo+Black&display=swap');
    .title {
        font-family: 'Archivo Black', sans-serif;
        font-size: 27px;
        color: white;
    }
    </style>
    """, unsafe_allow_html=True)
st.sidebar.markdown('<div class="title">🧭 NIT NAVIGATOR</div>', unsafe_allow_html=True)
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
from nirf import fig
st.plotly_chart(fig, use_container_width=True)



# Section 2 - Institute Location
st.markdown("---") # Horizontal line
st.markdown('<div id="section2"></div>', unsafe_allow_html=True)
st.title("📍 Institute Location")
if 'location' not in st.session_state:
    st.session_state.location = "SELECT"
df = pd.read_csv('NITs_Location_Updated.csv')
map = px.scatter_mapbox(df,
                        lat="Latitude",
                        lon="Longitude",
                        hover_name="NIT Name",
                        hover_data={"City":True ,"State/UT":True},
                        zoom=3.5,
                        height=1000,
                        mapbox_style="open-street-map",
                        title="📍 NITs Across India")
map.update_layout(height=650, width=90)
left_col, right_col = st.columns([1, 1])  # adjust width ratio
loc_option = ["SELECT","NIT Agartala","NIT Allahabad","NIT Andhra Pradesh","NIT Arunachal Pradesh","NIT Bhopal","NIT Calicut",
        "NIT Delhi","NIT Durgapur","NIT Goa","NIT Hamirpur","NIT Jaipur","NIT Jalandhar","NIT Jamshedpur","NIT Karnataka(Surathkal)",
        "NIT Kurukshetra","NIT Manipur","NIT Meghalaya","NIT Mizoram","NIT Nagaland","NIT Nagpur","NIT Patna","NIT Puducherry",
        "NIT Raipur","NIT Rourkela","NIT Sikkim","NIT Silchar","NIT Srinagar","NIT Surat(SVNIT)","NIT Tiruchirappalli(Trichy)",
        "NIT Uttarakhand","NIT Warangal"]
with left_col:
    st.markdown("<br><br><br><br><br><br><br><br><br><br>", unsafe_allow_html=True)
    st.selectbox("Choose  specific  NIT  to  see  its  location", loc_option, index = loc_option.index(st.session_state.location),
                 key = "nitkey_2")
    option = st.session_state.nitkey_2

    # Dictionary with HTML formatting
    texts = {
        "SELECT": "",
        "NIT Agartala": "<b>CITY :</b> Agartala<br><b>STATE/UT :</b> Tripura",
        "NIT Allahabad": "<b>CITY :</b> Prayagraj<br><b>STATE/UT :</b> Uttar Pradesh",
        "NIT Andhra Pradesh": "<b>CITY :</b> Tadepalligudem<br><b>STATE/UT :</b> Andhra Pradesh",
        "NIT Arunachal Pradesh": "<b>CITY :</b> Yupia<br><b>STATE/UT :</b> Arunachal Pradesh",
        "NIT Bhopal": "<b>CITY :</b> Bhopal<br><b>STATE/UT :</b> Madhya Pradesh",
        "NIT Calicut": "<b>CITY :</b> Kozhikode<br><b>STATE/UT :</b> Kerala",
        "NIT Delhi": "<b>CITY :</b> Delhi<br><b>STATE/UT :</b> Delhi",
        "NIT Durgapur": "<b>CITY :</b> Durgapur<br><b>STATE/UT :</b> West Bengal",
        "NIT Goa": "<b>CITY :</b> Farmagudi<br><b>STATE/UT :</b> Goa",
        "NIT Hamirpur": "<b>CITY :</b> Hamirpur<br><b>STATE/UT :</b> Himachal Pradesh",
        "NIT Jaipur": "<b>CITY :</b> Jaipur<br><b>STATE/UT :</b> Rajasthan",
        "NIT Jalandhar": "<b>CITY :</b> Jalandhar<br><b>STATE/UT :</b> Punjab",
        "NIT Jamshedpur": "<b>CITY :</b> Jamshedpur<br><b>STATE/UT :</b> Jharkhand",
        "NIT Karnataka(Surathkal)": "<b>CITY :</b> Mangalore<br><b>STATE/UT :</b> Karnataka",
        "NIT Kurukshetra": "<b>CITY :</b> Kurukshetra<br><b>STATE/UT :</b> Haryana",
        "NIT Manipur": "<b>CITY :</b> Imphal<br><b>STATE/UT :</b> Manipur",
        "NIT Meghalaya": "<b>CITY :</b> Shillong<br><b>STATE/UT :</b> Meghalaya",
        "NIT Mizoram": "<b>CITY :</b> Aizawl<br><b>STATE/UT :</b> Mizoram",
        "NIT Nagaland": "<b>CITY :</b> Dimapur<br><b>STATE/UT :</b> Nagaland",
        "NIT Nagpur": "<b>CITY :</b> Nagpur<br><b>STATE/UT :</b> Maharashtra",
        "NIT Patna": "<b>CITY :</b> Patna<br><b>STATE/UT :</b> Bihar",
        "NIT Puducherry": "<b>CITY :</b> Karaikal<br><b>STATE/UT :</b> Puducherry",
        "NIT Raipur": "<b>CITY :</b> Raipur<br><b>STATE/UT :</b> Chhattisgarh",
        "NIT Rourkela": "<b>CITY :</b> Rourkela<br><b>STATE/UT :</b> Odisha",
        "NIT Sikkim": "<b>CITY :</b> Ravangla<br><b>STATE/UT :</b> Sikkim",
        "NIT Silchar": "<b>CITY :</b> Silchar<br><b>STATE/UT :</b> Assam",
        "NIT Srinagar": "<b>CITY :</b> Srinagar<br><b>STATE/UT :</b> Jammu and Kashmir",
        "NIT Surat(SVNIT)": "<b>CITY :</b> Surat<br><b>STATE/UT :</b> Gujarat",
        "NIT Tiruchirappalli(Trichy)": "<b>CITY :</b> Tiruchirappalli<br><b>STATE/UT :</b> Tamil Nadu",
        "NIT Uttarakhand": "<b>CITY :</b> Srinagar (Garhwal)<br><b>STATE/UT :</b> Uttarakhand",
        "NIT Warangal": "<b>CITY :</b> Warangal<br><b>STATE/UT :</b> Telangana"
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
                 ,key = "nitkey_3t")
    transport = st.session_state.nitkey_3t

if transport == "Railway Distance":
    data = {
        'NIT Name': [
            'NIT Jalandhar', 'NIT Trichy', 'NIT Warangal', 'NIT Surathkal',
            'NIT Rourkela', 'NIT Patna', 'NIT Delhi', 'NIT Jaipur'
        ],
        'Railway Distance (km)': [5.2, 1.1, 6.8, 3.4, 8.5, 2.3, 7.7, 3.1]
    }
    df = pd.DataFrame(data)

    # Store original min and max
    orig_min_dist = float(df["Railway Distance (km)"].min())
    orig_max_dist = float(df["Railway Distance (km)"].max())

    # NIT selector
    all_options = ["All"] + sorted(df["NIT Name"].unique().tolist())
    st.multiselect("Select NIT(s):", options=all_options, default=st.session_state.selected_nits,key = "nitkey_3m")
    selected = st.session_state.nitkey_3m
    # Distance slider
    st.slider("Select Railway Distance Range (km):",
                min_value=0.0,
                max_value=round(orig_max_dist + 1, 1),
                value=st.session_state.railway_distance_range, step=0.1, key ="nitkey_3s")

    distance_range = st.session_state.nitkey_3s
    # Check if slider was touched (not at full range)
    slider_changed = (distance_range[0] > orig_min_dist) or (distance_range[1] < orig_max_dist)

    # Filtering logic
    filtered_df = df.copy()

    if "All" in selected:
        filtered_df = df.copy()
        show_plot = True
    elif selected:
        filtered_df = filtered_df[filtered_df["NIT Name"].isin(selected)]
        show_plot = True
    elif slider_changed:
        # If no NIT selected but slider changed, show all NITs in that range
        show_plot = True
    else:
        # No selection, and slider not moved → show nothing
        st.info("Please select NIT(s) or adjust the distance slider to see the chart.")
        show_plot = False

    # Apply slider filtering always
    if show_plot :
        filtered_df = filtered_df[
            (filtered_df["Railway Distance (km)"] >= distance_range[0]) &
            (filtered_df["Railway Distance (km)"] <= distance_range[1])
        ]

    # If empty result
    if show_plot and filtered_df.empty:
        st.warning("No NITs match the selected filters.")
    elif show_plot:
        filtered_df = filtered_df.sort_values(by="Railway Distance (km)", ascending=True)

        # Lollipop Plot
        railway = go.Figure()

        # Invisible anchor
        railway.add_trace(go.Scatter(
            x=[0]*len(filtered_df),
            y=filtered_df['NIT Name'],
            mode='markers',
            marker=dict(color='rgba(0,0,0,0)'),
            showlegend=False
        ))

        # Lines
        railway.add_trace(go.Scatter(
            x=filtered_df['Railway Distance (km)'],
            y=filtered_df['NIT Name'],
            mode='lines',
            line=dict(color='lightgray', width=2),
            showlegend=False
        ))

        # Dots
        railway.add_trace(go.Scatter(
            x=filtered_df['Railway Distance (km)'],
            y=filtered_df['NIT Name'],
            mode='markers',
            marker=dict(
                size=14,
                color=filtered_df['Railway Distance (km)'],
                colorscale='RdYlGn_r',
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

        railway.update_layout(
            title="🚉 Railway Distance Lollipop Chart",
            xaxis_title="Distance to Nearest Railway Station (km)",
            yaxis=dict(categoryorder='array', categoryarray=filtered_df['NIT Name']),
            plot_bgcolor='rgba(0,0,0,0)',
            height=550
        )

        st.plotly_chart(railway, use_container_width=True)

else :
    pass



# Section 4 - Seat Matrix
st.markdown("---")
st.markdown('<div id="section4"></div>', unsafe_allow_html=True)
st.title("🪑 Seat Matrix")

if 'seat_matrix_nit' not in st.session_state:
    st.session_state.seat_matrix_nit = "SELECT"
nit_list = ["SELECT","NIT Agartala","NIT Allahabad","NIT Andhra Pradesh","NIT Arunachal Pradesh","NIT Bhopal","NIT Calicut",
        "NIT Delhi","NIT Durgapur","NIT Goa","NIT Hamirpur","NIT Jaipur","NIT Jalandhar","NIT Jamshedpur","NIT Karnataka(Surathkal)",
        "NIT Kurukshetra","NIT Manipur","NIT Meghalaya","NIT Mizoram","NIT Nagaland","NIT Nagpur","NIT Patna","NIT Puducherry",
        "NIT Raipur","NIT Rourkela","NIT Sikkim","NIT Silchar","NIT Srinagar","NIT Surat(SVNIT)","NIT Tiruchirappalli(Trichy)",
        "NIT Uttarakhand","NIT Warangal"]
col1, col2 = st.columns(2)
with col2:
    st.markdown("<br>",unsafe_allow_html=True)
    st.selectbox("Choose  specific  NIT  to  see  its  Seat Distribution Matrix", nit_list
        , index=nit_list.index(st.session_state.seat_matrix_nit), key = "nitkey_4")
    selected_nit = st.session_state.nitkey_4
    if selected_nit == "SELECT":
        st.markdown("""<span style='font-size: 16px; font-weight: 600;'>This Pie chart contains total number of seats and their percentage(%) for Open, Gen-EWS, SC, ST, OBC-NCL and PwD all for Gender Neutral and also seats reserved of Female candidates. 
                This data is extracted for all branches combined and seats reserved for home state students and other state students. 
                Below the pie chart is the change in number of seats as whole for the specific institute from the last year.</span>""",unsafe_allow_html=True)
    else :
        st.markdown("""<span style='font-size: 16px; font-weight: 600;'>This Pie chart contains total number of seats and their percentage(%) for Open, Gen-EWS, SC, ST, OBC-NCL and PwD all for Gender Neutral and also seats reserved of Female candidates. 
                This data is extracted for all branches combined and seats reserved for home state students and other state students. 
                Below the pie chart is the change in number of seats as whole for the specific institute from the last year.</span>
                \n<span style='font-size: 16px;'><b>Institute having highest Open seats :</b><br>
                <b>Institute having highest Gen-EWS seats :</b><br>
                <b>Institute having highest SC seats :</b><br>
                <b>Institute having highest ST seats :</b><br>
                <b>Institute having highest OBC-NCL seats :</b><br>
                <b>Institute having highest PwD seats :</b><br>
                <b>Institute having highest Female-only seats :</b></span>""",unsafe_allow_html=True)


with col1:
    from seat import plot_seat_distribution
    if selected_nit == "SELECT":
        st.markdown("<br><br><br>",unsafe_allow_html=True)
        st.markdown("""<span style='font-size: 14px;'><b>Institute having highest Open seats :</b><br>
                <b>Institute having highest Gen-EWS seats :</b><br>
                <b>Institute having highest SC seats :</b><br>
                <b>Institute having highest ST seats :</b><br>
                <b>Institute having highest OBC-NCL seats :</b><br>
                <b>Institute having highest PwD seats :</b><br>
                <b>Institute having highest Female-only seats :</b></span>""",unsafe_allow_html=True
        )
    elif selected_nit == "NIT Agartala":
       df = pd.DataFrame(
           {"Category": ["Open", "Gen-EWS", "SC", "ST", "OBC-NCL", "PwD", "Female-only"],
           "Seats": [360, 93, 134, 174, 125, 56, 218] }
       )
       plot_seat_distribution(df, selected_nit)
       st.caption("NIT ")
# if st.button("Reset Selection"):
#     st.session_state.seat_matrix_nit = "SELECT"



# Section 5 - Campus Area
st.markdown("---")
st.markdown('<div id="section5"></div>', unsafe_allow_html=True)
st.title("🌳 Campus Area")

if 'campus_area' not in st.session_state:
    st.session_state.campus_area = "SELECT"
st.markdown("""<span style='font-size: 16px; font-weight: 600;'>The campus area of National Institutes of Technology (NITs) varies across different institutes, with some having extensive land holdings.
            For instance, IIT Kanpur's campus is spread over an area of 4.3 square kilometers (1,100 acres).Similarly, NIT Kurukshetra has a campus that spans over 300 acres.
            These campuses are designed to provide students with ample space for academic activities, research, and extracurricular pursuits.
            They often include facilities such as libraries, laboratories, hostels, and recreational areas to support a comprehensive educational experience.
            The size and layout of each NIT campus are tailored to meet the specific needs of the institution and its students.</span>""",unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)
# Read CSV file
df = pd.read_csv('NITs_Area.csv',header=None, names=['Institute', 'Area'])
top10 = df.head(10)
middle10 = df.iloc[len(df)//2 - 5 : len(df)//2 + 5]
last11 = df.tail(11)

st.selectbox("Select the list of NIT to check their Campus Area", ["SELECT","top10","middle10","last11"]
            , index = ["SELECT","top10","middle10","last11"].index(st.session_state.campus_area), key = "nitkey_5")
area = st.session_state.nitkey_5
if area == "top10" :
    # Plotly: Top 10 Horizontal Bar Chart with gradient
    top_area = px.bar(
        top10,
        x='Area',
        y='Institute',
        orientation='h',
        color='Area',
        color_continuous_scale='Reds',
        title='Top 10 NITs by Area',
        text='Area'
    )
    top_area.update_layout(
        yaxis={'categoryorder': 'total ascending'},
        title_font_size=15,
        height=450,  # 👈 increase plot height here
        margin=dict(t=60, b=40, l=60, r=30)
    )
    st.plotly_chart(top_area)

elif area == "middle10" :
    middle_area = px.scatter(
    middle10,
    x='Institute',
    y='Area',
    size='Area',
    size_max=25,
    color='Area',
    color_continuous_scale='Blues',
    title='Middle 10 NITs - Area Spread',
    text='Institute'
    )
    middle_area.update_traces(textposition='top center')
    middle_area.update_layout(
        xaxis_tickangle=45,
        title_font_size=15,
        height= 500,
        font=dict(size=11)
    )
    st.plotly_chart(middle_area)

elif area == "last11" :
    last_area = px.bar(
    last11,
    x='Area',
    y='Institute',
    orientation='h',
    color='Area',
    color_continuous_scale='Greens',
    title='last 11 NITs by Area',
    text='Area'
    )
    last_area.update_layout(
        yaxis={'categoryorder': 'total ascending'},
        title_font_size=18,
        height=450,  # 👈 increase plot height here
        margin=dict(t=60, b=40, l=60, r=30)  # 👈 optional padding to reduce clutter
    )
    st.plotly_chart(last_area)



# Section 6 - Opening & Closing Ranks
st.markdown("---")
st.markdown('<div id="section6"></div>', unsafe_allow_html=True)
st.title("🎯 Opening & Closing Ranks")
if 'oac_category' not in st.session_state:
    st.session_state.oac_category = "SELECT"
if 'oac_institute' not in st.session_state:
    st.session_state.oac_institute = "SELECT"
if 'oac_department' not in st.session_state:
    st.session_state.oac_department = "SELECT"

# Load data
df = pd.read_csv("oac values.csv")
cols = st.columns(3)
category_option = ["SELECT"] + sorted(df['Category'].unique())
institute_option = ["SELECT"] + sorted(df['Institute'].unique())
department_option = ["SELECT"] + sorted(df['Department'].unique())

# Sidebar filters
with cols[0]:
    st.selectbox("Select Category", category_option,
                index = category_option.index(st.session_state.oac_category), key = "nitkey_6c")
    category = st.session_state.nitkey_6c
with cols[1]:
    st.selectbox("Select NIT", institute_option,
                index = institute_option.index(st.session_state.oac_institute), key = "nitkey_6i")
    institute = st.session_state.nitkey_6i
with cols[2]:
    st.selectbox("Select Department", department_option,
                index = department_option.index(st.session_state.oac_department), key = "nitkey_6d")
    department = st.session_state.nitkey_6d

if (institute != "SELECT" and
    department != "SELECT" and
    category != "SELECT"):
    # Filtered Data
    filtered_df = df[(df['Institute'] == institute) &
                     (df['Department'] == department) &
                     (df['Category'] == category)]

    # Melt the DataFrame for area plot (wide → long format)
    melted_df = filtered_df.melt(id_vars='Round',
                                 value_vars=['Opening Rank', 'Closing Rank'],
                                 var_name='Rank Type',
                                 value_name='Rank')

    # Plot
    oac_ranks = px.area(melted_df,
                  x="Round",
                  y="Rank",
                  color="Rank Type",
                  line_group="Rank Type",
                  markers=True,
                  title=f"Opening & Closing Ranks for {department} at {institute} ({category})")

    oac_ranks.update_layout(yaxis_title="Rank", xaxis_title="JoSAA Round", legend_title="")

    st.plotly_chart(oac_ranks, use_container_width=True)

else:
    st.warning("Please select all fields to display the chart.")















