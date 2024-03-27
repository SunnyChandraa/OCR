# import pytesseract
# import PIL.Image
# import cv2
# import re, locale

# img_command_config = r"--psm 6 --oem 3"

# text = pytesseract.image_to_string(PIL.Image.open("1.png"), config=img_command_config)
# parse = re.sub(r'[\W_]+', '', text)
# print(parse)

# import cv2
# import pytesseract
# import re, locale

# # Load gambar
# image = cv2.imread('1.png')

# # Praproses gambar
# gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# gray = cv2.medianBlur(gray, 3)
# gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

# cv2.imshow('threshold image', image)

# # Gunakan pytesseract untuk mengenali teks
# custom_config = r'--oem 3 --psm 6'
# text = pytesseract.image_to_string(gray, config=custom_config)
# parse = re.sub(r'[\W_]+', '', text)
# print(text)


import cv2
import numpy as np
import pytesseract
import re, locale
#pytesseract.pytesseract.tesseract_cmd = r'D:\Program Files\pytesseract\tesseract.exe'
path_to_image = "1.png"
#path_to_image = "logo1.png"
image = cv2.imread(path_to_image)
h, w, _ = image.shape
w*=2; h*=2
w = (int)(w); h = (int) (h)
image = cv2.resize(image, (w,h), interpolation = cv2.INTER_AREA) #Resize 
# converting image into gray scale image
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow('grey image', gray_image)
cv2.waitKey(0)
# converting it to binary image by Thresholding
# this step is require if you have colored image because if you skip this part
# then tesseract won't able to detect text correctly and this will give incorrect result
#threshold_img = cv2.threshold(gray_image, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
# display image
threshold_img = cv2.adaptiveThreshold(gray_image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
            cv2.THRESH_BINARY,13,3) 
cv2.imshow('threshold image', threshold_img)            
cv2.waitKey(0)
#threshold_img = cv2.GaussianBlur(threshold_img,(3,3),0)
#threshold_img = cv2.GaussianBlur(threshold_img,(3,3),0)
threshold_img = cv2.medianBlur(threshold_img,5)
cv2.imshow('medianBlur', threshold_img)            
cv2.waitKey(0)

threshold_img  = cv2.bitwise_not(threshold_img)
cv2.imshow('Invert', threshold_img)            
cv2.waitKey(0)

cv2.imshow('threshold image', threshold_img)

# Maintain output window until user presses a key
cv2.waitKey(0)

# Destroying present windows on screen
cv2.destroyAllWindows()
# now feeding image to tesseract
custom_config = r"--psm 6 --oem 3"         
text = pytesseract.image_to_string(threshold_img, config=custom_config) 
parse = re.sub(r'[\W_]+', '', text)
print(parse)