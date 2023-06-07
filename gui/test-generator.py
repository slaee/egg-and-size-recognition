import cv2
import customtkinter as ctk
import PIL.Image
import PIL.ImageTk
import numpy as np

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

root = ctk.CTk()
root.geometry("800x700")

liveframe = ctk.CTkFrame(root)
liveframe.pack(pady=10, padx=10, fill="both", expand=True)

camera_feed = ctk.CTkLabel(liveframe, text="")
camera_feed.pack(pady=10, padx=10)


imageTextBox = ctk.CTkEntry(liveframe, placeholder_text="Image Name")
imageTextBox.configure(font=("XL", 16))
imageTextBox.place(x=250, y=520, relwidth=0.3, relheight=0.08)

captureImage = ctk.CTkButton(liveframe, text="Capture Image")
captureImage.configure(font=("XL", 16))
captureImage.place(x=250, y=600, relwidth=0.3, relheight=0.08)

cap = cv2.VideoCapture(0)

def adjust_saturation_contrast(image, saturation_factor, contrast_factor):
    # Convert the image to the HSV color space
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # Adjust the saturation channel
    hsv_image[:, :, 1] = np.clip(hsv_image[:, :, 1] * saturation_factor, 0, 255).astype(np.uint8)

    # Convert the image back to the BGR color space
    adjusted_image = cv2.cvtColor(hsv_image, cv2.COLOR_HSV2BGR)

    # Adjust the contrast using cv2.convertScaleAbs
    adjusted_image = cv2.convertScaleAbs(adjusted_image, alpha=contrast_factor)

    return adjusted_image

while True:
    image = cap.read()[1]
    # # grayscale
    # # image = cv2.convertScaleAbs(image.astype(float), alpha=0.5, beta=-20)
    # image = adjust_saturation_contrast(image, 1.5, 0.5)
    image = PIL.Image.fromarray(cv2.cvtColor(image, cv2.COLOR_BGR2GRAY))
    # image = PIL.Image.fromarray(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    width, height = image.size
    left = (width - 370)/2
    top = (height - 370)/2
    right = (width + 370)/2
    bottom = (height + 370)/2
    image = image.crop((left, top, right, bottom))
    photo = PIL.ImageTk.PhotoImage(image)
    camera_feed.configure(image=photo)
    camera_feed.image = photo
    root.update()


