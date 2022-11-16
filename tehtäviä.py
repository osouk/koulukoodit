# 1.1 Kirjoita toistolause, joka kirjoittaa luvut nollasta kahteenkymmeneen.

laskuri = 0
while laskuri <= 20:
    print(laskuri)
    laskuri +=1
    
# 1.2 Kirjoita toistolause, joka kirjoittaa numerot kymmenestä kahteenkymmeneen.

laskuri = 10
while laskuri <= 20:
    print(laskuri)
    laskuri +=1

# 1.3 Kirjoita toistolause, joka kirjoittaa numerot sadasta nollaan. (100, 99, 98, jne.)
laskuri = 100
while laskuri >= 0:
    print(laskuri)
    laskuri -=1

# 1.4  Kirjoita toistolause, joka kirjoittaa joka toisen numeron yhdestä yhdeksään. (1,3,5,7,9)

laskuri = 1
while laskuri <= 9:
    print(laskuri)
    laskuri +=2

# 2.1 Kirjoita toistolause, joka kirjoittaa listassa olevien hedelmien nimiä. Kirjoita listaan ainakin viisi
# hedelmää

hedelmat = ["paaryna","omena","mandariini","appelsiini","kiwi"]
print(hedelmat)

#2.2 Kirjoita toistolause, joka käy läpi listaa, jossa on ihmisten ikiä. Listassa tulee olla ainakin kuusi numeroa
#väliltä 0-100. Jos luku on pienempi kuin 18, niin tulosta ”alaikäinen”, jos toisin niin tulosta ”täysi-ikäinen”.

ihmiset = [5,20,18,80,54,17]
for i in range(len(ihmiset)):
    if ihmiset[i] >= 18:
        print("täysi-ikäinen")
    else:
        print("alaikäinen")

# 2.3 Kirjoita toisto lause, joka lisää listaan viiden kertotaulun numerot kymmenenteen kertoimeen asti.

luku = 0
loppu = 55
while luku < loppu:
    print(luku)
    luku += 5


# 2.4 Kirjoita toistolause, joka kirjoittaa listassa olevien lemmikkien nimiä. Nimet tulee kirjoittaa päin
# vastaisessa järjestyksessä, eli viimeinen nimi ensimmäisenä. Nimi listassa tulee olla ainakin neljä nimeä.
lemmikit = ["Musti", "katti", "kurre","lehmä"]
for i in range(len(lemmikit)):
    print( lemmikit[len(lemmikit) -i-1] )
      