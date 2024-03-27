import cv2
from PIL import Image
import pytesseract
import io

# Load gambar
image = cv2.imread('1.png')

# Mengecilkan karakter pada gambar
scale_percent = 60  # Ubah sesuai kebutuhan
width = int(image.shape[1] * scale_percent / 100)
height = int(image.shape[0] * scale_percent / 100)
dim = (width, height)
resized_image = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)

# Ubah gambar OpenCV ke format PIL
pil_image = Image.fromarray(resized_image)

# Ubah ke grayscale
gray = pil_image.convert('L')

# Thresholding
_, thresh = cv2.threshold(cv2.cvtColor(resized_image, cv2.COLOR_BGR2GRAY), 150, 255, cv2.THRESH_BINARY_INV)

# Deteksi kontur
contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Inisialisasi list untuk menyimpan teks dari setiap kotak
box_texts = []

# Loop over each contour
for contour in contours:
    # Dapatkan bounding box untuk setiap kontur
    x, y, w, h = cv2.boundingRect(contour)
    
    # Resize bounding box coordinates
    x = int(x * scale_percent / 100)
    y = int(y * scale_percent / 100)
    w = int(w * scale_percent / 100)
    h = int(h * scale_percent / 100)
    
    # Potong kotak dari gambar
    box_image = resized_image[y:y+h, x:x+w]
    
    # Simpan gambar ke dalam aliran byte
    img_byte_arr = io.BytesIO()
    Image.fromarray(cv2.cvtColor(box_image, cv2.COLOR_BGR2RGB)).save(img_byte_arr, format='PNG')
    
    # Atur pointer aliran byte ke awal
    img_byte_arr.seek(0)
    
    # Gunakan pytesseract untuk mengenali teks dalam kotak
    text = pytesseract.image_to_string(Image.open(img_byte_arr), lang='eng', config='--psm 6')
    
    # Tambahkan teks ke dalam list
    box_texts.append(text)

# Gabungkan teks dari semua kotak
full_text = '\n'.join(box_texts)

# Tampilkan hasil
print("Full Text:")
print(full_text)
