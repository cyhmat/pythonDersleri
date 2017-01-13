import sys
sys.path.append("C:/Users/cyhmat/PycharmProjects/pythonDersleri/dPy")
import getpass
import databasePy

def register():
    username =  input("Username : ")
    password = getpass.getpass("Şifreniz lütfen : ")
    return username,password

def login():
    print("Logging")

