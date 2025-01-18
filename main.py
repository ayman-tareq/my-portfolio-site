import streamlit as st
from PIL import Image

# Load your image
image = Image.open("tareq.png")  # Replace with the path to your image

# Page configuration
st.set_page_config(page_title="Tareq Hossain Portfolio", layout="centered")

# Main content
col1, col2 = st.columns([3, 1])

with col1:
    st.title("Tareq Hossain")
    st.subheader("Data Engineer at Algesoft")
    st.write(
        """Zahir Brothers, Shulokbohor, Panchlaish, Chattogram  
+88 01815-475818 (WhatsApp Only)

[LinkedIn](https://www.linkedin.com/in/aymantareq-97/) | [Email](mailto:tareq.iiuc.eb@gmail.com) | [GitHub](https://github.com/ayman-tareq)
        """
    )

with col2:
    st.image(image, width=150)

st.header("Professional Summary")
st.write(
    "Dedicated and experienced freelancing instructor and data engineer with 4+ years of expertise in "
    "freelancing platforms such as Fiverr, Upwork, and LinkedIn job hunting strategies. Proficient in teaching "
    "how to succeed in freelancing, leveraging my background in Python programming, data management, "
    "Sentiment Analysis, and Web scraping."
)

st.header("Key Skills")
st.write(
    """- Mastery of freelancing platforms: Fiverr, Upwork, and LinkedIn  
- Client acquisition and relationship management  
- Teaching freelancing career strategies and job-hunting techniques  
- Programming: Python, Node.js, C/C++, SQL, Pandas  
- Web development (Django), Browser Automation, and Data engineering  
- AWS Technologies: EC2, Lambda, S3, RDS, and CloudWatch  
- Google Cloud Platform (GCP), Google APIs, Google BigQuery"""
)

st.header("Experience")

st.subheader("Algesoft | South Korea - Data Engineer")
st.write("**January 2023 - Present**")
st.write(
    """- Engineered data pipelines and performed data maintenance using Python, AWS, SQL, Pandas, Numpy.  
- Led projects in sentiment analysis and automation for clients."""
)

st.subheader("Freelance via Fiverr and Upwork | US - Programmer")
st.write("**August 2020 - Present**")
st.write(
    """- Delivered numerous successful Python-based projects, including data analysis and browser automation.  
- Assisted clients in automating business workflows and handling complex data tasks."""
)

st.header("Certifications")
st.write(
    """- [Python for Everybody Specialization](https://coursera.org/share/265a03c494131cd8e7a570e0b2a4a182)  
- [Introduction to Git and GitHub](https://coursera.org/share/dd20929984a4e5f2f4edbc767f303575)  
- [Building Web Applications in Django](https://coursera.org/share/a5a171a28acb8fdb97bfcf3d5d149a36)  
- [Workforce Recovery Program](https://drive.google.com/file/d/14a8ayHLj8qed9HCNMDY35ImOgdHNMvwB/view?usp=sharing)
""")

st.header("Portfolio")
st.write("[Crypto Analytics Dashboard](https://crypto-analytics-1.streamlit.app/)")

st.header("Education")
st.write(
    """**International Islamic University Chittagong**  
BSS in Economics and Banking  
February 2019 - June 2023"""
)
