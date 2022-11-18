# 1.1
# Kirjoita luokka nimeltä ”auto”. Luokasta tulee löytyä muuttujat merkki, väri, paino, vuosimalli, kilometrit,
# hinta. Lisää muuttujien merkki, väri, paino, vuosimalli ja kilometrit arvot itse.
# Luo listaan vähintään 3kpl auto-olioita. Voit keksiä olioiden muuttujien arvot itse. Auto-oliot tulee lisätä
# listaan nimeltään Autot.
# Esimerkki listaan lisäämisestä
# Auto1 = Auto()
# Autot = []
# Autot.append(Auto1)

# Esimerkki arvoja:
# mersu, tummansininen, 1200kg, 1994, 200000
# volvo, punainen, 1000kg, 1999, 350000
# cadillac, vihreä, 2500kg, 1985, 150000

# 1.2
# Kirjoita auto luokkaan funktio, joka laskee auton hinnan. Hinta rakentuu kahdesta osasta, ikäkerroin ja
# kilometrikerroin.
# Ikäkerroin lasketaan seuraavasti: 1 + (1 / ikä) * 100.
# Kilometrikerroin rakentuu: 1 + (1 / kilometrit) * 10000 * 100
# Lopuksi hinta lasketaan (Ikäkerroin + Kilometrikerroin) * 1000
# Pyöristä hinta niin, että hinta on kokonaisluku.

# 1.3
# Tulosta autojen tiedot. Tiedot tulee tulostaa hinta järjestyksessä, kalleimmasta halvimpaan. Tulosta auto
# kohtaiset tiedot seuraavan laisesti: Merkki, väri, vuosimalli, kilometrit, hinta.
# Esimerkki tulostuksesta
# cadillac, vihreä, 2500kg, 1985, 150000, 10794
# mersu, tummansininen, 1994, 200000, 10571
# volvo, punainen, 1000kg, 1999, 350000, 8083

Autot = []

class auto:
    def __init__(self):
        self.merkki = " "
        self.vari = " "
        self.paino  = "0"
        self.ika = "0"
        self.kilsat = "0"
        self.hinta = "0"
        

Auto1 = auto()
Auto1.merkki =
Autot.append(Auto1)

Auto2 = auto()
Auto2.merkki = "puegeotti"
Auto2.vari = "harmaa"
Auto2.paino = "1300kg"
Auto2.ika = "2007"
Auto2.kilsat = "2000000"
Auto2.hinta = "0"
Autot.append(Auto2)

Auto3 = auto()
Auto3.merkki = "Chervolet"
Auto3.vari = "punainen"
Auto3.paino = "1600kg"
Auto3.ika = "1969"
Auto3.kilsat = "150000"
Auto3.hinta = "0"
Autot.append(Auto3)

print(Autot)