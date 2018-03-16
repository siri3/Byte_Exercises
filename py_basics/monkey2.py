import string
import random
import math

#compare = "methinks it is like a weasel"
compare = "i too"
l = len(compare)
match_i=[]
#generate a random string
def generate():
    alpha = " " + string.ascii_lowercase 
    gen=""
    for i in range (0,l):
        if i in match_i:
            gen = gen + compare[i]
        else:
            gen = gen + (random.choice(alpha))          
    return gen

#score
def scorefn(gen):
    same = 0
    for i in range(0,l):
        if compare[i] == gen[i]:
            same = same + 1 
            match_i.append(i)       
    return (same)

#repeat
j = 1
i = 1
best_score=0
gen = generate()
score = scorefn(gen)
while score < l:
    if i == 10000:
        print(j," ",best_score," ",best)
        i = 0
    i = i + 1
    j = j + 1
    gen = generate()
    score = scorefn(gen)
    if score > best_score:
        best_score = score
        best = gen
print ("complete at ",j," ",gen)
    
    
   



