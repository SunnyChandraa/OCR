import pytesseract
import PIL.Image
import cv2

img_command_config = r"--psm 6 --oem 3"

text = pytesseract.image_to_string(PIL.Image.open("1.png"), config=img_command_config)
print(text)
