#lotto simulaattori tehtävä

#käyttäjä valitsee 7 random numeora väliltä 1-41,
#kaikkien lukujen tulee olla uniikkeja

#lopuksi ohjelma tulostaa oikein arvattujen lukujen määrän,
#ja jos kaikki on oikein niin tulostaa "Voitit"
import random

lottonumerot = []
LottoArvaus = []

numerot = 1
while numerot <= 41:
    lottonumerot.append(numerot)
    numerot += 1
print(lottonumerot)

num = random.choice(lottonumerot)

print(num)
LottoArvaus.append(num)
lottonumerot.remove(num)

arvausmaara = 1
while arvausmaara <= 7:
    LottoArvaus.append(num)
    arvausmaara += 1
print(LottoArvaus)
            