import streamlit as st
from few_shot import FewShotPosts
from post_generator import generate_post

language_options = ["English", "Hinglish"]
length_options = ["Short", "Medium", "Long"]


def main():
    st.set_page_config(
        page_title="LinkedIn Post Generator",
        page_icon="💼",
        layout="centered",
        initial_sidebar_state="expanded",
    )

    # ---------- Custom CSS (LinkedIn blue theme) ----------
    st.markdown(
        """
        <style>
            .stApp {
                background: linear-gradient(180deg, #f3f6f8 0%, #eaf0f5 100%);
            }

            #MainMenu, footer {visibility: hidden;}

            /* Hero header */
            .hero {
                background: linear-gradient(135deg, #0a66c2 0%, #004182 100%);
                padding: 2rem 2.2rem;
                border-radius: 16px;
                color: white;
                margin-bottom: 1.8rem;
                box-shadow: 0 10px 28px rgba(10, 102, 194, 0.28);
                text-align: center;
            }
            .hero h1 {
                font-size: 2rem;
                font-weight: 800;
                margin-bottom: 0.3rem;
                color: white;
            }
            .hero p {
                font-size: 1rem;
                opacity: 0.92;
                margin: 0;
            }

            /* Card container */
            .card {
                background: white;
                border-radius: 14px;
                padding: 1.5rem 1.7rem;
                box-shadow: 0 4px 16px rgba(10, 102, 194, 0.08);
                border: 1px solid rgba(10, 102, 194, 0.08);
                margin-bottom: 1.3rem;
            }

            /* Selectbox labels */
            label {
                font-weight: 600 !important;
                color: #004182 !important;
            }

            div[data-baseweb="select"] > div {
                border-color: #0a66c2 !important;
                border-radius: 8px !important;
            }

            /* Generate button */
            .stButton > button {
                background: linear-gradient(135deg, #0a66c2 0%, #004182 100%);
                color: white;
                font-weight: 700;
                font-size: 1.02rem;
                padding: 0.6rem 1.4rem;
                border: none;
                border-radius: 999px;
                width: 100%;
                box-shadow: 0 6px 16px rgba(10, 102, 194, 0.3);
                transition: transform 0.15s ease;
            }
            .stButton > button:hover {
                transform: translateY(-1px);
                background: linear-gradient(135deg, #004182 0%, #0a66c2 100%);
                color: white;
                border: none;
            }

            /* Generated post card */
            .post-card {
                background: white;
                border-radius: 14px;
                padding: 1.6rem 1.8rem;
                border: 1px solid #d0e3f5;
                border-left: 5px solid #0a66c2;
                box-shadow: 0 4px 16px rgba(10, 102, 194, 0.08);
                white-space: pre-wrap;
                line-height: 1.6;
                color: #1d2226;
            }
            .post-card-title {
                color: #0a66c2;
                font-weight: 700;
                font-size: 1.1rem;
                margin-bottom: 0.8rem;
            }

            /* Sidebar */
            section[data-testid="stSidebar"] {
                background: linear-gradient(180deg, #0a66c2 0%, #004182 100%);
            }
            section[data-testid="stSidebar"] * {
                color: white !important;
            }
            .sidebar-badge {
                display: inline-block;
                background: rgba(255, 255, 255, 0.15);
                padding: 0.35rem 0.9rem;
                border-radius: 999px;
                font-size: 0.85rem;
                font-weight: 600;
                margin-top: 1rem;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )

    # ---------- Sidebar ----------
    with st.sidebar:
        st.markdown("### 📄 About this app")
        st.write(
            "Pick a topic, length, and language, and this app will "
            "generate a ready-to-share LinkedIn post using a few-shot "
            "prompted language model."
        )

        st.markdown("---")
        st.markdown("**Supported languages**")
        st.markdown("- English\n- Hinglish")

        st.markdown("---")
        st.markdown(
            '<div class="sidebar-badge">✨ Built by Rihaab Wadekar</div>',
            unsafe_allow_html=True,
        )

    # ---------- Hero header ----------
    st.markdown(
        """
        <div class="hero">
            <h1>💼 LinkedIn Post Generator</h1>
            <p>Pick a topic, length, and language — get a ready-to-share LinkedIn post in seconds.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    fs = FewShotPosts()

    # ---------- Options card ----------
    st.markdown('<div class="card">', unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)
    with col1:
        selected_tags = st.selectbox("Title", options=fs.get_tags())
    with col2:
        selected_length = st.selectbox("Length", options=length_options)
    with col3:
        selected_language = st.selectbox("Language", options=language_options)

    generate_clicked = st.button("✨ Generate post")
    st.markdown('</div>', unsafe_allow_html=True)

    if generate_clicked:
        with st.spinner("Crafting your LinkedIn post..."):
            post = generate_post(selected_length, selected_language, selected_tags)

        st.markdown(
            f"""
            <div class="post-card">
                <div class="post-card-title">📝 Generated Post</div>
                {post}
            </div>
            """,
            unsafe_allow_html=True,
        )


if __name__ == '__main__':
    main()
