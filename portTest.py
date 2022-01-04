import socket

def find_ports(target, portRange):
    openPorts = [];
    for port in portRange:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
        sock.settimeout(1);
        try:
            checkPort = sock.connect_ex((target, port));
            if(checkPort == 0):
                openPorts.append(checkPort);
                with open("portScanLogs.txt", "a") as portFile:
                    portFile.writelines(str(target) + ":" + str(port) + "\n");
        except:
            pass;
        sock.close();
    return openPorts;
        
