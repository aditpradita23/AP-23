import streamlit as st
from PIL import Image

st.set_page_config(page_title="Microstock AI Generator", page_icon="🚀", layout="centered")

st.title("🚀 Microstock AI Caption & Keyword Generator")
st.write("Pilih platform tujuan Anda, atur kategori, lalu upload karya untuk menghasilkan metadata.")

# Menu pilihan platform di bagian utama atau sidebar
platform = st.selectbox(
    "Pilih Platform Microstock Tujuan:",
    ["Adobe Stock", "Shutterstock"]
)

st.info(f"Mode aktif: **{platform}** dipilih.")

# Pengaturan tambahan: Kategori dan Jenis Aset
st.subheader("⚙️ Detail Aset")
col1, col2 = st.columns(2)

with col1:
    asset_type = st.selectbox(
        "Jenis Aset:",
        ["Photo (Foto)", "Illustration (Ilustrasi)", "Vector (Vektor)", "3D Render"]
    )

with col2:
    category = st.selectbox(
        "Kategori Utama:",
        [
            "Animals (Hewan)",
            "Architecture (Arsitektur)",
            "Business (Bisnis)",
            "Food (Makanan)",
            "Landscapes (Pemandangan)",
            "People (Orang)",
            "Nature (Alam)",
            "Technology (Teknologi)"
        ]
    )

# Aturan batas keyword berdasarkan platform
max_keywords = 49 if platform == "Adobe Stock" else 50

# Upload file gambar
uploaded_file = st.file_uploader(f"Pilih gambar untuk {platform}...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption=f"Gambar ({asset_type} - {category})", use_container_width=True)
    
    st.info(f"Menganalisis gambar untuk {platform}...")
    
    # Hasil simulasi AI berdasarkan pilihan kategori & jenis
    clean_category = category.split(" ")[0].lower()
    clean_type = asset_type.split(" ")[0].lower()
    
    sample_title = f"Professional {clean_type} depicting {clean_category} for commercial and creative projects on {platform}"
    sample_keywords = f"{clean_category}, {clean_type}, stock photo, commercial use, creative, professional design, high resolution, digital asset, marketing, background"

    st.success("Analisis selesai!")
    
    st.subheader(f"Rekomendasi Judul (Title) - {platform}:")
    st.code(sample_title, language="text")
    
    st.subheader(f"Rekomendasi Kata Kunci (Max {max_keywords} Keywords):")
    st.code(sample_keywords, language="text")
    
    st.caption(f"Tip: Metadata ini telah disesuaikan dengan kategori {category} untuk standar {platform}.")
