from time import sleep
from threading import Thread
from psutil import process_iter

vmservices = ["vmsrvc", "vmusrvc", "vboxtray", "vmtoolsd", "df5serv", "vboxservice"]
debuggers = ["Suspend", "Progress Telerik Fiddler Web Debugger", "Fiddler", "Wireshark", "dumpcap", "dnSpy", "dnSpy-x86", "cheatengine-x86_64", "HTTPDebuggerUI", "Procmon", "Procmon64", "Procmon64a", "ProcessHacker", "x32dbg", "x64dbg", "DotNetDataCollector32", "DotNetDataCollector64", "HTTPDebuggerSvc", "HTTP Debugger", "ida", "ida64", "idag", "idag64", "idaw", "idaw64", "idaq", "idaq64", "idau", "idau64", "scylla", "scylla_x64", "scylla_x86", "protection_id", "windbg", "reshacker", "ImportREC", "IMMUNITYDEBUGGER", "MegaDumper", "disassembly", "Debug", "[CPU" "Immunity", "MegaDumper 1.0 by CodeCracker / SnD", "Charles", "charles", "OLLYDBG", "Import_reconstructor", "codecracker", "de4dot", "ilspy", "graywolf", "simpleassemblyexplorer", "x64netdumper", "hxd", "petools", "simpleassembly", "httpanalyzer", "httpdebug", "processhacker", "memoryedit", "memory", "de4dotmodded", "process hacker", "process monitor", "qt5core"]

def VMServices():
    while True:
        for service in vmservices:
            for proc in process_iter():
                if service in proc.name():
                    exit()
        sleep(1.5)

def antiDebug():
    while True:
        for process in process_iter():
            for dbg in debuggers:
                if dbg in process.name().lower():
                    try:
                        process.kill()
                    except Exception:
                        exit()
            sleep(0.15)

Thread(target=VMServices, daemon=True).start()
Thread(target=antiDebug, daemon=True).start()