import streamlit as st



# Custom CSS styling
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Archivo+Black&display=swap');
    .title {
        text-align: center;
        font-family: 'Archivo Black', sans-serif;
        font-size: 48px;
        margin-top: 20px;
        color: white;
    }

    .card-container {
        display: flex;
        justify-content: center;
        margin-top: 60px;
        gap: 100px;
    }

    .card {
        background-color: #1e2a38;
        padding: 40px 30px;
        border-radius: 15px;
        width: 250px;
        text-align: center;
        cursor: pointer;
        box-shadow: 0 6px 20px rgba(0, 0, 0, 0.3);
        transition: transform 0.2s ease, box-shadow 0.2s ease;
    }

    .card:hover {
        transform: translateY(-5px);
        box-shadow: 0 8px 25px rgba(0, 0, 0, 0.4);
    }

    .card * {
       position: relative;
       z-index: 2;  /* Keep text above the image */
    }

    .card-title {
        font-family: 'Archivo Black', sans-serif;
        font-size: 60px;
        color: #dbe8f3;
        margin-bottom: 15px;
    }

    .card-subtitle {
        font-size: 20px;
        font-weight: bold;
        color: #cfd8dc;
        font-family: Arial, sans-serif;
    }
    a{
        text-decoration: none;
        color: inherit;
    }
    </style>
""", unsafe_allow_html=True)

# HTML content
st.markdown('<div class="title">CHOOSE YOUR INSTITUTE</div>', unsafe_allow_html=True)

st.markdown("""
    <div class="card-container">
        <a href= "?goto=NIT">
            <div class="card" onclick="window.location.href='#nit'">
                <div class="card-title">NIT</div>
                <div class="card-subtitle">National Institute of<br>Technology</div>
            </div>
        </a>
        <a href= "?goto=IIT">
            <div class="card" onclick="window.location.href='#iit'">
                <div class="card-title">IIT</div>
                <div class="card-subtitle">Indian Institute of<br>Technology</div>
            </div>
        </a>
    </div>
""", unsafe_allow_html=True)



