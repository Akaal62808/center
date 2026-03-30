import streamlit as st

st.set_page_config(page_title="Gurshan Computer Centre", layout="wide")

# ---------- SESSION STATE (for button navigation) ----------
if "page" not in st.session_state:
    st.session_state.page = "Home"

# ---------- SIDEBAR ----------
st.sidebar.title("📚 Navigation")
selected = st.sidebar.radio(
    "Go to",
    ["Home", "About Us", "Courses", "Contact"],
    index=["Home", "About Us", "Courses", "Contact"].index(st.session_state.page)
)

st.session_state.page = selected

# ---------------- HOME PAGE ----------------
if st.session_state.page == "Home":

    st.markdown("""
    <style>
    .hero {
        background-image: url('https://images.unsplash.com/photo-1581092334651-ddf26d9a09d0');
        background-size: cover;
        padding: 80px;
        border-radius: 15px;
        text-align: center;
        color: white;
    }
    .btn {
        background-color: #ff4b4b;
        color: white;
        padding: 12px 25px;
        border-radius: 8px;
        text-decoration: none;
        font-size: 18px;
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="hero">
        <h1>Welcome to Gurshan Computer Centre</h1>
        <p>Build your future with powerful computer skills and confidence 🚀</p>
    </div>
    """, unsafe_allow_html=True)

    st.write("")

    if st.button("🚀 Join Now"):
        st.session_state.page = "Contact"
        st.rerun()

    st.write("")

    st.subheader("Why Choose Us?")
    st.write("✔ Experienced Trainers")
    st.write("✔ Practical Learning")
    st.write("✔ 100% Career Guidance")

# ---------------- ABOUT PAGE ----------------
elif st.session_state.page == "About Us":

    st.title("About Gurshan Computer Centre")

    st.write("""
    Gurshan Computer Centre is committed to providing quality computer education to students of all levels. 
    Our goal is to make students confident in digital skills so they can succeed in modern careers. 
    We focus on practical knowledge, expert guidance, and real-world applications. 
    Many students have successfully built their careers after learning from our institute, 
    and we continue to guide new learners every day toward a bright future.
    """)

# ---------------- COURSES PAGE ----------------
elif st.session_state.page == "Courses":

    st.title("Our Courses")

    col1, col2 = st.columns(2)

    with col1:
        st.image("https://images.unsplash.com/photo-1518779578993-ec3579fee39f")
        st.subheader("Basic Computer Course")

    with col2:
        st.image("https://images.unsplash.com/photo-1517430816045-df4b7de11d1d")
        st.subheader("Web Development")

    col3, col4 = st.columns(2)

    with col3:
        st.image("https://images.unsplash.com/photo-1555949963-aa79dcee981c")
        st.subheader("Python Programming")

    with col4:
        st.image("https://images.unsplash.com/photo-1584697964403-3c4f4c4c4c4c")
        st.subheader("Tally with GST")

# ---------------- CONTACT PAGE ----------------
elif st.session_state.page == "Contact":

    st.title("Contact Us")

    st.write("📞 Phone: +91 98765 43210")
    st.write("📧 Email: gurshancomputer@gmail.com")

    st.subheader("Visit Us")

    st.markdown("""
    <iframe src="https://www.google.com/maps?q=Delhi&output=embed" 
    width="100%" height="400"></iframe>
    """, unsafe_allow_html=True)

    st.subheader("Send Message")

    name = st.text_input("Your Name")
    message = st.text_area("Your Message")

    if st.button("Submit"):
        st.success("Thanks! We will contact you soon.")
