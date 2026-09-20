import streamlit as st
from PIL import Image
import google.generativeai as genai

st.set_page_config(page_title="Microstock AI Generator")
st.title("🚀 Microstock AI Caption & Keyword Generator")
st.write("Upload gambar karya Anda, dan AI akan otomatis membaca isinya untuk menghasilkan metadata Adobe Stock & Shutterstock.")

# Mengambil API Key secara aman dari Secrets Streamlit
try:
    api_key = st.secrets["GEMINI_API_KEY"]
    genai.configure(api_key=api_key)
except Exception:
    st.error("API Key belum diatur di Streamlit Secrets. Harap atur terlebih dahulu.")

platform = st.selectbox(
    "Pilih Platform Microstock Tujuan:",
    ["Adobe Stock", "Shutterstock"]
)

max_keywords = 49 if platform == "Adobe Stock" else 50

uploaded_file = st.file_uploader(f"Pilih gambar untuk {platform}...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Gambar yang diunggah", use_container_width=True)

    if st.button("✨ Generate Metadata Otomatis"):
        with st.spinner("AI sedang menganalisis visual gambar Anda..."):
            try:
                # Otomatis mendeteksi model Gemini yang mendukung fitur gambar (vision)
                selected_model_name = 'gemini-1.5-flash'
                for m in genai.list_models():
                    if 'generateContent' in m.supported_generation_methods and 'flash' in m.name.lower():
                        selected_model_name = m.name
                        break
                
                model = genai.GenerativeModel(selected_model_name)

                prompt = f"""
                Analyze this image for a {platform} microstock contributor.
                Provide the output strictly in two sections:
                1. Title: A compelling, commercial, professional title.
                2. Keywords: Exactly {max_keywords} relevant comma-separated keywords.
                """

                response = model.generate_content([prompt, image])

                st.success("Analisis AI Selesai!")
                st.subheader("Hasil Metadata AI:")
                st.write(response.text)

            except Exception as e:
                st.error(f"Terjadi kesalahan: {e}")
