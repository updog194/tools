import networking
import netifaces
from scapy.all import ARP, Ether, srp
import requests #to get the ip from http://checkip.dyndns.com/
import socket #socket will also be used for getting private ip address of the machine
from bs4 import BeautifulSoup
########################## imports for network scanning

def getPrivateMachineIP():
    ip = socket.gethostbyname(socket.gethostname());
    return str(ip)
def getPublicIpAddress():
    webrequest = requests.get("http://checkip.dyndns.com/").text;
    soup = BeautifulSoup(webrequest, 'html.parser');
    bodyContent = soup.body.text;
    bC = bodyContent.split(" ");
    return str(bC[3]);
def getDefaultGateWay():
    gateways = netifaces.gateways();
    return gateways['default'][netifaces.AF_INET][0]

def scanNetworkForHosts(gatewayIP):
    print("Scanning for Hosts on network");
    #using scapy to initially send arp requests for host discovery
    #Ether creates a ethernet packet with the braodcasting mac address
    #Arp creates a arp packet with the ip adress
    #the division operator stacks them
    #the srp sends out the packet through layer 2
    results=srp(Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=gatewayIP+"/24"),timeout=2)[0] #note result contains sent AND received variables
    discoveredHosts = [];
    for sent, received in results:
        discoveredHosts.append("IP: " + str(received.psrc) + " | MAC: " + str(received.hwsrc));

    return discoveredHosts;

def main():
    privateIp = getPrivateMachineIP();
    publicIp = getPrivateMachineIP();
    defaultGateway = getDefaultGateWay();
    print(f'private Ip: {privateIp} | public IP: {publicIp} | defaultGateway: {defaultGateway}')
    #get out default network gateway and our private ip
    for host in scanNetworkForHosts(defaultGateway):
        print(host);
    return scanNetworkForHosts(defaultGateway);
    

if __name__=="__main__":
    main();