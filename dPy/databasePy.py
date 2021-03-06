import sqlite3
import sys
sys.path.append("C:/Users/cyhmat/PycharmProjects/pythonDersleri/dPy")
import login

stars = "=" * 90

#==============================================================================================================
# This is where the tables are create.
#==============================================================================================================

def createtable():
    con = sqlite3.connect("database.db")
    print(stars)
    print("Connection established !")
    cursor = con.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS users(username,password)")
    cursor.execute("CREATE TABLE IF NOT EXISTS lessons(lesson,testorstudy,howlong,howmany)")
    con.commit()
    con.close()
    print("Tables created !")
    print(stars)

#==============================================================================================================
# I'm registering infos into the users table.
#==============================================================================================================

def registerinfo():
    con = sqlite3.connect("database.db")
    cursor = con.cursor()
    username = input("Username : ") # Sqlite highlighting and implementing not working on my IDE.
    password = getpass.getpass("Şifreniz lütfen : ") # Check it out later.
    cursor.execute("INSERT INTO users (username,password) VALUES(?,?)", (username, password))
    con.commit()
    con.close()
    print(stars)
    print("Registration completed.")
    print(stars)

#==============================================================================================================
# I'm checking inputs in here.
#==============================================================================================================

def checklogin():
