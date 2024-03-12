

import tkinter as tk  
from tkinter import filedialog  
from PIL import Image, ImageTk  
import pytesseract  
import cv2


def preprocess_image(image_path):  
    # Load the image
    image = cv2.imread(image_path)
    
    # Convert to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return gray_image  

def perform_ocr(image):  
    # Perform OCR using Pytesseract  
    extracted_text = pytesseract.image_to_string(image, lang='eng')  
    return extracted_text  

def extract_logo(image_path):
    # Load the image
    image = cv2.imread(image_path)

    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply thresholding
    _, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

    # Find contours
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Find the contour with maximum area (assuming it's the logo)
    max_contour = max(contours, key=cv2.contourArea)

    # Extract the bounding box of the contour
    x, y, w, h = cv2.boundingRect(max_contour)

    # Crop the logo from the image
    logo = image[y:y+h, x:x+w]

    return logo

def process_image():  
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])  
    if file_path:  
        processed_image = preprocess_image(file_path)  
        extracted_text = perform_ocr(processed_image)  
        logo = extract_logo(file_path)

        info_window = tk.Toplevel(root)  
        info_window.title("Extracted Contact Information")  

        text_widget = tk.Text(info_window)  
        text_widget.insert(tk.END, extracted_text)  
        text_widget.config(state=tk.DISABLED)  
        text_widget.pack()  

        if logo is not None:
            logo_image = Image.fromarray(cv2.cvtColor(logo, cv2.COLOR_BGR2RGB))
            logo_photo = ImageTk.PhotoImage(image=logo_image)
            logo_label = tk.Label(info_window, image=logo_photo)
            logo_label.image = logo_photo
            logo_label.pack()  

def open_image():  
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])  
    if file_path:  
        image = Image.open(file_path)  
        image.thumbnail((400, 400))
        img_label.image = ImageTk.PhotoImage(image)  
        img_label.config(image=img_label.image)  

root = tk.Tk()  
root.title("Business Card Reader")  
  
open_button = tk.Button(root, text="Open Image", command=open_image)  
process_button = tk.Button(root, text="Process Image", command=process_image)  

img_label = tk.Label(root)  
img_label.pack()  
open_button.pack()  
process_button.pack()  

root.mainloop()
