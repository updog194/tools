import hashlib
import os
import sys

fileName = "";
hash = "";
hashType = "md5";

def getArgs():
    try:
        global fileName;
        fileName = sys.argv[1];
        global hash;
        hash = sys.argv[2];
        global hashType;
        hashType = sys.argv[3];
    except Exception as e:
        print("Error in hanbdeling arguments <python.py> <filename(ABS PATH)> <hash> <optional specified hash type>")
        pass;

def crackHash():
    global hashType;
    global hash;
    global fileName;

    try:
        with open(fileName, "r") as f:
            print("Attempting to crack HASH: " + str(hash) + " with " + hashType);
            for line in f:
                if(hashType == "md5"):
                    hashLine = hashlib.md5(line.strip().encode());
                    hashedPass = hashLine.hexdigest();
                    if(hashedPass == hash):
                        print("PASSSWORD FOUND: " + str(line.strip()))
                elif(hashType == "sha256"):
                    hashLine = hashlib.sha256(line.strip().encode());
                    hashedPass = hashLine.hexdigest();
                    if(hashedPass == hash):
                        print("PASSSWORD FOUND: " + str(line.strip()))
                        break;

    except Exception as e:
        print(e);

if __name__=="__main__":
    getArgs();
    crackHash();