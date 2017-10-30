"""
Infinite loop to freeze the batch container until the kafka and ES containers are running

code adapted from the following source:

Author: deployeveryday.com
Date: 9/12/2016
URL: http://deployeveryday.com/2016/09/12/race-condition-docker-compose.html
"""


import socket
import time
import argparse

# use argparse library to read in command line arguments with flags
parser = argparse.ArgumentParser()
parser.add_argument('--service-name', required=True)
parser.add_argument('--ip', required=True)
parser.add_argument('--port', required=True)

args = parser.parse_args()

service_name = str(args.service_name)
port = int(args.port)
ip = str(args.ip)

# stall while the given container is not running
while True:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex((ip, port))
    if result == 0:
        print("{0} port is open".format(service_name))
        break
    else:
        print("{0} port is not open".format(service_name))
        time.sleep(5)
