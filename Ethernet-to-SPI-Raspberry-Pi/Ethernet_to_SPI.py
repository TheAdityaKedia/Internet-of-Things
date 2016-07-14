# -*- coding: utf-8 -*-
"""
Created on Wed Jun 15 10:06:42 2016 
@author: adi

"""
 
 
import socket
import wiringpi
from time import ctime, sleep
 

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
    to_write =  ctime()+" - connected to: "+ addr[0] + " on port "+str(addr[1])+"\n" 
    with open('connection-log.txt', 'a+') as f:
        f.write(to_write)
    talk=conn.recv(1024)
    to_write = ctime()+" - Message from client: \'"+ talk.decode() + "\'\n" 
    with open('connection-log.txt', 'a+') as f:
        f.write(to_write)
        to_write = ctime()+" - Writing to SPI\n"
        f.write(to_write)
    data = talk
    recv = wiringpi.wiringPiSPIDataRW(0, data)
    to_write = ctime()+" - Received from SPI device: \'"+ str(recv)+ "\'\n" 
    with open('connection-log.txt', 'a+') as f:
        f.write(to_write)
        to_write = ctime()+" - sending response to client: \'"+ str(recv)+ "\'\n"
        f.write(to_write)
    conn.send(str(recv).encode())
    conn.send('End\n'.encode())
    sleep(1)
    conn.close()
    to_write = ctime()+" - connection to "+ addr[0] + " closed\n"
    with open('connection-log.txt', 'a+') as f:
        f.write(to_write)
