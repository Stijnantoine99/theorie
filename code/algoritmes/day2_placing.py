import random
import csv
import numpy as np 
import matplotlib.pyplot as plt
import matplotlib.colors

x, y = (160, 180) 
wijk1 = [[0 for i in range(x)] for j in range(y)] 
counter = 0 

while counter < 12: 
    x = random.randrange(32,158)
    y_oud = random.randrange(2,178)

    while wijk1[y_oud][x] != 0:
        x = random.randrange(32,158)
        y_oud = random.randrange(2,178)

    if wijk1[y_oud][x+8] or wijk1[y_oud+8][x] != 0:
        print("Break")
    else: 
        for i in range(0,8):
            x += 1
            print(x)
            wijk1[y_oud][x] = 1
            for j in range(0,8):
                y = y_oud + j
                print(y)
                wijk1[y][x] = 1  
        counter += 1  


counter_maison = 0 
while counter_maison < 3:
    x = random.randrange(32,158)
    y_oud = random.randrange(2,178)

    while wijk1[y_oud][x] != 0:
        x = random.randrange(32,158)
        y_oud = random.randrange(2,178)
    
    if wijk1[y_oud][x+8] or wijk1[y_oud+8][x] != 0:
        print("Break")
    else: 
        for i in range(0,12):
            x += 1
            print(x)
            wijk1[y_oud][x] = 3
            for j in range(0,10):
                y = y_oud + j
                print(y)
                wijk1[y][x] = 3 
        counter_maison += 1  

counter_bungalow = 0
while counter_bungalow < 5:
    x = random.randrange(32,158)
    y_oud = random.randrange(2,18)

    while wijk1[y_oud][x] != 0:
        x = random.randrange(32,158)
        y_oud = random.randrange(2,178)
    
    if wijk1[y_oud][x+8] or wijk1[y_oud+8][x] != 0:
        print("Break")
    else: 
        for i in range(0,11):
            x += 1
            print(x)
            wijk1[y_oud][x] = 2
            for j in range(0,7):
                y = y_oud + j
                print(y)
                wijk1[y][x] = 2
        counter_bungalow += 1  


H = np.array(wijk1)
plt.imshow(H)
plt.pcolor(H, cmap = "Greens_r")

plt.show()
plt.savefig("blueprint.png")

with open("wijk1.csv","w+") as my_csv:
    csvWriter = csv.writer(my_csv,delimiter=',')
    csvWriter.writerows(wijk1)