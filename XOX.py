from time import sleep

def menu():
    try:
        sleep(3)
        print(menuStr)
        sleep(0.5)
        choose = int(input("For Play = 1\nFor Exit = 0\nChoose : "))
        print(stars)
    except:
        print("There's something wrong about your input. Try again.")
        menu()

    if choose == 1:
        sleep(0.3)
        print("Game starting...")
        player1 = str(input("Player1 : "))
        player2 = str(input("Player2 : "))
        sleep(0.3)
        print("Thanks a lot. ^^")
        return player1, player2
    elif choose == 0:
        print("Cya dude.")
    else:
        print("There's something wrong about your input. Try again.")
        menu()

def turns(p1,p2):
    global loop
    while True:
        sleep(1)
        print(stars)
        sleep(0.3)
        print(gamePlany1)
        sleep(0.3)
        print(gamePlany2)
        sleep(0.3)
        print(gamePlany3)
        sleep(0.3)
        print(stars)

        if win() == 1:
            loop = 1

            return loop
        else:
            pass

        if len(p1Cond) + len(p2Cond) == 9:
            print("Its a draw ! :D")
            menu()
        else:
            pass

        if turn%2 == 0:
            sleep(0.3)
            print("Its {}'s turn.".format(p1))
            sleep(0.3)
            print("Can you give me one x and one y cordinate ?")
            makeYourMove()
            break
        else:
            print("Its {}'s turn.".format(p2))
            print("Can you give me one x and one y cordinate ?")
            makeYourMove()
            break

def makeYourMove():
    try:
        x = int(input("X : "))
        y = int(input("Y : "))

        checkIt(x, y)
    except:
        print("Hatalı bir girdi verdiniz.")
        makeYourMove()

def checkIt(x,y):
    global turn
    if x == 1:
        if y == 1:
            if gamePlany1[0] != "___":
                print("Its already taken. Try again...")
                makeYourMove()
            else:
                if turn%2 == 0:
                    gamePlany1[0] = "X".center(3)
                    turn +=1
                    p1Cond.append(1)
                    turns(p1,p2)
                else:
                    gamePlany1[0]= "O".center(3)
                    turn += 1
                    p2Cond.append(1)
                    turns(p1,p2)
    if x == 1:
        if y == 2:
            if gamePlany1[1] != "___":
                print("Its already taken. Try again...")
                makeYourMove()
            else:
                if turn%2 == 0:
                    gamePlany1[1] = "X".center(3)
                    turn +=1
                    p1Cond.append(2)
                    turns(p1,p2)
                else:
                    gamePlany1[1]= "O".center(3)
                    turn += 1
                    p2Cond.append(2)
                    turns(p1,p2)

    if x == 1:
        if y == 3:
            if gamePlany1[2] != "___":
                print("Its already taken. Try again...")
                makeYourMove()
            else:
                if turn%2 == 0:
                    gamePlany1[2] = "X".center(3)
                    turn +=1
                    p1Cond.append(3)
                    turns(p1,p2)
                else:
                    gamePlany1[2]= "O".center(3)
                    turn += 1
                    p2Cond.append(3)
                    turns(p1,p2)

    if x == 3:
        if y == 1:
            if gamePlany3[0] != "___":
                print("Its already taken. Try again...")
                makeYourMove()
            else:
                if turn%2 == 0:
                    gamePlany3[0] = "X".center(3)
                    turn +=1
                    p1Cond.append(7)
                    turns(p1,p2)
                else:
                    gamePlany3[0]= "O".center(3)
                    turn += 1
                    p2Cond.append(7)
                    turns(p1,p2)
    if x == 3:
        if y == 2:
            if gamePlany3[1] != "___":
                print("Its already taken. Try again...")
                makeYourMove()
            else:
                if turn%2 == 0:
                    gamePlany3[1] = "X".center(3)
                    turn +=1
                    p1Cond.append(8)
                    turns(p1,p2)
                else:
                    gamePlany3[1]= "O".center(3)
                    turn += 1
                    p2Cond.append(8)
                    turns(p1,p2)

    if x == 3:
        if y == 3:
            if gamePlany3[2] != "___":
                print("Its already taken. Try again...")
                makeYourMove()
            else:
                if turn%2 == 0:
                    gamePlany3[2] = "X".center(3)
                    turn +=1
                    p1Cond.append(9)
                    turns(p1,p2)
                else:
                    gamePlany3[2]= "O".center(3)
                    turn += 1
                    p2Cond.append(9)
                    turns(p1,p2)

    if x == 2:
        if y == 1:
            if gamePlany2[0] != "___":
                print("Its already taken. Try again...")
                makeYourMove()
            else:
                if turn%2 == 0:
                    gamePlany2[0] = "X".center(3)
                    turn +=1
                    p1Cond.append(4)
                    turns(p1,p2)
                else:
                    gamePlany2[0]= "O".center(3)
                    turn += 1
                    p2Cond.append(4)
                    turns(p1,p2)
    if x == 2:
        if y == 2:
            if gamePlany2[1] != "___":
                print("Its already taken. Try again...")
                makeYourMove()
            else:
                if turn%2 == 0:
                    gamePlany2[1] = "X".center(3)
                    turn +=1
                    p1Cond.append(5)
                    turns(p1,p2)
                else:
                    gamePlany2[1]= "O".center(3)
                    turn += 1
                    p2Cond.append(5)
                    turns(p1,p2)

    if x == 2:
        if y == 3:
            if gamePlany2[2] != "___":
                print("Its already taken. Try again...")
                makeYourMove()
            else:
                if turn%2 == 0:
                    gamePlany2[2] = "X".center(3)
                    turn +=1
                    p1Cond.append(6)
                    turns(p1,p2)
                else:
                    gamePlany2[2]= "O".center(3)
                    turn += 1
                    p2Cond.append(6)
                    turns(p1,p2)

    if x >3 or x<1 :
        sleep(0.3)
        print("Hatalı bir girdi verdiniz.")
        makeYourMove()

def win():
    p1Cond.sort()
    p2Cond.sort()
    w = 0

    if winCond.count(p1Cond) == 1:
        print("Congratulations {}. You win.".format(p1))
        w = 1
        return w
    elif winCond.count(p2Cond) == 1:
        print("Congratulations {}. You win.".format(p2))
        w = 1
        return w

menuStr = """
_______________________________________________________________________________________
                  _____                             _
  _ __ ___  _   _| ____|_ __   ___ _ __ _   _ _ __ | |_ ___ _ __
 | '_ ` _ \| | | |  _| | '_ \ / __| '__| | | | '_ \| __/ _ \ '__|
 | | | | | | |_| | |___| | | | (__| |  | |_| | |_) | ||  __/ |
 |_| |_| |_|\__, |_____|_| |_|\___|_|   \__, | .__/ \__\___|_|
            |___/                       |___/|_|                 v.0.0.2
_________________________________________________________________________________________

"""
stars = "_" * 89
gamePlany1 =["___","___","___"]
gamePlany2 =["___","___","___"]
gamePlany3 =["___","___","___"]
winCond = [[1,2,3],[4,5,6],[7,8,9],[1,5,9],[3,5,7],[1,4,7],[2,5,8],[3,6,9]]
p1Cond = []
p2Cond = []
turn = 0
loop = 0

p1, p2 = menu()
sleep(0.5)
turns(p1,p2)

if loop == 1:
    menu()
