import streamlit as st
from rembg import remove
from PIL import Image
from io import BytesIO
import time

# Page config
st.set_page_config(page_title="Creatix Background Remover", layout="wide")

# ------------------ CUSTOM CSS ------------------
st.markdown("""
<style>
/* Main background */
.stApp {
    background-color: #f8fafc;
}

/* Title */
.main-title {
    text-align: center;
    font-size: 48px;
    font-weight: 800;
    color: #0f172a;
    margin-bottom: 10px;
}

/* Subtitle */
.sub-text {
    text-align: center;
    color: #475569;
    font-size: 20px;
    margin-bottom: 40px;
}

/* Upload box */
.upload-box {
    border: 2px dashed #94a3b8;
    padding: 40px;
    border-radius: 18px;
    text-align: center;
    background-color: white;
    font-size: 18px;
}

/* Result cards */
.result-box {
    background-color: white;
    padding: 20px;
    border-radius: 18px;
    text-align: center;
    box-shadow: 0 4px 20px rgba(0,0,0,0.08);
    font-size: 18px;
}

/* Footer */
.footer {
    text-align: center;
    color: #64748b;
    font-size: 14px;
    margin-top: 50px;
}
</style>
""", unsafe_allow_html=True)

# ------------------ HEADER ------------------
st.markdown('<div class="main-title">🎨 Creatix Background Remover</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-text">Upload an image and get instant background removal</div>', unsafe_allow_html=True)

# ------------------ UPLOAD ------------------
st.markdown('<div class="upload-box">', unsafe_allow_html=True)
uploaded_file = st.file_uploader("📂 Drag & Drop or Browse Image", type=["png", "jpg", "jpeg"])
st.markdown('</div>', unsafe_allow_html=True)

# ------------------ PROCESS FUNCTION ------------------
def convert_image(img):
    buf = BytesIO()
    img.save(buf, format="PNG")
    return buf.getvalue()

# ------------------ MAIN LOGIC ------------------
if uploaded_file:
    start = time.time()

    image = Image.open(uploaded_file)
    output = remove(image)

    st.markdown("## Results")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown('<div class="result-box">', unsafe_allow_html=True)
        st.markdown("### Original Image")
        st.image(image, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="result-box">', unsafe_allow_html=True)
        st.markdown("### Background Removed")
        st.image(output, use_container_width=True)
        st.download_button(
            "⬇ Download Image",
            convert_image(output),
            "removed.png",
            "image/png"
        )
        st.markdown('</div>', unsafe_allow_html=True)

    st.success(f"Processed in {round(time.time()-start,2)} sec")

# ------------------ FOOTER ------------------
st.markdown('<div class="footer">Powered by CREATIX.Special Thanks for rembg</div>', unsafe_allow_html=True)