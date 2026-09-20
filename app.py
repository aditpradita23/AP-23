import streamlit as st

st.set_page_config(page_title="Microstock Helper Sederhana", page_icon="🛠️")
st.title("🛠️ Microstock Metadata Organizer")
st.write("Alat praktis tanpa API Key untuk merapikan, menghitung, dan memformat judul serta kata kunci microstock Anda.")

# 1. Input Judul
st.subheader("1. Pengaturan Judul")
raw_title = st.text_input("Masukkan Judul (Title):", "Beautiful sunset over the calm ocean waves")

# 2. Input Kata Kunci
st.subheader("2. Pengaturan Kata Kunci")
st.write("Tulis atau *paste* kata kunci Anda di bawah ini (bisa dipisah dengan koma, spasi, atau baris baru).")
raw_keywords = st.text_area("Daftar Kata Kunci (Keywords):", "sunset, ocean, beach, nature, wave, water, beautiful, summer, sky, clouds, ocean, sunset")

if st.button("✨ Format dan Rapikan Otomatis"):
    if raw_keywords:
        # Membersihkan dan menghilangkan duplikat kata kunci secara otomatis
        words = []
        for line in raw_keywords.replace(',', '\n').split('\n'):
            for word in line.split():
                cleaned = word.strip().lower()
                if cleaned and cleaned not in words:
                    words.append(cleaned)
        
        keyword_count = len(words)
        formatted_keywords = ", ".join(words)
        
        st.success("Berhasil Dirapikan!")
        
        st.markdown("### Hasil Siap Pakai:")
        
        st.text_input("Judul Final:", raw_title)
        
        st.markdown(f"**Total Kata Kunci:** `{keyword_count}` kata")
        st.text_area("Kata Kunci Final (Comma-Separated):", formatted_keywords, height=150)
        
        if keyword_count > 49:
            st.warning("⚠️ Catatan: Shutterstock/Adobe Stock biasanya membatasi maksimal 50 kata kunci. Sebaiknya kurangi beberapa kata.")
        else:
            st.info("✅ Jumlah kata kunci sudah ideal dan aman!")
    else:
        st.error("Silakan masukkan kata kunci terlebih dahulu.")
