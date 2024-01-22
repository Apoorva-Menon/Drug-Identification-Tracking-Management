import cv2
import pytesseract
import tkinter as tk
from tkinter import filedialog

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe' #Link to the tesseract executable installed
root = tk.Tk()
root.withdraw()

print("Select the image")
img_name = filedialog.askopenfilename()    # to select the image from the file explorer
img = cv2.imread(img_name)
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)  # color conversion from rgb to bgr color scheme
print(pytesseract.image_to_string(img))    # recognizing text from the image and print

#Detecting Word Locations
hImg,wImg,xImg = img.shape
boxes = pytesseract.image_to_data(img)     # converting the tesseract image to data
for x,b in enumerate(boxes.splitlines()):
    if x!=0:
        b = b.split()
        if len(b)==12:                     # selecting the rows with identified words
            x,y,w,h = int(b[6]),int(b[7]),int(b[8]),int(b[9])   # identifying corners of the location of every identified word
            cv2.rectangle(img,(x,y),(w+x,h+y),(0,0,255),1)      # creating a box around every found word
cv2.imshow('Result',img)                   # displaying the image with the boxes
cv2.waitKey(0)