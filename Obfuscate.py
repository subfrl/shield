import os
from Junk import Shield
import binascii
import sys
import time
import base64
from colored import fg

c1 = fg("#1452fc")
c2 =fg("#ffffff")
c3 =fg("#fc2b2e")

imports = []

os.system('title ')
os.system('cls')
os.system('mode con: cols=80 lines=30')
print(f"""{c1}



                                _ |_  o  _  |  _|
                               _> | | | (/_ | (_|

""")

f = input(f"{c1}File name{c1}:{c2} ")
f2 = input(f"{c1}Create new file {c2}(Y/N){c1}:{c2} ")
f3 = input(f"{c1}Anti-debugger {c2}(Y/N){c1}:{c2} ")
f4 = int(input(f"{c1}Junk amount {c3}(100 Max){c1}:{c2} "))

if f4 > 100:
    f1 = int(100)
else:
    pass

with open("Anti.py", "r") as anti:
    c = anti.read()

# I loved this obfuscation by wodxgod, so i decided to use it ! (If you are seeing this wodxgod, if you would like this part to be removed, please contact us)
OFFSET = 20
VARIABLE_NAME = '__SHILDED_SHILDED' * 20

def SecondLayer(content):
    b64_content = base64.b64encode(content.encode()).decode()
    index = 0
    code = f'{VARIABLE_NAME} = ""\n'
    for _ in range(int(len(b64_content) / OFFSET) + 1):
        _str = ''
        for char in b64_content[index:index + OFFSET]:
            byte = str(hex(ord(char)))[2:]
            if len(byte) < 2:
                byte = '0' + byte
            _str += '\\x' + str(byte)
        code += f'{VARIABLE_NAME} += "{_str}"\n'
        index += OFFSET
    code += f'exec(__import__("\\x62\\x61\\x73\\x65\\x36\\x34").b64decode({VARIABLE_NAME}.encode("\\x75\\x74\\x66\\x2d\\x38")).decode("\\x75\\x74\\x66\\x2d\\x38"))'
    return code

def RetriveImports(f):
    file1 = open(str(f), 'r', errors='ignore')
    Lines = file1.readlines()
    for line in Lines:
        if("import" in line and not "#" in line and not "(" in line and not ")" in line and not '"' in line):
            imports.append(line)

def oneline_hex(string):
    pbase = "import binascii\nexec(binascii.unhexlify(bytes('PLACEHOLDER','UTF-8')).decode())"
    result = binascii.hexlify(bytes(string, 'utf-8')).decode()
    return pbase.replace('PLACEHOLDER', result)

def oneliner(f, c):
    with open(str(f), 'r', encoding="utf8") as e:
        code = str(e.read())
        e.close()
        print(f"{c1}[{c2}+{c1}] One liner has started..")
        result = code
        for i in range(5):
            result = oneline_hex(result)

    result = SecondLayer(result).encode('utf-8')
    a = base64.b64encode(result)
    result = (f"exec(base64.b64decode({str(a)}))").encode('utf-8')
    result = result.decode("utf-8")

    if f2 == "y" or f2 == "Y" or f2 == "yes" or f2 == "YES" or f2 == "ye" or f2 == "ya":
        with open(f"Output.py", 'w') as e:
            Shield.junk(e, f4)
            if f3 == "y" or f3 == "Y" or f3 == "yes" or f3 == "YES" or f3 == "ye" or f3 == "ya":
                print(f"{c1}[{c2}+{c1}] Adding anti-debugger..")
                c = c.encode('utf-8')
                h = base64.b64encode(c)
                for i in range(3):
                    result1 = (f"exec(base64.b64decode({str(h)}))").encode('utf-8')
                result1 = result1.decode("utf-8")
                e.write(result1 + "\n")
                print(f"{c1}[{c2}+{c1}] Finished adding anti-debugger..")
            e.write(str(result))
            Shield.junk(e, f4)
            Shield.junk(e, f4)
            e.close()
        with open(f"Output.py",'r') as contents:
            save = contents.read()
        with open(f"Output.py",'w') as contents:
            for i in range(len(imports)):
                contents.write(imports[i])
            contents.write("import base64\n")
        with open(f"Output.py",'a') as contents:
            contents.write(save)
    else:
        with open(str(f), 'w') as e:
            Shield.junk(e, f4)
            if f3 == "y" or f3 == "Y" or f3 == "yes" or f3 == "YES" or f3 == "ye" or f3 == "ya":
                print(f"{c1}[{c2}+{c1}] Adding anti-debugger..")
                c = c.encode('utf-8')
                h = base64.b64encode(c)
                for i in range(3):
                    result1 = (f"exec(base64.b64decode({str(h)}))").encode('utf-8')
                result1 = result1.decode("utf-8")
                e.write(result1 + "\n")
                print(f"{c1}[{c2}+{c1}] Finished adding anti-debugger..")
            e.write(str(result))
            Shield.junk(e, f4)
            Shield.junk(e, f4)
            e.close()
        with open(str(f),'r') as contents:
            save = contents.read()
        with open(str(f),'w') as contents:
            for i in range(len(imports)):
                contents.write(imports[i])
            contents.write("import base64\n")
        with open(str(f),'a') as contents:
            contents.write(save)


    print(f"{c1}[{c2}+{c1}] Finished one lining..")

os.system('cls')
RetriveImports(f)
oneliner(f, c)

print(f"{c1}[{c2}+{c1}] Successfully obfuscated your file")
time.sleep(5)
sys.exit()
