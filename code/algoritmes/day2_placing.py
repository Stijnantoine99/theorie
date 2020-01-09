import random
import csv
import numpy as np 
import matplotlib.pyplot as plt
import matplotlib.colors

x, y = (160, 180) 
wijk1 = [[0 for i in range(x)] for j in range(y)] 


# adding water

def water():
    x_coor = -1
    y_coor = -1
    for i in range(0,32):
        wijk1[y_coor][x_coor] = 4
        x_coor += 1 
        y_coor = -1

        for i in range(0,180):
            y_coor += 1
            wijk1[y_coor][x_coor] = 4
            
    

# adding eensgezinswoningen 

def eensgezinswoningen(aantal):
    eensgezins_coordinatenlijst = []
    counter = 0 
    while counter < aantal: 
        x = random.randrange(32,150)
        y_oud = random.randrange(2,170)
        print(wijk1[y_oud][x])


        while wijk1[y_oud][x] or wijk1[y_oud][x+8] or wijk1[y_oud+8][x] or wijk1[y_oud+8][x+8] != 0:
            x = random.randrange(32,150)
            y_oud = random.randrange(2,170)

        eensgezins_coordinatenlijst.append([x,y_oud])

        for i in range(0,8):
            x += 1
            wijk1[y_oud][x] = 1
            for j in range(0,8):
                y = y_oud + j
                wijk1[y][x] = 1  
        counter += 1  
    

# adding maison

def maison(aantal):
    maison_coordinatenlijst = []
    counter_maison = 0 
    while counter_maison < aantal:
        x = random.randrange(32,142)
        y_oud = random.randrange(6,164)

        while wijk1[y_oud][x] or wijk1[y_oud+5][x] or wijk1[y_oud][x+6] or wijk1[y_oud+10][x] or wijk1[y_oud][x+12] or wijk1[y_oud+10][x+6] or wijk1[y_oud+5][x+12] or wijk1[y_oud+10][x+12] != 0:
            x = random.randrange(32,142)
            y_oud = random.randrange(2,164)
        
        maison_coordinatenlijst.append([x,y_oud])

        for i in range(0,12):
            x += 1
            wijk1[y_oud][x] = 3
            for j in range(0,10):
                y = y_oud + j
                wijk1[y][x] = 3 
        counter_maison += 1  

# adding bungalow
def bungalow(aantal):
    bungalow_coordinatenlijst = []
    counter_bungalow = 0
    while counter_bungalow < aantal:
        x = random.randrange(32,146)
        y_oud = random.randrange(3,170)

        while wijk1[y_oud][x] or wijk1[y_oud][x+5] or wijk1[y_oud+7][x] or wijk1[y_oud][x+11] or wijk1[y_oud+7][x+11] or wijk1[y_oud+7][x+5] != 0:
            x = random.randrange(32,146)
            y_oud = random.randrange(2,170)

        bungalow_coordinatenlijst.append([x,y_oud])
        
        for i in range(0,11):
            x += 1
            wijk1[y_oud][x] = 2
            for j in range(0,7):
                y = y_oud + j
                wijk1[y][x] = 2
        counter_bungalow += 1  

    print(bungalow_coordinatenlijst[4])
    print(bungalow_coordinatenlijst[4][1])
    print(bungalow_coordinatenlijst[4][0])






def main():
    # adding houses
    water()
    eensgezinswoningen(12)
    bungalow(5)
    maison(3)

    # showing picture
    H = np.array(wijk1)
    plt.imshow(H)
    plt.pcolor(H, cmap = "Greens_r")

    plt.show()
    plt.savefig("blueprint.png")


    # saving in csv file
    with open("wijk1.csv","w+") as my_csv:
        csvWriter = csv.writer(my_csv,delimiter=',')
        csvWriter.writerows(wijk1)

if __name__ == '__main__':
    main()