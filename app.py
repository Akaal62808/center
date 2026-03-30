import streamlit as st

st.set_page_config(page_title="Gurshan Computer Centre", layout="wide")

Sidebar Navigation

st.sidebar.title("📚 Navigation") page = st.sidebar.radio("Go to", ["Home", "About Us", "Courses", "Contact"])

#---------------- HOME PAGE ----------------

if page == "Home": st.markdown(""" <style> .hero { background-image: url('https://images.unsplash.com/photo-1581092334651-ddf26d9a09d0'); background-size: cover; padding: 80px; border-radius: 15px; text-align: center; color: white; } .btn { background-color: #ff4b4b; color: white; padding: 10px 20px; border-radius: 8px; text-decoration: none; font-size: 18px; } </style> """, unsafe_allow_html=True)

st.markdown("""
<div class="hero">
    <h1>Welcome to Gurshan Computer Centre</h1>
    <p>Empowering students with skills for a brighter digital future 🚀</p>
    <a href="#contact" class="btn">Join Now</a>
</div>
""", unsafe_allow_html=True)

st.write("\n")

st.subheader("Why Choose Us?")
st.write("✔ Experienced Trainers")
st.write("✔ Practical Learning")
st.write("✔ 100% Career Guidance")

#---------------- ABOUT PAGE ----------------

elif page == "About Us": st.title("About Gurshan Computer Centre") st.write(""" Gurshan Computer Centre is dedicated to providing high-quality computer education to students of all levels. Our mission is to empower students with modern digital skills that help them succeed in today’s competitive world. We focus on practical training, experienced guidance, and career-oriented learning. Thousands of students have built their future with us, and we continue to guide new learners every day. """)

#---------------- COURSES PAGE ----------------

elif page == "Courses": st.title("Our Courses")

col1, col2 = st.columns(2)

with col1:
    st.image("https://images.unsplash.com/photo-1518779578993-ec3579fee39f")
    st.subheader("Basic Computer Course")

with col2:
    st.image("https://images.unsplash.com/photo-1517430816045-df4b7de11d1d")
    st.subheader("Web Development Course")

col3, col4 = st.columns(2)

with col3:
    st.image("https://images.unsplash.com/photo-1555949963-aa79dcee981c")
    st.subheader("Python Programming")

with col4:
    st.image("https://images.unsplash.com/photo-1584697964403-3c4f4c4c4c4c")
    st.subheader("Tally with GST")

#---------------- CONTACT PAGE ----------------

elif page == "Contact": st.title("Contact Us")

st.write("📞 Phone: +91 98765 43210")
st.write("📧 Email: gurshancomputer@gmail.com")

st.subheader("Visit Us")

st.markdown("""
<iframe src="https://www.google.com/maps?q=Delhi&output=embed" width="100%" height="400"></iframe>
""", unsafe_allow_html=True)

st.subheader("Send Message")
name = st.text_input("Your Name")
message = st.text_area("Your Message")

if st.button("Submit"):
    st.success("Thanks! We will contact you soon.")
