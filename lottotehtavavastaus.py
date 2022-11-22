#lotto simulaattori tehtävä

#käyttäjä valitsee 7 random numeora väliltä 1-41,
#kaikkien lukujen tulee olla uniikkeja

#lopuksi ohjelma tulostaa oikein arvattujen lukujen määrän,
#ja jos kaikki on oikein niin tulostaa "Voitit"

import random

#arvaukset
arvaukset = []
while len(arvaukset) < 7:
    luku = int(input("Arvaa luku väliltä 1-41: "))
    
    if luku > 41 or luku < 1: #tarkistaa luvun mahdollisuuden
        print("Luku ei ole väliltä 1-41")
        continue
    
    if luku not in arvaukset: #selvittää onko listassa luku
        arvaukset.append(luku)
    else:
        print("Olen kirjoittanut tämän luvun jo")
        
        
#lotto generointi
lotto = []
while len(lotto) < 7:
    luku = random.randint(1,41)
    
    if luku not in lotto:
        lotto.append(luku)


#Pisteytys
laskuri = 0
for i in range(len(arvaukset)):
    if arvaukset[i] in lotto:
        laskuri += 1
print("Pisteitä: " + str(laskuri))
    
print(lotto)
    
    




