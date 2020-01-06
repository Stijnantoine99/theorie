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
# print(wijk1)

for i in range(0,12):
    x = random.randrange(2,158)
    y_oud = random.randrange(2,158)

    while wijk1[x][y_oud] == "H":
        x = random.randrange(2,158)
        y_oud = random.randrange(2,158)

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


    if wijk1[x+8][y_oud] or wijk1[x][y_oud+8] == 'H':
        print("Break")
    else: 
        for i in range(0,8):
            x += 1
            print(x)
            wijk1[x][y_oud] = "H"
            for j in range(0,8):
                y = y_oud + j
                print(y)
                wijk1[x][y] = "H"






# print(wijk1)

with open("wijk1.csv","w+") as my_csv:
    csvWriter = csv.writer(my_csv,delimiter=',')
    csvWriter.writerows(wijk1)