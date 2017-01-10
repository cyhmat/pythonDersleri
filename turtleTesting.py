from turtle import *
import random

def t1Movement():
    global t1Pos
    turtle1.forward(randomNum)
    t1Pos = t1Pos + randomNum
    print("t1Pos : " + str(t1Pos))
def t2Movement():
    global t2Pos
    turtle2.forward(randomNum)
    t2Pos = t2Pos + randomNum
    print("t2Pos : " + str(t2Pos))

def reset():
    turtle1.reset()
    turtle2.reset()
    raceTrack.reset()
    turtle1.hideturtle()
    turtle2.hideturtle()

def trackDrawing():
    raceTrack.up()  # Çizdirmiyoruz.
    raceTrack.left(180)  # Konum alıyor.
    raceTrack.forward(410)  # Konum alıyor.
    raceTrack.down()  # Çizim işlemi başlıyor.
    raceTrack.begin_fill()
    raceTrack.left(180)  # Konum alıyor.
    raceTrack.forward(820)  # Konum alıyor.
    raceTrack.color("lightgreen")
    raceTrack.left(90)  # Konum alıyor.
    raceTrack.forward(50)
    raceTrack.left(90)
    raceTrack.forward(820)  # Konum alıyor.
    raceTrack.left(90)
    raceTrack.forward(50)
    raceTrack.color("lightblue")
    raceTrack.forward(50)
    raceTrack.left(90)
    raceTrack.forward(820)  # Konum alıyor.
    raceTrack.left(90)
    raceTrack.forward(100)
    raceTrack.color("grey")
    raceTrack.up()
    raceTrack.left(90)
    raceTrack.forward(410)
    raceTrack.left(90)
    raceTrack.forward(50)

    turtle1.showturtle()
    turtle1.up()  # Çizdirmiyoruz.
    turtle1.shape("turtle")  # Şekli belirlendi.
    turtle1.color("lightgreen")  # Rengi belirlendi.
    turtle1.speed("slow")  # İlk pozisyona geçmek için hızı belirlendi.
    turtle1.right(90)  # Konum alıyor.
    turtle1.forward(50)  # Konum alıyor.
    turtle1.right(90)  # Konum alıyor.
    turtle1.forward(400)  # Konum alıyor.
    turtle1.left(180)  # Konum alıyor.

    turtle2.showturtle()
    turtle2.up()  # Çizdirmiyoruz.
    turtle2.shape("turtle")  # Şekli belirlendi.
    turtle2.color("lightblue")  # Rengi belirlendi.
    turtle2.speed("slow")  # İlk pozisyona geçmek için hızı belirlendi.
    turtle2.left(90)  # Konum alıyor.
    turtle2.forward(50)  # Konum alıyor.
    turtle2.left(90)  # Konum alıyor.
    turtle2.forward(400)  # Konum alıyor.
    turtle2.right(180)  # Konum alıyor.

screen = Screen()  # Ekranı oluşturdum.
screen.title("Welcome to the turtle race!")
raceTrack = Turtle()  # Yarış alanını çizecek turtle'ı oluşturdum.
turtle1 = Turtle()  # turtle1 Objesini oluşturdum.
turtle2 = Turtle()  # turtle2 Objesini oluşturdum.


turtle1.hideturtle()
turtle2.hideturtle()

finishLine = 800
t1Pos = 0
t2Pos = 0
boolNum = 1

player1 = screen.textinput("Player Name", "Name of first player:")
player2 =screen.textinput("NIM", "Name of second player:")

while boolNum == 1:
    trackDrawing()
    t1Pos = 0
    t2Pos = 0
    while t1Pos < finishLine and t2Pos < finishLine:
        randomNum = random.randint(1, 10)
        t1Movement()
        randomNum = random.randint(1, 10)
        t2Movement()

    if t1Pos>t2Pos:
        print("Kazanan Kaplumbağa {}".format(player1))
        raceTrack.write("Kazanan Kaplumbağa {}".format(player1),"center",font=("Arial",16,"normal"))
        boolNum = screen.numinput("Devam etmek için 1 , çıkmak için 0 giriniz.","Girdi : ")
        if boolNum == 1 :
            reset()
        else:
            pass
    elif t2Pos>t1Pos:
        print("Kazanan Kaplumbağa {}".format(player2))
        raceTrack.write("Kazanan Kaplumbağa {}".format(player2),"center",font=("Arial",16,"normal"))
        boolNum = screen.numinput("Devam etmek için 1 , çıkmak için 0 giriniz.","Girdi : ")
        if boolNum == 1 :
            if boolNum == 1:
                reset()
        else:
            pass
    else:
        print("Beraberlik !")



screen.exitonclick()