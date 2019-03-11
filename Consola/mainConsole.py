
# estructura central de la consola

import readline
import consoleCommands as comm
import users
from time import sleep,ctime

def openConsole(username):
    banner()
    print(ctime())
    if username == "guest":
        print("You're logged in as 'guest'")
    else:
        print("Welcome '{}'!\n".format(username))
    while True:
        inCommand = input('{}~# '.format(username)).lower()
        if inCommand != "exit":
            runCommand(username,inCommand)
        else:
            if exitConsole():
                break
            else:
                pass

def runCommand(username,command):
    if command == "help":
        comm.help()
    elif command == "admin":
        comm.admin()
    elif command == "clock":
        comm.clock()
    elif command == "logout":
        comm.logout(username)
    elif command == "menu":
        comm.menu()
    elif command == "signin":
        comm.signIn()
    elif command == "telnet":
        comm.telnet(username)
    elif command == "":
        pass
    else:
        print ("\nOops! command '{}' doesn't exists".format(command))

def exitConsole():
    validation = input("You're exiting TupiConsole. Confirm [y/n]: ")
    if validation == "y":
        print("\n   Exiting console...")
        print("   Powered by Tupi.\n")
        sleep(1)
        return True
    elif validation == "n":
        print("Canceling...")
        sleep(.5)
        return False
    else:
        print("Wrong input. Canceling...")
        sleep(.5)
        return False

def banner():
    print("\nWelcome to TupiConsole!")
