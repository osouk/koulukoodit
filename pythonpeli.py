import pgzrun,math
# from pgzhelper import *
WIDTH = 500
HEIGHT = 500

 

alien = Actor('alien')
alien.x = 0
alien.y = 50
WIDTH = 500
HEIGHT = 500

 

background = Actor('background')
ticker = 0
suuntax = 0
suuntay = 0
laajuus = 24
def draw():
    screen.clear()
    background.draw()
    alien.draw()
def update():
    global ticker,suuntax,suuntay,staminaincrease,stamina,staminaOnAarre
    alien.x -= 4
    alien.y -= 4
    alien.x %= WIDTH
    alien.y %= HEIGHT
    ticker += 1
pgzrun.go()