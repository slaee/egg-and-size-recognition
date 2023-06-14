#!ten_env/bin/python3

from gui import root, usb_listener_thread

if __name__ == "__main__":
    try:
        root.mainloop()
        usb_listener_thread.join()
    except KeyboardInterrupt:
        print("Exiting...")
        exit(0)

