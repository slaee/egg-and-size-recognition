import pyudev

class USBUtil:
    def __init__(self):
        self.context = pyudev.Context()
        self.status = False

    def listen(self):
        monitor = pyudev.Monitor.from_netlink(self.context)
        monitor.filter_by(subsystem='usb')
        monitor.start()

        # Iterate over the devices to find the flash drive
        for device in iter(monitor.poll, None):
            # check if the ID_MODEL contains "Flash" word
            try:
                if device.get('ID_MODEL') == "USB_Flash_Disk":
                    self.status = True
                else:
                    self.status = False
            except IOError:
                self.status = False
                print("Flash drive is not readable or writable.")