import streamlit as st
from PIL import Image
import google.generativeai as genai

st.set_page_config(page_title="Microstock AI Generator", page_icon="🚀", layout="centered")

st.title("🚀 Microstock AI Caption & Keyword Generator")
st.write("Upload gambar karya Anda, dan AI akan otomatis membaca isinya untuk menghasilkan metadata Adobe Stock & Shutterstock.")

st.sidebar.header("🔑 Konfigurasi AI")
api_key = st.sidebar.text_input("Masukkan Google Gemini API Key:", type="password")

platform = st.selectbox(
    "Pilih Platform Microstock Tujuan:",
    ["Adobe Stock", "Shutterstock"]
)

max_keywords = 49 if platform == "Adobe Stock" else 50

uploaded_file = st.file_uploader(f"Pilih gambar untuk {platform}...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Gambar yang diunggah", use_container_width=True)
    
    if not api_key:
        st.warning("⚠️ Masukkan Google Gemini API Key Anda terlebih dahulu di menu sidebar untuk mulai menganalisis gambar secara otomatis.")
    else:
        if st.button("✨ Generate Metadata Otomatis"):
            with st.spinner("AI sedang menganalisis visual gambar Anda..."):
                try:
                    genai.configure(api_key=api_key)
                    # Menggunakan model standar gemini-pro-vision atau gemini-flash
                    model = genai.GenerativeModel('gemini-1.5-flash-latest')
                    
                    prompt = f"""
                    Analyze this image for a {platform} microstock contributor. 
                    Provide the output strictly in two sections:
                    1. Title: A compelling, commercial, professional title (around 10-15 words).
                    2. Keywords: Exactly {max_keywords} relevant comma-separated keywords, ordered from most important to least important, no numbers, just keywords.
                    """
                    
                    response = model.generate_content([prompt, image])
                    
                    st.success("Analisis AI Selesai!")
                    st.subheader("Hasil Metadata AI:")
                    st.write(response.text)
                    
                except Exception as e:
                    st.error(f"Terjadi kesalahan: {e}")
