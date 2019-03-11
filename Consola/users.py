
import readline
import getpass

#Registro de usuarios


registeredUsers = {"atupilojon":"tupi-123","dpicchio":"jamaica","a":"a"}

def signInUser(username):
    #password = input('   password: ')
    password = getpass.getpass('   password: ')
    if password == registeredUsers.get(username):
        return True
    else:
        return False
