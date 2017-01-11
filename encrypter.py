import math
import itertools

def menu():
    while True:
        try:
            print(menuStr)
            print(stars)
            choose = int(input("For Encrypter = 1\nFor Decrypter = 2\nFor Exit = 0\nChoose : "))
            print(stars)
            break
        except:
            print("Girdi de bir problem var.")
            pass

    if choose == 1:
            print("Encrypter opening...")
            print(stars)
            myEncrypter()
    elif choose == 2:
            print("Decrypter opening...")
            myDecrypter()
    elif choose == 0:
            print("Cya dude.")
    else:
        print("Hata menüde.")
        menu()


def myEncrypter():
    inputWord = str(input("Input : "))
    print(stars)
    iList = list(inputWord)
    aList = []
    tempList = []
    outputList = []
    t=0

    for item in iList:
        try:
            aList.append(((alphabet.index(item)+1)*2)%29)
        except:
            print("Şuan sadece alfabe ile işlem yapabilirsiniz.")
            iList.clear()
            myEncrypter()


    for x in aList:
        tempList = list(str(math.sin(x)))
        tempList.reverse()
        for items in itertools.islice(tempList,0,3):
            outputList.append(items)


    for a in outputList:
        if t == 0 :print("Sonucunuz: ",end="")
        t+=1
        print(a,end="")


def myDecrypter():
    print("b")

alphabet = ['a', 'b', 'c', 'ç', 'd', 'e', 'f', 'g', 'ğ', 'h', 'ı', 'i', 'j',
 'k', 'l', 'm', 'n', 'o', 'ö', 'p', 'r', 's', 'ş', 't', 'u', 'ü',
 'v', 'y', 'z']

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

menu()