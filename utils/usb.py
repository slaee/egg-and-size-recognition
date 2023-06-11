import usb.core
import usb.util
import time

class USB:
    def listen_for_devices(self):
        stop = False
        devices = usb.core.find(find_all=True)

        while True:
            # Check if any USB device is connected
            devices = usb.core.find(find_all=True)
            if devices:
                for device in devices:
                    if(self.check_device_capabilities(device)):
                        print(device)
                        print("Device is rewritable and can read files")
                        stop = True
            if stop:
                break
            time.sleep(0.5)

    def check_device_capabilities(self, device: usb.core.Device):
        flag = False
        # Check if the plugged device is rewritable and can read files
        if device is not None:
            # Check if the device supports mass storage class
            if usb.util.find_descriptor(device, bInterfaceClass=8, bInterfaceSubClass=6, bInterfaceProtocol=80):
                print("Device supports Mass Storage Class")
                flag = True
            else:
                print("Device does not support Mass Storage Class")
                flag = False
        else:
            print("No device connected")
            flag = False
        
        return flag
