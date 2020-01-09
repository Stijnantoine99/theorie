import random
import csv
import numpy as np 
import matplotlib.pyplot as plt
import matplotlib.colors

x, y = (160, 180) 
wijk1 = [[0 for i in range(x)] for j in range(y)] 


# adding water

class Placing: 


    def __init__(self, aantal_eensgezins, aantal_maison, aantal_bungalow):
        self.aantal_eensgezins = aantal_eensgezins
        self.aantal_maison = aantal_maison
        self.aantal_bungalow = aantal_bungalow



    def water(self):
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

    def eensgezinswoningen(self, aantal_eensgezins):
        eensgezins_coordinatenlijst = []
        counter = 0 
        while counter < aantal_eensgezins: 
            x = random.randrange(32,150)
            y_oud = random.randrange(2,170)

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

        return eensgezins_coordinatenlijst
        

    # adding maison

    def maison(self, aantal_maison):
        maison_coordinatenlijst = []
        counter_maison = 0 
        while counter_maison < aantal_maison:
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
    def bungalow(self, aantal_bungalow):
        bungalow_coordinatenlijst = []
        counter_bungalow = 0
        while counter_bungalow < aantal_bungalow:
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

    # print(bungalow_coordinatenlijst[4][0])
# def calculate():

class Kosten():

    def __init__(self, eengezins_aantal, bungalow_aantal, maison_aantal):
        self.eengezins_aantal = eengezins_aantal
        self.bungalow_aantal = bungalow_aantal
        self.maison_aantal = maison_aantal

        
    def eengezins_cost(self, eengezins_aantal):
        # make default prices of houses
        self.eengezins = 285000 
        self.eengezins_aantal = eengezins_aantal

        # calcualte percentage of extra housing worth per extra sqaure meter space
        self.percentage_eengezins = self.eengezins * 0.03

        # make default total prices
        self.total_eengezins = eengezins_aantal * self.eengezins

        # getting the coordinates from placing class
        coordinateslijst = Placing.eensgezinswoningen(self, eengezins_aantal)

        for coordinates in coordinateslijst:

            # locate the basepoints
            # top_left = [coordinates[0], coordinates[1]]
            # print(top_left)
            # top_right = [coordinates[0], coordinates[1] + 8]
            # bottom_left = [coordinates[0] + 8, coordinates[1]]
            # bottom_right = [coordinates[0] + 8, coordinates[1] + 8]
            # top_middle = [coordinates[0], coordinates[1] + 4]
            # left_middle = [coordinates[0] + 4, coordinates[1]]
            # right_middle = [coordinates[0] + 4, coordinates[1] + 8]
            # bottom_middle = [coordinates[0] + 8, coordinates[1] + 4]

            top_left = [coordinates[1], coordinates[0]]
            print(top_left)
            top_right = [coordinates[1], coordinates[0] + 8]
            bottom_left = [coordinates[1] + 8, coordinates[0]]
            bottom_right = [coordinates[1] + 8, coordinates[0] + 8]
            top_middle = [coordinates[1], coordinates[0] + 4]
            left_middle = [coordinates[1] + 4, coordinates[0]]
            right_middle = [coordinates[1] + 4, coordinates[0] + 8]
            bottom_middle = [coordinates[1] + 8, coordinates[0] + 4]

            # make default value for checking whether the area checked around the house is free
            vrij = True
            meter_counter = 3

            # check whether there is free ground around the house
            while vrij == True:
            
                # if there are any houses in the area of the search command then stop searching
                if wijk1[top_left[0]][top_left[1] - meter_counter] or wijk1[top_left[0] - meter_counter][top_left[1]] or wijk1[top_right[0]][top_right[1] + meter_counter] or wijk1[top_right[0] - meter_counter][top_right[1]] or wijk1[bottom_left[0]][bottom_left[1] - meter_counter] or wijk1[bottom_left[0] + meter_counter][bottom_left[1]] or wijk1[bottom_right[0]][bottom_right[1] + meter_counter] or wijk1[bottom_right[0] + meter_counter][bottom_right[1]] or wijk1[top_middle[0] - meter_counter][top_middle[1]] or wijk1[left_middle[0]][left_middle[1] - meter_counter] or wijk1[right_middle[0]][right_middle[1] + meter_counter] or wijk1[bottom_middle[0] + meter_counter][bottom_middle[1] - meter_counter] != 0:
                    print('begin')
                    print(wijk1[top_left[0]][top_left[1] - meter_counter])
                    print(wijk1[top_left[0] - meter_counter][top_left[1]])
                    print(wijk1[top_right[0]][top_right[1] + meter_counter])
                    print(wijk1[top_right[0] - meter_counter][top_right[1]])
                    print(wijk1[bottom_left[0]][bottom_left[1] - meter_counter])
                    print(wijk1[bottom_left[0] + meter_counter][bottom_left[1]])
                    print(wijk1[bottom_right[0]][bottom_right[1] + meter_counter])
                    print(wijk1[bottom_right[0] + meter_counter][bottom_right[1]])
                    print(wijk1[top_middle[0] - meter_counter][top_middle[1]])
                    print(wijk1[left_middle[0]][left_middle[1] - meter_counter])
                    print(wijk1[right_middle[0]][right_middle[1] + meter_counter])
                    print(wijk1[bottom_middle[0] + meter_counter][bottom_middle[1] - meter_counter])
                    
                    
                    vrij = False
                    print("break")
                    print(meter_counter)
                    print('eind')
                # if wijk1[top_left[0]][top_left[1] - meter_counter] or wijk1[top_left[0] - meter_counter][top_left[1]] or wijk1[top_right[0]][top_left[1] + meter_counter] or wijk1[top_right[0] - meter_counter][top_right[1]] or wijk1[bottom_left[0]][bottom_left[1] - meter_counter] or wijk1[bottom_left[0] + meter_counter][bottom_left[1]] or wijk1[bottom_right[0]][bottom_right[1] + meter_counter] or wijk1[bottom_right[0] + meter_counter][bottom_right[1]] or wijk1[top_middle[0] - meter_counter][top_middle[1]] or wijk1[left_middle[0]][left_middle[1] - meter_counter] or wijk1[right_middle[0]][right_middle[1] + meter_counter] or wijk1[bottom_middle[0] + meter_counter][bottom_middle[1] - meter_counter] == 1 or 2 or 3:
                #     print(wijk1[top_left[0]][top_left[1] - meter_counter])
                #     print(wijk1[top_left[0] - meter_counter][top_left[1]])
                #     print(wijk1[top_right[0]][top_right[1] + meter_counter])
                #     print(wijk1[top_right[0] - meter_counter][top_right[1]])
                #     print(wijk1[bottom_left[0]][bottom_left[1] - meter_counter])
                #     print(wijk1[bottom_left[0] + meter_counter][bottom_left[1]])
                #     print(wijk1[bottom_right[0]][bottom_right[1] + meter_counter])
                #     print(wijk1[bottom_right[0] + meter_counter][bottom_right[1]])
                #     print(wijk1[top_middle[0] - meter_counter][top_middle[1]])
                #     print(wijk1[left_middle[0]][left_middle[1] - meter_counter])
                #     print(wijk1[right_middle[0]][right_middle[1] + meter_counter])
                #     print(wijk1[bottom_middle[0] + meter_counter][bottom_middle[1] - meter_counter])
                    
                    # self.total_eengezins = self.total_eengezins + self.percentage_eengezins
                    # meter_counter += 1 
                    # print('begin money')
                    # print(self.total_eengezins)
                    # print(meter_counter)
                    # print('eind money')
                    
                    # vrij = False
                    # print("break")
                    # print(meter_counter)
                    # print('eind')

                
                # if there are no houses found in the area of the search command an extra amount of money to the total worth of the eengezinswoningen
                else:
                
                    self.total_eengezins = self.total_eengezins + self.percentage_eengezins
                    meter_counter += 1 
                    print('begin money')
                    print(self.total_eengezins)
                    print(meter_counter)
                    print('eind money')
                    

    # def bungalow_cost(self, bungalow_aantal):

    #     # make default prices of houses
    #     self.bungalow = 399000

    #     # calcualte percentage of extra housing worth per extra sqaure meter space
    #     self.percentage_bungalow = self.bungalow * 0.04

    #     # make default total prices
    #     self.total_bungalow = bungalow_aantal * self.bungalow




    def housing_costs(self, eengezins_aantal, bungalow_aantal, maison_aantal):

        # make default prices of houses
        self.eengezins = 285000
        self.bungalow = 399000
        self.maison = 610000
        self.eengezins_aantal = eengezins_aantal

        # calcualte percentage of extra housing worth per extra sqaure meter space
        self.percentage_eengezins = self.eengezins * 0.03
        self.percentage_bungalow = self.bungalow * 0.04
        self.percentage_maison = self.maison * 0.06

        # make default total prices
        self.total_eengezins = eengezins_aantal * self.eengezins
        self.total_bungalow = bungalow_aantal * self.bungalow
        self.total_maison = maison_aantal * self.maison

        coordinateslijst = Placing.eensgezinswoningen(self, eengezins_aantal)
        print(coordinateslijst)
        for coordinates in coordinateslijst:
            # locate the basepoints
            top_left = [coordinates[0], coordinates[1]]
            top_right = [coordinates[0], coordinates[1] + 8]
            bottom_left = [coordinates[0] + 8, coordinates[1]]
            bottom_right = [coordinates[0] + 8, coordinates[1] + 8]
            top_middle = [coordinates[0], coordinates[1] + 4]
            left_middle = [coordinates[0] + 4, coordinates[1]]
            right_middle = [coordinates[0] + 4, coordinates[1] + 8]
            bottom_middle = [coordinates[0] + 8, coordinates[1] + 4]

            # make default value for checking whether the area checked around the house is free
            vrij = True
            meter_counter = 3

            # check whether there is free ground around the house
            while vrij == True:
            
                # if there are any houses in the area of the search command then stop searching
                if wijk1[top_left[0]][top_left[1] - meter_counter] or wijk1[top_left[0] - meter_counter][top_left[1]] or wijk1[top_right[0]][top_left[1] + meter_counter] or wijk1[top_right[0] - meter_counter][top_right[1]] or wijk1[bottom_left[0]][bottom_left[1] - meter_counter] or wijk1[bottom_left[0] + meter_counter][bottom_left[1]] or wijk1[bottom_right[0]][bottom_right[1] + meter_counter] or wijk1[bottom_right[0] + meter_counter][bottom_right[1]] or wijk1[top_middle[0] - meter_counter][top_middle[1]] or wijk1[left_middle[0]][left_middle[1] - meter_counter] or wijk1[right_middle[0]][right_middle[1] + meter_counter] or wijk1[bottom_middle[0] + meter_counter][bottom_middle[1] - meter_counter] != 0:
                    vrij = False
                    print("break")
                    print(meter_counter)
                
                # if there are no houses found in the area of the search command an extra amount of money to the total worth of the eengezinswoningen
                else:
                    self.total_eengezins = self.total_eengezins + self.percentage_eengezins
                    meter_counter += 1 
                    print(self.total_eengezins)
                    print(meter_counter)



def main():
    # adding houses
    price = Kosten(12, 5, 3)
    place = Placing(12, 5, 3)
    
    place.water()
    place.eensgezinswoningen(12)
    place.bungalow(5)
    place.maison(3)

    price.eengezins_cost(12)


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