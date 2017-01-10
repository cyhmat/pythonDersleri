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

screen = Screen() #Ekranı oluşturdum.

raceTrack = Turtle()#Yarış alanını çizecek turtle'ı oluşturdum.
raceTrack.up() # Çizdirmiyoruz.
raceTrack.left(180)#Konum alıyor.
raceTrack.forward(410)#Konum alıyor.
raceTrack.down()#Çizim işlemi başlıyor.
raceTrack.begin_fill()
raceTrack.left(180)#Konum alıyor.
raceTrack.forward(820)#Konum alıyor.
raceTrack.color("lightgreen")
raceTrack.left(90)#Konum alıyor.
raceTrack.forward(50)
raceTrack.left(90)
raceTrack.forward(820)#Konum alıyor.
raceTrack.left(90)
raceTrack.forward(50)
raceTrack.color("lightblue")
raceTrack.forward(50)
raceTrack.left(90)
raceTrack.forward(820)#Konum alıyor.
raceTrack.left(90)
raceTrack.forward(100)
raceTrack.color("grey")
raceTrack.up()
raceTrack.left(90)
raceTrack.forward(410)
raceTrack.left(90)
raceTrack.forward(50)



turtle1 = Turtle() # turtle1 Objesini oluşturdum.
turtle1.up() # Çizdirmiyoruz.
turtle1.shape("turtle") # Şekli belirlendi.
turtle1.color("lightgreen") # Rengi belirlendi.
turtle1.speed("slow") # İlk pozisyona geçmek için hızı belirlendi.
turtle1.right(90)#Konum alıyor.
turtle1.forward(50)#Konum alıyor.
turtle1.right(90)#Konum alıyor.
turtle1.forward(400)#Konum alıyor.
turtle1.left(180)#Konum alıyor.

turtle2 = Turtle() # turtle2 Objesini oluşturdum.
turtle2.up() # Çizdirmiyoruz.
turtle2.shape("turtle") # Şekli belirlendi.
turtle2.color("lightblue") # Rengi belirlendi.
turtle2.speed("slow") # İlk pozisyona geçmek için hızı belirlendi.
turtle2.left(90)#Konum alıyor.
turtle2.forward(50)#Konum alıyor.
turtle2.left(90)#Konum alıyor.
turtle2.forward(400)#Konum alıyor.
turtle2.right(180)#Konum alıyor.

finishLine = 800
t1Pos = 0
t2Pos = 0

while t1Pos < finishLine and t2Pos < finishLine:
    randomNum = random.randint(1, 10)
    t1Movement()
    randomNum = random.randint(1, 10)
    t2Movement()

if t1Pos>t2Pos:
    print("Yeşil kaplumbağa kazandı !")
    raceTrack.write("Yeşil kaplumbağa kazandı !","center",font=("Arial",16,"normal"))
elif t2Pos>t1Pos:
    print("Mavi kaplumbağa kazandı !")
    raceTrack.write("Mavi kaplumbağa kazandı !","center",font=("Arial",16,"normal"))
else:
    print("Beraberlik !")

screen.exitonclick()