import sys
sys.path.append("C:/Users/cyhmat/PycharmProjects/pythonDersleri/dPy")
import databasePy
from time import sleep
stars = "=" * 90 # Just for menu.
#==============================================================================================================
# Here we are making our enterance for login or register.
# After the enter() we are executing databasePy.py
#==============================================================================================================
def enter():
    sEnter = """
+-----------------------------------------------------+
|                                                     |
|                                                     |
|                                                     |
|                 X    XXXXXXXX                       |
|                 X    X      XXX                     |
|                 X    X        XX                    |
|                 X    X         X                    |
|                 X    X         X                    |
|                 X    X         XX                   |
|                 X    X          X                   |
|                 X    X         XX                   |
|                 X    X         X                    |
|                 X    X      XXXX                    |
|                 X    XXXXXXXX                       |
|        XXXXXXXX X    X                              |
|      XXX        X    X         X    X               |
|     XX          X    X         X    X               |
|     XX         XX    X         XX XXXX              |
|      XXX      XX     X     X    XXX  X              |
|        XXXXXXXX      X     X        XX              |
|                            XXX     XX               |
|                              XXXXXX                 |
|                                         cyhmat 2017 |
|                                                     |
+-----------------------------------------------------+

    """ # Its cool right ? :D
    sleep(0.5)
    print(stars)
    sleep(0.5)
    print(sEnter) # Make this logo animated.
    sleep(0.5)
    print(stars)

    while True:
        chooseEnter = 0
        try:
            chooseEnter= int(input("If you are a user please press '1'\n"
                                   "If you want to register please press '2'\n" # We are getting inputs.
                                   "If you want to  exit please press '0'\n"
                                   "Make your choose : "))
            break
        except ValueError:
            print("There is something wrong with your input.")

    if chooseEnter ==  1 : print("Login.")
    elif chooseEnter == 2 :  databasePy.createtable() , databasePy.registerinfo()
    elif chooseEnter== 0 : input("See you later ! ^^")
    else: print("There is something wrong with your input.")

enter()