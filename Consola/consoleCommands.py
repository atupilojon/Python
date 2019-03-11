
from time import ctime
import users
import mainConsole
import telnetSubProc

# comandos soportados por la consoleCommands
commandList = ["help","?","admin","exit","logout","menu","signin","telnet"]

def help():
    for command in commandList:
        print(" {}".format(command))

def admin():
    print ("Admin privileges in development...")

def clock():
    print(ctime())

def logout(username):
    print ("Login out '{}'".format(username))
    raise KeyboardInterrupt

def menu():
    print ("Printing list of equipments...")

def signIn():
    user = input('   username: ').lower()
    if users.signInUser(user):
        try:
            mainConsole.openConsole(user)
        except KeyboardInterrupt:
            print("")
    else:
        print("Bad username/password")

def telnet(username):
    try:
        telnetSubProc.runTelnet(username)
    except KeyboardInterrupt:
        print("")
