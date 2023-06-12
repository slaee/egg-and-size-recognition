from gui import root, usb_listener_thread

root.mainloop()
usb_listener_thread.join()