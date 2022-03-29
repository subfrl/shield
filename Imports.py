import os, sys, time, base64, random
from Junk import *

imports = []

def typing(word1):
    for word in word1:
        sys.stdout.write(word)
        time.sleep(0.05)
        sys.stdout.flush()

def encryption():
    with open("Test.py", 'rb') as f:
        data = f.read()

    file1 = open('Test.py', 'w')
    file1.write("")
    file1.close()
    with open("Test.py",'r') as contents:
        save = contents.read()
    with open("Test.py",'w') as contents:
        for i in range(len(imports)):
            contents.write(imports[i])
        contents.write("import base64\n")
    with open("Test.py",'a') as contents:
        contents.write(save)


    with open("Test.py", 'a') as f:
        a = base64.b64encode(data)
        a2 = (f"exec(base64.b64decode({str(a)}))").encode('utf-8')

        for i in range(25):
            a = base64.b64encode(a2)
            a2 = (f"exec(base64.b64decode({str(a)}))").encode('utf-8')
            Shield.junk(f, random.randint(20, 45))
            
        f.write(a2.decode("utf-8"))
        Shield.junk(f, random.randint(20, 45))
        typing("\nFinished first layer of encryption.\n")

def main():
    file1 = open('Test.py', 'r', errors='ignore')
    Lines = file1.readlines()
    count = 0
    for line in Lines:
        if("import" in line and not "#" in line and not "(" in line and not ")" in line and not '"' in line):
            count = count + 1
            imports.append(line)
    typing(f"File has {count} imports.\n")
    typing("Finished appending imports.\n")
    typing("Encrypting")
    for i in range(random.randint(3, 6)):
        sys.stdout.write('.')
        time.sleep(0.25)
        sys.stdout.flush()
    encryption()

main()