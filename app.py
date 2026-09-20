import streamlit as st
from PIL import Image

st.set_page_config(page_title="Microstock Helper", page_icon="🖼️")
st.title("🖼️ Microstock Metadata Organizer & Preview")
st.write("Unggah gambar untuk melihat pratinjau karya Anda, lalu rapikan judul dan kata kuncinya secara manual tanpa takut error API.")

# 1. Kotak Upload Foto (Hanya untuk preview gambar)
uploaded_file = st.file_uploader("Pilih gambar karya Anda...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Pratinjau Gambar Anda", use_container_width=True)

st.markdown("---")

# 2. Input Judul
st.subheader("Pengaturan Judul & Kata Kunci")
raw_title = st.text_input("Judul (Title):", "Beautiful landscape photography")

# 3. Input Kata Kunci
raw_keywords = st.text_area("Daftar Kata Kunci (pisahkan dengan koma atau spasi):", "landscape, nature, beautiful, mountain, sky, clouds, scenery")

if st.button("✨ Rapikan dan Hitung Keywords"):
    if raw_keywords:
        words = []
        for line in raw_keywords.replace(',', '\n').split('\n'):
            for word in line.split():
                cleaned = word.strip().lower()
                if cleaned and cleaned not in words:
                    words.append(cleaned)
        
        keyword_count = len(words)
        formatted_keywords = ", ".join(words)
        
        st.success("Berhasil Dirapikan!")
        st.markdown(f"**Total Kata Kunci:** `{keyword_count}` kata")
        
        st.text_input("Judul Final (Siap Salin):", raw_title)
        st.text_area("Kata Kunci Final (Siap Salin):", formatted_keywords, height=150)
        
        if keyword_count > 50:
            st.warning("⚠️ Catatan: Kebanyakan microstock membatasi maksimal 50 kata kunci.")
        else:
            st.info("✅ Jumlah kata kunci aman!")
    else:
        st.error("Masukkan kata kunci terlebih dahulu.")
