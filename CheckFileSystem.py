import re
import os.path
from netmiko import ConnectHandler
from threading import Thread

def CheckFileSystem(device_type, username, password, ip_address):
    SshCFS = {
        "device_type" : device_type,
        "ip" : ip_address,
        "username" : username,
        "password" : password
    }

    try:
        net_connect = ConnectHandler(**SshCFS)
        host = net_connect.send_command("show run | i hostname")
        hostname = re.search(r"\b(\w+)$", host)
        DeviceSpace = net_connect.send_command("dir bootflash: | i bytes")
        ImageSize = os.path.getsize("C:\juragandevnet\cat9k_iosxe.17.06.04.SPA.bin")
        match = re.search(r"\((\d+) bytes free\)", DeviceSpace)

        ### IF SELECTION TO CHECK WHETHER THE DEVICE HAS AN AVAILABLE SPACE FOR THE OS IMAGE OR NOT ###
        if int(match.group(1)) < ImageSize:
            print(hostname.group(1) + " = Not Enough Space On Device")
        else:
            print(hostname.group(1) + " = Space Is Available On Device")

    except Exception:
        print("Check your Network Connection, make sure you can SSH to", ip_address)

### READ FILE ###
f = open("devices.txt", "r")

threads=[]
threads = [Thread(target=CheckFileSystem, args=("cisco_ios", "admin", "devnet!123", ip_address)) for ip_address in f.readlines()]
for thread in threads:
    thread.start()
for thread in threads:
    thread.join()