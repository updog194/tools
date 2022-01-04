import subprocess;
import requests;
import io;
import time;
import os;
import threading;
import sys;

running = True;
dirsFound = ["/"];

def dirSearcher(checkForFilesInp):
    global running

    if(len(sys.argv) != 2):
        print("Inccorect Usage")
        print("EX: python <python.py> url");
        print("Include FULL url path | EX: https://www.google.com/");
        sys.exit();
    file = open("/wordlists/wordlist2.txt", "r");
    dirList = file.readlines();

    for dir in dirList:
        if(checkForFilesInp != ""):
            dir = dir.strip() + checkForFilesInp;
        dir_enum = f"{sys.argv[1]}{dir}";
        makeRequest = requests.get(dir_enum);
        if(makeRequest.status_code == 404):
            print("[X] " + dir_enum)
            pass;
        else:
            print("[HIT] " + dir);
            dirsFound.append(dir);
    running = False;

if __name__=="__main__":
    checkForFilesInp = input("File Extension(leave blank for dir only search): ");
    mainThread = threading.Thread(target=dirSearcher,args=(checkForFilesInp,) ,daemon=True);
    mainThread.start();
    timer = 0;
    while(running):
        os.system('cls')
        print("Elasped Time: {0}".format(timer));
        for dir in dirsFound:
            print(dir, end=" | ");
        print();
        time.sleep(1);
        timer = timer + 1;

