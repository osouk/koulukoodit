# # taulukko = [23,34,45,56,77]
# # maara=len(taulukko)
# # print(maara)
# # taulukko.append("Miisu")
# # print(taulukko)
# # maara=len(taulukko)
# # print(maara)
# # laskuri = 0
# # while laskuri < maara:
# #     #Printataan indeksi ja sen osoittama taulukon alkio
# #     print("Indeksi on:", laskuri, "Alkio:", taulukko[laskuri])
# #     laskuri += 2# 
# # #     tulosta joka toinen alkio taulukko:sta
# 
import random

tulos = []
parilliset = []
parittomat = []
# laita taulukkoon 100 klp satunnaislukuja valilta 0-100
laskuri = 0
while laskuri < 100:
    tulos.append(random.randint(0,100))
    laskuri += 1
while laskuri < 100:
    laskuri +=1
    print(tulos[laskuri])
laskuri = 0
while laskuri < 100:
    tulos.append(random.randint(0,100))
    laskuri += 1
    
print("Erotellaan parilliset!")
laskuri = 0
while laskuri <100:
    luku = tulos[laskuri]
    print(luku, end = " ")
#     jos tuo "luku" on parillinen se laitetaan parillisten taulukkoon.
    if luku %2 == 0:
        parilliset.append(luku)
    if luku %2 == 1:
        parittomat.append(luku)
    laskuri = laskuri + 1
print(parilliset)
print(parittomat)