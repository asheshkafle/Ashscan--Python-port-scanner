#!/bin/python
#importing stuff
import sys
import socket
from datetime import datetime
#defining variable
x = 0


#defining target
if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1])#translate hostname to ipv4
else:
    print("Invalid input")
    print("Syntax : pytyhon3 ashscan.py <ip> or ./ashscan <ip>")

#banner
print("Welcome to:")
print("-"*50)
print("ASHSCAN","\n")
print("-"*50)
print("Starting scan on :"+ target)
a = datetime.now()
print("Starting time :" + str(a))
print("="*50,"\n")




#outro
def outro():
    print("="*50)
    print("Exiting program")
    b = datetime.now()
    f = b - a
    print("Time :" + str(b))
    print("Total time taken :" + str(f))
    print("-"*50)


#the important stuff
try:
    for port in range(1,65535):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((target,port))#returns an error indicator
        if result == 0:
            x = 1
            print("port {} is open".format(port))    
            s.close()   
    if x == 0:
        print("There are no open ports")
        s.close()
    print()
    outro()
    

#excecptional cases
except KeyboardInterrupt:
    print("\nKeyboard interruption.")
    outro()
    sys.exit()

except socket.gaierror:
    print("\nHostname could not be resolved")
    outro()
    sys.exit()

except socket.error:
    print("\ncouldn't connect to server")
    outro()
    sys.exit()