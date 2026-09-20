import streamlit as st
from PIL import Image

st.set_page_config(page_title="Adobe Stock AI Generator", page_icon="📸", layout="centered")

st.title("📸 Adobe Stock AI Caption & Keyword Generator")
st.write("Upload foto atau gambar karya Anda untuk menghasilkan Judul dan Kata Kunci otomatis sesuai standar Adobe Stock.")

# Upload file gambar
uploaded_file = st.file_uploader("Pilih gambar...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Gambar yang diunggah", use_container_width=True)
    
    st.info("Menganalisis gambar...")
    
    # Simulasi hasil AI untuk Judul dan Kata Kunci
    sample_title = "Beautiful digital art of landscape with vibrant colors"
    sample_keywords = "digital art, landscape, vibrant, colors, abstract, cubism, nature, scenic, creative, stock photo, illustration, modern, graphic element, visual, artistic, background, beautiful, bright, colorful, fine art"

    st.success("Analisis selesai!")
    
    st.subheader("Rekomendasi Judul (Title):")
    st.code(sample_title, language="text")
    
    st.subheader("Rekomendasi Kata Kunci (Keywords - 49 Max):")
    st.code(sample_keywords, language="text")
    
    st.caption("Tip: Anda bisa langsung menyalin teks di atas dan menempelkannya ke halaman Adobe Stock Contributor.")
