import random
tulokset = []
for i in range (6):
    tulokset.append(random.randint(1,6))
    
score = []

for i in range(len(tulokset)):
    score.append(0)
    for k in range(len(tulokset)):
        if tulokset[i] == tulokset[k]:
            score[i] += 1
            
suurin = 0
for i in range(len(score)):
    if score[i] > suurin:
        suurin = score[i]
        
print(suurin, tulokset)