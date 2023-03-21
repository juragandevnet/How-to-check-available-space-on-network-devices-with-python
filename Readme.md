This script can help you to check available space on your 1,000 or even million network devices in just a minute.
This script is for multivendor you just need to modify the script, feel free to clone or even modify the script.

Features:
- Checking available space on your network devices.
- for Non-Cisco Devices, please change the command "dir bootflash: " with others vendor command you want to check it.


Requirements:
- import re (for regex purpose)
- import os.path (for checking where is OS image located on your PC/Laptop/Server)
- netmiko (for ssh to devices)
- threading (to run tasks at the same time/simultaneously)

