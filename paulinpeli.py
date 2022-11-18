#Pelitehtavava 17.11.2022
#pelissa kuuluu olla pelaaja luokka, seka luokka aarteelle ja hyttysille.
#pelissa tulee olla 10x10 kentta jossa kaikki oliot ovat
# hahmo liikkuu wasd nappaimin
# pelaajalla on 100 energiaa ja jos osuu hyttyseen han menettaa osan siita
#jos pelaaja osuu aarre ruutuun han voittaa pelin
#Peliluuppi voidaan toteuttaa "while-input"-rakenteella, Pygamea tai hiirta ei tarvita

#A) Toteuta ja testaa peli.

#B) Paranna pelia, niin, etta se on oikeasti pelattava, eika voitto ole vain satunnainen.

oliot = []
for y in range(10):
    kolumn = " "

   
import random

class pelaaja:
    def __init__(self):
        self.energia = 100
        self.pos = [0,0]
        self.merkki = "P"
       
    
class hyttynen:
    def __init__(self):
        self.pos = [9,9]
        self.merkki = "V"

class aarre:
    def __init__(self):
        self.pos = [random.randint(0,10), random.randint(0,10)]
        self.merkki = "A"
        
mina = pelaaja()
oliot.append(mina)

vihu = hyttynen()
oliot.append(vihu)

chest = aarre()
oliot.append(chest)
for x in range(10):
        
    sisaltaa = " "
    for a in oliot:
        if a.pos == [y.x]:
            sisaltaa = a.merkki
    kolumn += sisaltaa
    print(kolumn)