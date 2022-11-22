#noppa peli
#kuusi noppaa
#pisteitä saa sen mukaan , kuinka monta kappaletta on samaa silmäkukua

#[1,1,1,2,2,3] -> 3

import random

heitot = []


for i in range(6):
    heitot.append(random.randint(1,6))

erinumerot = len(set(heitot))
print(erinumerot)
print(heitot)
