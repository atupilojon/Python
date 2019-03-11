
#Subproceso de para telnet a equipos

devices = [("localhost","127.0.0.1")]

def runTelnet(username):
    while True:
        inCommand = input('{}~telnet# '.format(username)).lower()
        if inCommand != "exit":
            print("Nothing...")
        else:
            break
