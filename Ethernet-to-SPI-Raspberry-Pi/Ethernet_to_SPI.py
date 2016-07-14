# -*- coding: utf-8 -*-
"""
Created on Wed Jun 15 10:06:42 2016 
@author: adi

"""
 
 
import socket
import wiringpi
 

port =5623
host = ''
buff=1024
wiringpi.wiringPiSetupGpio()
wiringpi.wiringPiSPISetup(0, 500000) 

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
s.listen(5)
 
while True:
    conn, addr =s.accept()
    print("connected to: ", addr)
    talk=conn.recv(1024)
    print("message from client:", talk)
    print("writing to SPI")
    data = talk
    recv = wiringpi.wiringPiSPIDataRW(0, data)
    print("SPI device says: ", recv)
    conn.send(str(recv).encode())
    conn.send('End\n'.encode())
