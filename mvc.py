from sqlAlch2 import session
from class_sqlalch import Device1, Base

class Device:

    ipAddress = ""
    port = ""
    
    def findDevices():
        devices = session.query(Device1.ipAddress,Device1.port)\
                        .filter(Device1.ipAddress.like('10%'))
        return devices

class DevicesView:

    def showDevices(self,devices):
        for d in devices:
            print('-------')
            print('IP Address:', d.ipAddress)
            print('Port:', d.port)

class DevicesController:

    def __init__(self):
        self.devices = Device.findDevices()

        v = DevicesView()
        v.showDevices(self.devices)

c = DevicesController()