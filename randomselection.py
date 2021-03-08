import random
lines = open('imageswithoutreferences.txt').read().splitlines()

for i in range(10):
    myline =random.choice(lines)
    print(myline)
    
    