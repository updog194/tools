 
import sys
import socket
import pyfiglet
import os

#Global variables set as arguments
target = "";
portRange = range(0, 1);
#ports able to be connected to
openPorts = [];

def getArguments():
    global target;
    global portRange;
    if(len(sys.argv) != 4):
        print("invalid arguments");
        print("Arguments should be <target> <lowest port to scan> <highest port to scan>")
        print("EX: portScanner.py x.x.x.x x xx");
        sys.exit();
    target = sys.argv[1];
    portRange = range(int(sys.argv[2]), int(sys.argv[3]));

def testTCPConnect(target, port):
    global openPorts;
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1); #note this line is meant for passing if more than half of second of time passes
        print("Testing port: " + str(port));
        testCon = sock.connect_ex((target, port));
        if(testCon == 0):
            openPorts.append(port);
            pass;
        sock.close();
    except Exception as err:
        pass;

def testPorts():
    global portRange;
    global target;
    global openPorts;
    for port in portRange:
        testTCPConnect(target, port);
    os.system("cls");
    portBanner = pyfiglet.figlet_format("--PORTS--");
    print(portBanner);
    for openPort in openPorts:
        print("PORT: [" + str(openPort) + "]");

if __name__=="__main__":
    getArguments();
    testPorts();
