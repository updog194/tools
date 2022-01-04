#HAND-MADE IMPORTS
#import hostServer
import networkScanner
import portTest
#PYTHON LIBARIES
import time
import threading
import contextlib
import sys
import os

def getHosts():
    return networkScanner.main();

def readPortsFile():
    with open("portScanLogs.txt", "r") as pFile:
        targetAndPorts = pFile.readlines();
        return targetAndPorts;

if(__name__=="__main__"):
    activeHostsIPs = [];

    for host in getHosts():
        hostItems = host.split();
        activeHostsIPs.append(hostItems[1]);

    mainPorts = [20, 21, 22, 25, 26,31,32,42, 53, 80, 123, 179, 443, 500, 3389, 14200];
    for host in activeHostsIPs:
        newPortScanThread = threading.Thread(target=portTest.find_ports, args=(host,mainPorts,));
        newPortScanThread.start();

    time.sleep(10);
    for tp in readPortsFile():
        print(tp);  
