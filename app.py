import streamlit as st
from PIL import Image

st.set_page_config(page_title="Microstock AI Generator", page_icon="🚀", layout="centered")

st.title("🚀 Microstock AI Caption & Keyword Generator")
st.write("Pilih platform tujuan Anda, lalu upload karya untuk menghasilkan metadata yang sesuai standar.")

# Menu pilihan platform
platform = st.selectbox(
    "Pilih Platform Microstock Tujuan:",
    ["Adobe Stock", "Shutterstock"]
)

st.info(f"Mode aktif: **{platform}** dipilih. Hasil generate akan disesuaikan dengan aturan algoritma {platform}.")

# Pengaturan tambahan berdasarkan platform
if platform == "Adobe Stock":
    max_keywords = 49
else:
    max_keywords = 50

# Upload file gambar
uploaded_file = st.file_uploader(f"Pilih gambar untuk {platform}...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption=f"Gambar untuk {platform}", use_container_width=True)
    
    st.info(f"Menganalisis gambar untuk {platform}...")
    
    # Simulasi hasil AI
    sample_title = f"Professional stock photo optimized for {platform} featuring creative design"
    sample_keywords = f"stock photo, {platform.lower().replace(' ', '')}, creative, commercial use, professional, high resolution, digital art, vector, background, modern design"

    st.success("Analisis selesai!")
    
    st.subheader(f"Rekomendasi Judul (Title) - {platform}:")
    st.code(sample_title, language="text")
    
    st.subheader(f"Rekomendasi Kata Kunci (Max {max_keywords} Keywords):")
    st.code(sample_keywords, language="text")
    
    st.caption(f"Tip: Format ini sudah disesuaikan dengan standar {platform}.")
