import pyudev
import re
import os
import traceback

class USBUtil:
    def __init__(self):
        self.context = pyudev.Context()
        self.device = None
        self.status = False

    def listen(self):
        monitor = pyudev.Monitor.from_netlink(self.context)
        monitor.filter_by(subsystem='usb')
        monitor.start()

        pattern = re.compile(r'(Flash|Storage|Disk)', re.IGNORECASE)

        for device in iter(monitor.poll, None):
            id_model = device.get('ID_MODEL')
            if id_model is not None and pattern.search(id_model):
                self.status = self.is_device_readable_and_writable(device.device_node)
            else:
                self.status = False

    def check_initial_status(self):
        pattern = re.compile(r'(Flash|Storage|Disk)', re.IGNORECASE)
        for device in self.context.list_devices(subsystem='usb'):
            id_model = device.get('ID_MODEL')
            if id_model is not None and pattern.search(id_model):
                self.status = self.is_device_readable_and_writable(device.device_node)
                break
            else:
                self.status = False

    def is_device_readable_and_writable(self, device_node):
        fd = None
        try:
            fd = os.open(device_node, os.O_RDWR)
            with os.fdopen(fd, 'rb') as f:
                data = f.read(512)
                f.close()

                f = open(device_node, 'rb+')
                f.write(b'Write some data to the flash drive')

                self.device = device_node
                return True
        except IOError as e:
            traceback.print_exc()
            return False
        finally:
            if fd is not None:
                os.close(fd)