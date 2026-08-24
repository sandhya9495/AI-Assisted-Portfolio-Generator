import streamlit as st
import webbrowser
from pathlib import Path

from input_handler import read_uploaded_resume
from gemini import generate_resume_json
from html_generator import generate_portfolio


BASE_DIR = Path(__file__).parent
PROFILE_FILE = BASE_DIR / "profile.jpg"


st.set_page_config(
    page_title="AI Portfolio Builder",
    page_icon="💼",
    layout="wide",
    initial_sidebar_state="collapsed"
)


st.markdown(
    """
    <style>

    .stApp {
        background:
            radial-gradient(circle at 10% 20%, rgba(59,130,246,0.20), transparent 28%),
            radial-gradient(circle at 90% 10%, rgba(168,85,247,0.25), transparent 30%),
            radial-gradient(circle at 80% 90%, rgba(236,72,153,0.18), transparent 30%),
            linear-gradient(135deg, #020617 0%, #071a3d 45%, #160b35 100%);
        color: white;
    }

    [data-testid="stHeader"] {
        background: transparent;
    }

    .block-container {
        max-width: 1050px;
        padding-top: 55px;
        padding-bottom: 40px;
    }

    .main-title {
        text-align: center;
        font-size: 56px;
        font-weight: 800;
        margin-bottom: 8px;
        background: linear-gradient(
            90deg,
            #60a5fa,
            #a855f7,
            #ec4899
        );
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }

    .subtitle {
        text-align: center;
        color: #dbeafe;
        font-size: 16px;
        margin-bottom: 45px;
    }

    .upload-card {
        background: rgba(255,255,255,0.08);
        border: 1px solid rgba(255,255,255,0.16);
        border-radius: 22px;
        padding: 28px 25px;
        height: 215px;
        box-shadow: 0 15px 45px rgba(0,0,0,0.25);
        backdrop-filter: blur(15px);
        text-align: center;
    }

    .upload-icon {
        width: 58px;
        height: 58px;
        border-radius: 18px;
        margin: 0 auto 15px auto;
        display: flex;
        align-items: center;
        justify-content: center;
        background: linear-gradient(
            135deg,
            #3b82f6,
            #8b5cf6
        );
        font-size: 29px;
    }

    .upload-title {
        color: white;
        font-size: 21px;
        font-weight: 700;
        margin-bottom: 8px;
    }

    .upload-description {
        color: #cbd5e1;
        font-size: 14px;
    }

    [data-testid="stFileUploader"] {
        background: rgba(2,6,23,0.25);
        border: 1px dashed rgba(147,197,253,0.55);
        border-radius: 16px;
        padding: 8px;
        margin-top: 2px;
    }

    [data-testid="stFileUploader"] section {
        background: transparent !important;
    }

    [data-testid="stFileUploader"] small {
        color: #cbd5e1 !important;
    }

    [data-testid="stFileUploader"] span {
        color: #e2e8f0 !important;
    }

    [data-testid="stFileUploader"] button {
        background: linear-gradient(
            90deg,
            #3b82f6,
            #8b5cf6
        ) !important;
        color: white !important;
        border: none !important;
        border-radius: 9px !important;
        font-weight: 600 !important;
    }

    [data-testid="stFileUploader"] button:hover {
        background: linear-gradient(
            90deg,
            #2563eb,
            #7c3aed
        ) !important;
    }

    [data-testid="stFileUploaderDropzone"] {
        background: transparent !important;
    }

    .stButton {
        margin-top: 30px;
    }

    .stButton > button {
        width: 100%;
        height: 55px;
        border: none;
        border-radius: 13px;
        color: white;
        font-size: 17px;
        font-weight: 700;
        background: linear-gradient(
            90deg,
            #3b82f6,
            #8b5cf6,
            #ec4899
        );
        box-shadow: 0 12px 35px rgba(139,92,246,0.35);
        transition: all 0.3s ease;
    }

    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 16px 45px rgba(139,92,246,0.55);
    }

    .selected-text {
        text-align: center;
        color: #86efac;
        font-size: 13px;
        font-weight: 600;
        margin-top: 8px;
    }

    .optional-text {
        text-align: center;
        color: #94a3b8;
        font-size: 12px;
        margin-top: 5px;
    }

    .security-text {
        text-align: center;
        color: #94a3b8;
        font-size: 12px;
        margin-top: 25px;
    }

    </style>
    """,
    unsafe_allow_html=True
)


st.markdown(
    '<div class="main-title">AI Portfolio Builder</div>',
    unsafe_allow_html=True
)


st.markdown(
    '<div class="subtitle">'
    'Upload your resume and profile photo to generate a professional portfolio.'
    '</div>',
    unsafe_allow_html=True
)


col1, col2 = st.columns(2, gap="large")


with col1:

    st.markdown(
        '<div class="upload-card">'
        '<div class="upload-icon">📄</div>'
        '<div class="upload-title">Upload Resume</div>'
        '<div class="upload-description">'
        'TXT, PDF or DOCX'
        '</div>'
        '</div>',
        unsafe_allow_html=True
    )

    resume_file = st.file_uploader(
        "Resume",
        type=["txt", "pdf", "docx"],
        label_visibility="collapsed"
    )

    if resume_file is not None:
        st.markdown(
            '<div class="selected-text">✓ Resume selected</div>',
            unsafe_allow_html=True
        )


with col2:

    st.markdown(
        '<div class="upload-card">'
        '<div class="upload-icon">🖼️</div>'
        '<div class="upload-title">Upload Profile Photo</div>'
        '<div class="upload-description">'
        'JPG, JPEG or PNG'
        '</div>'
        '</div>',
        unsafe_allow_html=True
    )

    profile_image = st.file_uploader(
        "Profile Photo",
        type=["jpg", "jpeg", "png"],
        label_visibility="collapsed"
    )

    if profile_image is not None:
        st.markdown(
            '<div class="selected-text">✓ Profile photo selected</div>',
            unsafe_allow_html=True
        )
    else:
        st.markdown(
            '<div class="optional-text">Optional</div>',
            unsafe_allow_html=True
        )


if st.button(
    "✨ Generate My Portfolio",
    type="primary",
    use_container_width=True
):

    if resume_file is None:
        st.error("Please upload your resume first.")
        st.stop()

    try:

        with st.spinner("Reading your resume..."):
            resume_text = read_uploaded_resume(resume_file)

        with st.spinner("🤖 AI is creating your portfolio..."):
            portfolio_data = generate_resume_json(resume_text)

        if profile_image is not None:

            with st.spinner("🖼️ Saving profile photo..."):

                image_bytes = profile_image.getvalue()

                with open(PROFILE_FILE, "wb") as file:
                    file.write(image_bytes)

        with st.spinner("🌐 Building your portfolio..."):

            generated_file = generate_portfolio(
                portfolio_data,
                str(PROFILE_FILE) if profile_image is not None else None
            )

        generated_path = Path(generated_file).resolve()

        webbrowser.open_new_tab(
            generated_path.as_uri()
        )

        st.success(
            "🎉 Portfolio generated! Opening your portfolio..."
        )

    except Exception as error:

        st.error(
            "Something went wrong while generating the portfolio."
        )

        st.write(str(error))


st.markdown(
    '<div class="security-text">'
    '🔒 Your resume is processed locally and used only to generate your portfolio.'
    '</div>',
    unsafe_allow_html=True
)