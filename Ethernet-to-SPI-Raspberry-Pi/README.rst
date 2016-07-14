Ethernet to SPI - Raspberry pi
====================

:Author: Aditya Kedia

.. contents::


   


Summary
-----------
This repo contains several servers and clients. 
The servers are written in Python, and are meant to run as forever on the Raspberry Pi. They
are meant to accept data from the client and write it to an SPI device, that is connected
to the Pi as a 'slave', and then send the devices response back to the client. The device could be 
anything from a temperature sensor to another MCU. The Wiring Pi library is used for the SPI 
communication.  Read more about the library here: http://wiringpi.com/
Thanks to the library, the communication can easily be changed to I2C, or any other serial 
protocol. Several different types of servers are explored. These can be used as starting point 
to design a custom protocol depending on the needs of the project.

The clients can be writing in various languages to run on several platforms. a few of the clients
demonstrated here are written in python and LabView to be run on operating systems. I will try to 
also include a sample Android client.

Servers:
----------
Ethernet_to_SPI.py
``````````````````
This file contains a simple server based in the socket module in python. It runs on the 
Raspberry-Pi and listens on port 5623. Any suitable TCP client can connect to the server.
The server will accept the connection, read the IP address of the client, and save them to a
logging file with a timestamp. Then it will read a byte string from the client, (maximum 1024
bytes) and send it to the destination sensor or board via SPI. The data read from the device
will be written to the TCP stream, and sent to the client, followed by the string "End\\n". The
server relies on the client to close the connection. However, only a queue of 5 connections
is accepted, so clients will be kicked out if the queue is full.

Use This file as a starting point to design your own protocol for IoT communication.
The major limitation of this server is the inability to maintain several connections at the
same time, because it relies on a single thread to handle all the communication. We will solve
this problem in the upcoming servers in two major ways: Multithreading, and asynchronous 
programming through the Twisted networking library.

Clients:
--------
eth_spi.vi
``````````
This is a client for SPI communications with the Raspberry Pi. It has been implemented as a 
sub-VI (virtual instrument) in LabView. It takes as input the clock rate of SPI communication, 
a chip select bit, the IP address of the destination server and the port, along with a string
of data to be written to the SPI device. It outputs the data read from the server (Raspberry-Pi) as 
a string.
To use this VI with the above servers, one would need to modify the servers slightly, to properly parse
the data relating to the clock rate and chip select, and handle them accordingly. This VI can then be 
introduced into a larger VI that generates the data to be written based on the needs of the project.
