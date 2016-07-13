# Ethernet to SPI (Raspberry-Pi)

Author: Aditya Kedia

Raspberry pi is a very common choice for IoT projrcts due to its price and form-factor. This Repo contains servers to be run on the Raspberry-Pi which is wired to the SPI device, and clients to be run on several client devices, via several platforms.

Ethernet_to_SPI.py - This repo contains a simple python server that runs on the Raspberry Pi froever. It accepts connections from all TCP clients, gets a bytestring to be writen to the SPI device, writes it, and then sends the SPI response to the TCP client, followed by the stirng "END\n". This is meant to be the starting point for designing a protocol 
