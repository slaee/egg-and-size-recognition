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

imageTextBox = ctk.CTkEntry(liveframe, placeholder_text="Egg health")
imageTextBox.configure(font=("XL", 16))
imageTextBox.place(x=150, y=520, relwidth=0.3, relheight=0.08)

imageSizeTextBox = ctk.CTkEntry(liveframe, placeholder_text="Size")
imageSizeTextBox.configure(font=("XL", 16))
imageSizeTextBox.place(x=420, y=520, relwidth=0.2, relheight=0.08)

captureimage = None
w_pixels = None

def capture_image():
    image_name = imageTextBox.get()
    image_size = imageSizeTextBox.get()
    if image_name != "":
        captureimage.save(f"./datasets/tests/{image_name}-{image_size}-{w_pixels}.png")
        print(f"{image_name}-{image_size}-{w_pixels}.png - SAVED")
    else:
        print("Image not saved")

captureImage = ctk.CTkButton(liveframe, text="Save Egg", command=capture_image)
captureImage.configure(font=("XL", 16))
captureImage.place(x=250, y=600, relwidth=0.3, relheight=0.08)

cap = cv2.VideoCapture(0)
if cap.isOpened():
    while True:
        image = cap.read()[1]
        image = PIL.Image.fromarray(cv2.cvtColor(image, cv2.COLOR_BGR2GRAY))
        width, height = image.size
        left = (width - 400)/2
        top = (height - 400)/2
        right = (width + 400)/2
        bottom = (height + 400)/2
        image = image.crop((left, top, right, bottom))

        captureimage = image

        threshold = np.mean(image)
        above_threshold = image > threshold
        white_pixels = np.sum(above_threshold)

        w_pixels = white_pixels

        # if(np.mean(image) > 10):
        #     print("Egg detected")
        # else:
        #     print("No egg detected")

        photo = PIL.ImageTk.PhotoImage(image)
        camera_feed.configure(image=photo)
        camera_feed.image = photo
    
        # if(np.mean(image) < 115):
        #     print("Egg detected")
        # else:
        #     print("No egg detected")

        
        
        # if np.mean(image) < 70:
        #     threshold = np.mean(image)
        #     above_threshold = image > threshold
        #     size = np.sum(above_threshold)
            
        #     print(size)
        #     print(np.mean(image))
        #     # image = PIL.Image.fromarray(cv2.cvtColor(image, cv2.COLOR_BGR2GRAY))
        #     # width, height = image.size
        #     # left = (width - 400)/2
        #     # top = (height - 400)/2
        #     # right = (width + 400)/2
        #     # bottom = (height + 400)/2
        #     # image = image.crop((left, top, right, bottom))
        #     # photo = PIL.ImageTk.PhotoImage(image)
        #     # camera_feed.configure(image=photo)
        #     # camera_feed.image = photo
        # else:
        #     camera_feed.configure(image=None)
        #     camera_feed.image = None
        #     print("No egg detected in light")
        
        root.update()