import customtkinter as ctk
from utils import USBUtil
import threading

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

root = ctk.CTk()

liveframe = ctk.CTkFrame(root)
liveframe.pack(pady=10, padx=10, fill="both", expand=True)
liveframe.place(x=20, y=20, relwidth=0.7, relheight=0.96)

jlabel = ctk.CTkLabel(liveframe, text="JUMBO:")
jlabel.configure(font=("XL", 64))
jlabel.place(x=40, y=20)

jvalue = ctk.CTkLabel(liveframe, text="0")
jvalue.configure(font=("XL", 64))
jvalue.place(x=300, y=20)

xllabel = ctk.CTkLabel(liveframe, text="XL:")
xllabel.configure(font=("XL", 64))
xllabel.place(x=40, y=140)

xlvalue = ctk.CTkLabel(liveframe, text="0")
xlvalue.configure(font=("XL", 64))
xlvalue.place(x=300, y=140)

llabel = ctk.CTkLabel(liveframe, text="L:")
llabel.configure(font=("XL", 64))
llabel.place(x=40, y=260)

lvalue = ctk.CTkLabel(liveframe, text="0")
lvalue.configure(font=("XL", 64))
lvalue.place(x=300, y=260)

mlabel = ctk.CTkLabel(liveframe, text="M:")
mlabel.configure(font=("XL", 64))
mlabel.place(x=40, y=380)

mvalue = ctk.CTkLabel(liveframe, text="0")
mvalue.configure(font=("XL", 64))
mvalue.place(x=300, y=380)

slabel = ctk.CTkLabel(liveframe, text="S:")
slabel.configure(font=("XL", 64))
slabel.place(x=40, y=500)

svalue = ctk.CTkLabel(liveframe, text="0")
svalue.configure(font=("XL", 64))
svalue.place(x=300, y=500)

xslabel = ctk.CTkLabel(liveframe, text="PEWEE:")
xslabel.configure(font=("XL", 64))
xslabel.place(x=40, y=620)

xsvalue = ctk.CTkLabel(liveframe, text="0")
xsvalue.configure(font=("XL", 64))
xsvalue.place(x=300, y=620)

rlabel = ctk.CTkLabel(liveframe, text="REJECT:")
rlabel.configure(font=("XL", 64))
rlabel.place(x=40, y=740)

rvalue = ctk.CTkLabel(liveframe, text="0")
rvalue.configure(font=("XL", 64))
rvalue.place(x=300, y=740)

usbstatus = ctk.CTkLabel(liveframe, text="No Flash Drive connected")
usbstatus.configure(font=("XL", 32))
usbstatus.configure(fg_color="red")
usbstatus.place(x=650, y=20, relwidth=0.4)

infousb = ctk.CTkLabel(liveframe, text="(Please insert a Flash Drive to save your data.)")
infousb.configure(font=("XL", 16))
infousb.place(x=690, y=60)

usb_manager = USBUtil()

def update_usb_status():
    if usb_manager.status:
        usbstatus.configure(text="Flash Drive connected")
        usbstatus.configure(fg_color="limegreen")
        infousb.configure(text="(Your data will be saved to the Flash Drive.)")
    else:
        usbstatus.configure(text="No Flash Drive connected")
        usbstatus.configure(fg_color="red")
        infousb.configure(text="(Please insert a Flash Drive to save your data.)")
    root.after(1000, update_usb_status)

def run_usb_listener():
    usb_manager.listen()
    root.after(0, update_usb_status)

# Create and start the thread
usb_listener_thread = threading.Thread(target=run_usb_listener)
usb_listener_thread.start()

def check_usb_status():
    update_usb_status()
    # Check again after 1 second (adjust the interval as needed)
    root.after(1000, check_usb_status)

check_usb_status()


startbtn = ctk.CTkButton(root, text="START")
startbtn.configure(font=("XL", 24))
startbtn.configure(fg_color="limegreen")
startbtn.configure(hover_color="green")
startbtn.place(x=1170, y=20, relwidth=0.25, relheight=0.1)

stopbtn = ctk.CTkButton(root, text="STOP")
stopbtn.configure(font=("XL", 24))
stopbtn.configure(fg_color="red")
stopbtn.configure(hover_color="darkred")
stopbtn.place(x=1170, y=140, relwidth=0.25, relheight=0.1)


# full screen
root.attributes("-fullscreen", True)
