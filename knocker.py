import os

class color:
    PINK = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

print("""
   ___   ___   ___  ______  __ __ _  __ ____   _____ __ __ ____  ___ 
  / _ \ / _ \ / _ \/_  __/ / //_// |/ // __ \ / ___// //_/|_  / / _ \
 / ___// // // , _/ / /   / ,<  /    // /_/ // /__ / ,<  _/_ < / , _/
/_/    \___//_/|_| /_/   /_/|_|/_/|_/ \____/ \___//_/|_|/____//_/|_| 
""")
print(color.YELLOW+color.BOLD+"By Abhishek S")


try:
    import concurrent.futures 
    from urllib.parse import urlparse
except ImportError:
    print(color.RED+color.BOLD+"This tool is not compatible with your version of python, please use python 3 or above")
    quit()
print(color.GREEN+color.BOLD+"Enter your host (ex: 192.168.137.154) :")
host = input()
print(color.GREEN+color.BOLD+"Enter the port sequence you want to port knock seperated by a space, ex: 2331 1337 3133")
p1,p2,p3 = input().split()
os.system("nmap -Pn --host-timeout 201 --max-retries 0 -p "+ p1 + " " + host)
os.system("nmap -Pn --host-timeout 201 --max-retries 0 -p "+ p2 + " " + host)
os.system("nmap -Pn --host-timeout 201 --max-retries 0 -p "+ p3 + " " + host)
print(color.BLUE+color.BOLD+"KNOCK KNOCK!! THE PORTS ARE KNOCKED - Thank you for using P3RTKN3CKER ")




