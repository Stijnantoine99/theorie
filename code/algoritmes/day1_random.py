# Random huizen plaatsen

# 20 huizen
# 12 eensgezinswoningen
# 5 bungalows
# 3 maisons

import random
import csv

# xlist = []
# for i in range(0,160):
#     xlist.append("i")
# print(xlist)

# ylist = []
# for i in range(0,180):
#     ylist.append("i")
# # print(ylist)

# x = random.choice(xlist[2:158])
# y = random.choice(ylist[2:178])

# x = random.randrange(2,158)
# y = random.randrange(2,158)

# print(x,y)

# xlist[x] = "X"
# print(xlist)


x, y = (160, 180) 
wijk1 = [[0 for i in range(x)] for j in range(y)] 
counter = 0 
# print(wijk1)

while counter < 12: 
    x = random.randrange(32,158)
    y_oud = random.randrange(2,178)

    while wijk1[y_oud][x] != 0:
        x = random.randrange(32,158)
        y_oud = random.randrange(2,178)

    print(x,y_oud)
    # wijk1[x][y_oud] = 'H'
    # print(wijk1)

    # for i in range(0,8):
    #     x += 1
    #     print(x)
    #     wijk1[x][y_oud] = "H"
    #     for j in range(0,8):
    #         y = y_oud + j
    #         print(y)
    #         wijk1[x][y] = "H"
    if wijk1[y_oud][x+8] or wijk1[y_oud+8][x] != 0:
        print("Break")
    else: 
        for i in range(0,8):
            x += 1
            print(x)
            wijk1[y_oud][x] = "E"
            for j in range(0,8):
                y = y_oud + j
                print(y)
                wijk1[y][x] = "E"  
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
            wijk1[y_oud][x] = "M"
            for j in range(0,10):
                y = y_oud + j
                print(y)
                wijk1[y][x] = "M"  
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
            wijk1[y_oud][x] = "B"
            for j in range(0,7):
                y = y_oud + j
                print(y)
                wijk1[y][x] = "B"  
        counter_bungalow += 1  










# print(wijk1)

with open("wijk1.csv","w+") as my_csv:
    csvWriter = csv.writer(my_csv,delimiter=',')
    csvWriter.writerows(wijk1)