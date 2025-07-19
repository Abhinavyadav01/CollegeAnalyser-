import streamlit as st
import pandas as pd
import os
import datetime
import matplotlib.pyplot as plt


st.set_page_config(page_title="College Analyser", layout="wide", initial_sidebar_state="collapsed")


st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Anton&display=swap');
    @import url('https://fonts.googleapis.com/css2?family=Archivo+Black&display=swap');
    .title{
        font-family: 'Anton', sans-serif;
        font-size: 123px;
        display: flex;
        align-items: center;
        justify-content: center;
        margin-top: -23px;
        background: linear-gradient(90deg, #9FA8DA, #80DEEA);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    .head{
        font-family: 'Archivo Black', sans-serif;
        font-size: 22px;
        display: flex;
        align-items: center;
        justify-content: center;
        margin-top: -13px;
        background: linear-gradient(90deg, #9FA8DA, #80DEEA);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    </style>
""",unsafe_allow_html=True)
st.markdown('<div class="title">COLLEGE ANALYSER</div>',unsafe_allow_html=True)
st.markdown('<div class="head">Explore. Compare. Decide. Your Gateway to Selecting the Best NITs and IITs Visually</div>',unsafe_allow_html=True)

st.markdown("""<div style='margin-top: 65px;'> <span style='font-size: 18px; font-weight: 600;'>The COLLEGE ANALYSER is an intuitive, visually-driven, and highly interactive web platform built to empower users in making informed decisions about India’s premier engineering institutions
              — the Indian Institutes of Technology (IITs) and National Institutes of Technology (NITs). In a country where engineering aspirants often rely on scattered information, word of mouth, or incomplete rankings,
              this platform serves as a centralized hub for exploring, analyzing, and comparing critical data points that actually matter when selecting a college. From NIRF rankings and geographical locations to connectivity
              via railways and airports, users can now make choices with clarity, context, and confidence. Whether you're a student preparing for JEE, a parent researching the best-fit college for your child, or an education 
              analyst tracking academic trends, this dashboard is designed to deliver reliable insights in a clean, elegant format. It eliminates information overload by turning complex data into visual plots and comparisons, allowing for quick yet informed judgments.</span> </div>""",unsafe_allow_html=True)

st.markdown("""<div style='margin-top: 20px;'> <span style='font-size: 25px; font-weight: 600;'>📊 What You’ll Find Inside</span></div>""",unsafe_allow_html=True)
st.markdown("""<span style='font-size: 18px; font-weight: 600;'>Each category IIT and NIT — has its own detailed section packed with valuable insights to help users explore and compare institutes with precision.</span>""",unsafe_allow_html=True)

cols = st.columns(2)
with cols[0]:
    st.markdown(""" <span style='font-size: 21px; font-weight: 600;'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;🧭 Institute Location</span>""",unsafe_allow_html=True)
    st.markdown("""<div style='margin-top: -13px;'><span style='font-size: 18px; font-weight: 600;'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;• Interactive map showing the geography of each institute<br>
                &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;• Understand regional accessibility and travel distance<br><br></span></div>""",unsafe_allow_html=True)

    st.markdown(""" <span style='font-size: 21px; font-weight: 600;'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;🏆 NIRF Rankings</span>""",unsafe_allow_html=True)
    st.markdown("""<div style='margin-top: -13px;'><span style='font-size: 18px; font-weight: 600;'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;• Visual comparison of institute rankings<br>
                &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;• Identify trends in academic performance and reputation<br><br></span></div>""",unsafe_allow_html=True)

    st.markdown(""" <span style='font-size: 21px; font-weight: 600;'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;📍 Distance to Transport Hubs</span>""",unsafe_allow_html=True)
    st.markdown("""<div style='margin-top: -13px;'><span style='font-size: 18px; font-weight: 600;'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;• Nearest railway station and airport distance from institute<br>
                &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;• Understand travel ease and institute connectivity<br><br></span></div>""",unsafe_allow_html=True)

with cols[1]:
    st.markdown(""" <span style='font-size: 21px; font-weight: 600;'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;🔓 Opening & Closing Ranks</span>""",unsafe_allow_html=True)
    st.markdown("""<div style='margin-top: -13px;'><span style='font-size: 18px; font-weight: 600;'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;• JEE Main/Advanced opening and closing ranks<br>
                &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;• Compare based on branch, category, and institute<br><br></span></div>""",unsafe_allow_html=True)

    st.markdown(""" <span style='font-size: 21px; font-weight: 600;'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;🏢 Campus Area</span>""",unsafe_allow_html=True)
    st.markdown("""<div style='margin-top: -13px;'><span style='font-size: 18px; font-weight: 600;'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;• Gives insight into infrastructure scale and lifestyle environment<br><br></span></div>""",unsafe_allow_html=True)

    st.markdown(""" <span style='font-size: 21px; font-weight: 600;'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;🪑 Seat Matrix</span>""",unsafe_allow_html=True)
    st.markdown("""<div style='margin-top: -13px;'><span style='font-size: 18px; font-weight: 600;'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;• Visual distribution of total seats and reserved categories<br>
                &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;• Helps in understanding seat allocation dynamics<br><br></span></div>""",unsafe_allow_html=True)


# Custom CSS + HTML to create fixed bottom note
st.markdown(
    """
    <style>
        .fixed-footer {
            font-family: 'Anton', sans-serif;
            position: fixed;
            bottom: 0;
            left: 0;
            width: 100%;
            background: rgba(0, 0, 0, 0.6); /* Translucent black */
            color: white;
            text-align: center;
            padding: 10px;
            font-size: 18px;
            line-spacing: 5px;
            z-index: 100;
            backdrop-filter: blur(6px);
        }
    </style>
    <div class="fixed-footer">
        🔔 Use Sidebar to access the Dashboards.
    </div>
    """,
    unsafe_allow_html=True)

cols = st.columns(2)

with cols[0]:
    st.markdown("<br>",unsafe_allow_html=True)
    st.subheader("🚀 Future Scopes")
    with st.expander("🤖 AI Integration"):
        st.write("We plan to incorporate AI models to analyze trends and suggest improvements.")

    with st.expander("📊 Real-Time Analytics"):
        st.write("Future updates will include live dashboards and predictive graphs.")

    with st.expander("📱 Cross-Platform Support"):
        st.write("Mobile app integration is on the roadmap to reach more users.")

    with st.expander("💼 Placement Insights & Packages"):
        st.write("Track average and highest packages across domains.")

with cols[1]:
    st.markdown("""<h2 style='text-align: center;'><span style='font-size: 25px;'>👨‍💻 Developer Info</span></h2>""",unsafe_allow_html=True)
    st.markdown("""
        <style>
            .dev-card {
                background: rgba(255, 255, 255, 0.08);
                backdrop-filter: blur(12px);
                border: 1px solid rgba(255, 255, 255, 0.15);
                border-radius: 20px;
                padding: 25px;
                max-width: 400px;
                margin: auto;
                box-shadow: 0 4px 30px rgba(0, 0, 0, 0.1);
                color: white;
                font-family: 'Segoe UI', sans-serif;
                text-align: center;
                height: 250px;
            }
    
            .dev-card h2 {
                margin-bottom: 5px;
            }
    
            .dev-card p {
                margin: 5px 0 15px;
                font-size: 16px;
                color: #ddd;
            }
    
            .dev-links a {
                margin: 0 8px;
                text-decoration: none;
                color: #00bfff;
                font-weight: bold;
            }
    
            .dev-links a:hover {
                text-decoration: underline;
            }
        </style>
    
        <div class="dev-card">
            <h2> Abhinav Yadav</h2>
            <p>B.Tech | NIT Jalandhar<br>Front End Dev • Data Analyst • UI/UX Explorer</p>
            <div class="dev-links">
                <a href="mailto:abhinav.codes01@gmail.com" target="_blank">Email</a>
                <a href="http://github.com/Abhinavyadav01" target="_blank">GitHub</a>
                <a href="https://www.linkedin.com/in/abhinavyadav23/" target="_blank">LinkedIn</a>
            </div>
        </div>
    """, unsafe_allow_html=True)

st.markdown("<br>",unsafe_allow_html=True)
st.markdown("---")
col1,col2,col3 = st.columns([1,3,1])
with col2:
    st.markdown("## User Feedback Form")
    st.markdown("We’d love to hear your thoughts and suggestions!")

    # Define CSV file to store feedback
    FEEDBACK_FILE = "user_feedback.csv"

    # Emojis for slider
    emoji_dict = {
        1: "😡 Very Bad",
        2: "😞 Bad",
        3: "😐 Okay",
        4: "😊 Good",
        5: "😍 Excellent"
    }

    with st.form("feedback_form", clear_on_submit=True):
        name = st.text_input("👤 Your Name")
        email = st.text_input("📧 Your Email")
        rating_value = st.slider("🌟 Rate your experience", 1, 5, 1)

        feedback_text = st.text_area("✍️ Any suggestions or feedback?", height=150)
        submitted = st.form_submit_button("📨 Submit Feedback")

        if submitted:
            feedback_entry = {
                "Name": name,
                "Email": email,
                "Rating": rating_value,
                "Feedback": feedback_text,
                "Timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }

            # Append feedback to CSV
            if os.path.exists(FEEDBACK_FILE):
                df = pd.read_csv(FEEDBACK_FILE)
                df = pd.concat([df, pd.DataFrame([feedback_entry])], ignore_index=True)
            else:
                df = pd.DataFrame([feedback_entry])

            df.to_csv(FEEDBACK_FILE, index=False)
            st.success("✅ Thank you! Your feedback has been recorded.")

st.markdown("<br><br>",unsafe_allow_html=True)
st.markdown("""
<style>
@keyframes typing {
  from { width: 0 }
  to { width: 100% }
}
.typewriter {
  font-family: monospace;
  font-size: 20px;
  overflow: hidden;
  border-right: 3px solid white;
  white-space: nowrap;
  width: 0;
  animation: typing 4s steps(40, end) forwards;
}
</style>

<div class="typewriter">🙌 Thanks for Visiting!<br>Exciting things are in the pipeline.  
<br>Keep exploring, 🌱 keep growing — and let’s build a smarter tomorrow together 💡🚀</div>
""", unsafe_allow_html=True)



