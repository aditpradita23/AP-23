import os
from PIL import Image
import piexif
import google.generativeai as genai

# Konfigurasi API Key AI (Ganti dengan API Key Anda)
genai.configure(api_key="MASUKKAN_GEMINI_API_KEY_ANDA")

def generate_stock_metadata(image_path):
    """Menggunakan AI Vision untuk membuat Judul dan Keyword stock photo"""
    print(f"Menganalisis gambar: {image_path}...")
    
    img = Image.open(image_path)
    
    # Prompt khusus untuk kebutuhan Microstock (Adobe Stock)
    prompt = (
        "Analyze this image for a microstock website like Adobe Stock. "
        "Provide your output strictly in this format:\n"
        "TITLE: [A descriptive, commercial title under 70 characters]\n"
        "KEYWORDS: [15-25 comma-separated relevant keywords, most important first]"
    )
    
    # Memanggil model AI
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content([img, prompt])
    
    text = response.text
    title = ""
    keywords = ""
    
    # Parsing hasil dari AI
    for line in text.split('\n'):
        if line.startswith("TITLE:"):
            title = line.replace("TITLE:", "").strip()
        elif line.startswith("KEYWORDS:"):
            keywords = line.replace("KEYWORDS:", "").strip()
            
    return title, keywords

def embed_metadata_to_image(image_path, title, keywords):
    """Menyematkan Judul dan Keyword ke EXIF/IPTC foto agar terbaca Adobe Stock"""
    img = Image.open(image_path)
    
    # Load EXIF data yang sudah ada (jika ada)
    exif_dict = piexif.load(image_path) if "exif" in img.info else {"0th": {}, "Exif": {}, "GPS": {}, "1st": {}, "thumbnail": None}
    
    # Masukkan Judul ke Tag ImageDescription (0th IFD)
    exif_dict["0th"][piexif.ImageIFD.ImageDescription] = title.encode("utf-8")
    
    # Masukkan Keyword ke Tag XPKeywords (0th IFD) dalam format UTF-16LE
    xp_keywords = keywords.encode("utf-16le") + b'\x00\x00'
    exif_dict["0th"][piexif.ImageIFD.XPKeywords] = xp_keywords
    
    # Simpan kembali metadata ke file gambar
    exif_bytes = piexif.dump(exif_dict)
    img.save(image_path, exif=exif_bytes)
    print(f"Berhasil menyematkan metadata ke: {image_path}\n")

# --- Eksekusi Utama ---
if __name__ == "__main__":
    target_image = "path_to_your_photo.jpg"  # Ganti dengan path foto Anda
    
    if os.path.exists(target_image):
        # 1. Generate Judul & Keyword via AI
        photo_title, photo_keywords = generate_stock_metadata(target_image)
        
        print(f"Judul: {photo_title}")
        print(f"Keywords: {photo_keywords}\n")
        
        # 2. Masukkan ke dalam File Foto
        embed_metadata_to_image(target_image, photo_title, photo_keywords)
    else:
        print("File gambar tidak ditemukan!")
