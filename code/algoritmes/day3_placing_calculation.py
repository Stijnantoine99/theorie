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
            vrij = False

            while vrij == False:
                x = random.randrange(32,150)
                y_oud = random.randrange(2,170)
                print('Eengezins')
                print(y_oud,x)

                nested_break = False

                for i in range(0,13):
                    if wijk1[y_oud - 2][x - 2 + i] == 1 or wijk1[y_oud - 2][x - 2 + i] == 2 or wijk1[y_oud - 2][x - 2 + i] == 3:
                        vrij = False
                        nested_break = True
                        break
                    else:
                        vrij = True
                    for j in range(0,13):
                        if wijk1[y_oud - 2 + j][x - 2 + i] == 1 or wijk1[y_oud - 2 + j][x - 2 + i] == 2 or wijk1[y_oud - 2 + j][x - 2 + i] == 3:
                            vrij = False
                            nested_break = True
                            break
                        else:
                            vrij = True
                    if nested_break:
                        break

            eensgezins_coordinatenlijst.append([x,y_oud])
            # print(x, y_oud)

            for i in range(0,12):

                # print(wijk1[y_oud][x])
                if i == 0 or i == 1 or i == 11 or i == 10:
                    wijk1[y_oud][x] = 5
                    # print(wijk1[y_oud][x])
                    
                    # for j in range(0,12):

                    #     if j == 0 or j == 1 or j == 11 or j == 10:
                    #         y = y_oud + j
                    #         wijk1[y][x] = 5
                    #         print(wijk1[y][x])


                else:
                    wijk1[y_oud][x] = 1
                    # print(wijk1[y_oud][x])
                    y = y_oud + j
                    wijk1[y][x] = 1
                    # print(wijk1[y][x])


                for j in range(0,12):

                    if j == 0 or j == 1 or j == 11 or j == 10 or i == 0 or i == 1 or i == 11 or i == 10:
                        y = y_oud + j
                        wijk1[y][x] = 5
                        # print(wijk1[y][x])
                        

                    else: 
                        y = y_oud + j
                        wijk1[y][x] = 1
                        # print(wijk1[y][x])
                        
                x += 1
            counter += 1  



            # for i in range(0,8):
            #     wijk1[y_oud][x] = 1
            #     for j in range(0,8):
            #         y = y_oud + j
            #         wijk1[y][x] = 1
                      
            #     x += 1
            # counter += 1  

        return eensgezins_coordinatenlijst
        

    # adding maison

    def maison(self, aantal_maison):
        maison_coordinatenlijst = []
        counter_maison = 0 

        while counter_maison < aantal_maison: 
            vrij = False

            while vrij == False:
                x = random.randrange(32,142)
                y_oud = random.randrange(6,164)
                print('Maison')
                print(y_oud,x)

                nested_break = False

                for i in range(0,25):
                    print(y_oud - 6, x - 6)
                    
                    if wijk1[y_oud - 6][x - 6 + i] == 1 or wijk1[y_oud - 6][x - 6 + i] == 2 or wijk1[y_oud - 6][x - 6 + i] == 3:
                        vrij = False
                        nested_break = True
                        print("break")
                        break
                    else:
                        vrij = True   
                    for j in range(0,23):
                        # print(wijk1[y_oud - 6 + j][x - 6 + i])
                        # print(y_oud - 6 + j, x-6 + i, wijk1[y_oud - 6 + j][x - 6 + i])
                        # print(x - 6 + i)
                        if wijk1[y_oud - 6 + j][x - 6 + i] == 1 or wijk1[y_oud - 6 + j][x - 6 + i] == 2 or wijk1[y_oud - 6 + j][x - 6 + i] == 3:
                            vrij = False
                            nested_break = True
                            print("break")
                            break
                        else:
                            vrij = True
                    print(vrij)
                    if nested_break:
                        print("nested break")
                        break


        
        # while counter_maison < aantal_maison:
        #     x = random.randrange(32,142)
        #     y_oud = random.randrange(6,164)

        #     while wijk1[y_oud][x] or wijk1[y_oud+5][x] or wijk1[y_oud][x+6] or wijk1[y_oud+10][x] or wijk1[y_oud][x+12] or wijk1[y_oud+10][x+6] or wijk1[y_oud+5][x+12] or wijk1[y_oud+10][x+12] != 0:
        #         x = random.randrange(32,142)
        #         y_oud = random.randrange(2,164)
            
            maison_coordinatenlijst.append([x,y_oud])

            for i in range(0,12):
                x += 1
                wijk1[y_oud][x] = 3
                for j in range(0,10):
                    y = y_oud + j
                    wijk1[y][x] = 3 
            counter_maison += 1  

        return maison_coordinatenlijst


    # adding bungalow
    def bungalow(self, aantal_bungalow):
        bungalow_coordinatenlijst = []
        counter_bungalow = 0 

        while counter_bungalow < aantal_bungalow: 
            vrij = False

            while vrij == False:
                x = random.randrange(32,146)
                y_oud = random.randrange(3,170)
                print('Bungalow')
                print(y_oud,x)

                nested_break = False

                for i in range(0,18):
                    if wijk1[y_oud - 3][x - 3 + i] == 1 or wijk1[y_oud - 3][x - 3 + i] == 2 or wijk1[y_oud - 3][x - 3 + i] == 3:
                        vrij = False
                        break

                    # elif nested_break:
                    #     break    

                    else:
                        vrij = True

                    for j in range(0,14):
                        if wijk1[y_oud - 3 + j][x - 3 + i] == 1 or wijk1[y_oud - 3 + j][x - 3 + i] == 2 or wijk1[y_oud - 3 + j][x - 3 + i] == 3:
                            vrij = False
                            nested_break = True
                            break
                        else:
                            vrij = True

                    if nested_break:
                        break






        # bungalow_coordinatenlijst = []
        # counter_bungalow = 0
        # while counter_bungalow < aantal_bungalow:
        #     x = random.randrange(32,146)
        #     y_oud = random.randrange(3,170)

        #     while wijk1[y_oud][x] or wijk1[y_oud][x+5] or wijk1[y_oud+7][x] or wijk1[y_oud][x+11] or wijk1[y_oud+7][x+11] or wijk1[y_oud+7][x+5] != 0:
        #         x = random.randrange(32,146)
        #         y_oud = random.randrange(2,170)

            bungalow_coordinatenlijst.append([x,y_oud])
            
            for i in range(0,11):
                x += 1
                wijk1[y_oud][x] = 2
                for j in range(0,7):
                    y = y_oud + j
                    wijk1[y][x] = 2
            counter_bungalow += 1  

        return bungalow_coordinatenlijst

    # print(bungalow_coordinatenlijst[4][0])
# def calculate():

class Kosten():

    def __init__(self, eengezins_aantal, bungalow_aantal, maison_aantal):
        self.eengezins_aantal = eengezins_aantal
        self.bungalow_aantal = bungalow_aantal
        self.maison_aantal = maison_aantal

        
    def eengezins_cost(self, coordinaten, eengezins_aantal):
        # make default prices of houses
        self.eengezins = 285000 
        self.eengezins_aantal = eengezins_aantal

        # calcualte percentage of extra housing worth per extra sqaure meter space
        self.percentage_eengezins = self.eengezins * 0.03

        # make default total prices
        self.total_eengezins = eengezins_aantal * self.eengezins

        # getting the coordinates from placing class
        
        coordinateslijst = coordinaten

        # print(coordinateslijst)

        

        # check the outline of every eengezinshuis

        for coordinates in coordinateslijst:

            # create default variables for checking the outline

            range_eengezins = 14
            locatie_outline_boven_x_as =  -3
            locatie_outline_boven_y_as = -3
            locatie_outline_onder_x_as = 11
            locatie_outline_onder_y_as = 11
            constante_x_links = -3
            constante_x_rechts = 11

            # Keep checking if there are no houses found

            check = True
            counter_x = 0
            counter_y = 0 
            counter_x_onder = 0
            counter_y_onder = 0
            
            meter = 3
            # print('yo')
            while check == True:
                # print(coordinates)

                # check area of entire outline from the top left
                for i in range(range_eengezins):

                    # if a house has been found in the area
                    if wijk1[coordinates[1] + locatie_outline_boven_x_as][coordinates[0] + locatie_outline_boven_y_as] != 0:
                        check = False
                        # print("House found in the area (x-as, boven)")
                        break

                    else:
                        # update by incrementing variable to search area
                        locatie_outline_boven_x_as += 1
                        counter_x += 1 
                        # print("x boven")
                        # print(wijk1[coordinates[1] + locatie_outline_boven_x_as][coordinates[0]+ locatie_outline_boven_y_as])

 

                for i in range(range_eengezins):

                    if wijk1[coordinates[1] + constante_x_links][coordinates[0] + locatie_outline_boven_y_as] != 0:
                        check = False
                        # print("House found in the area (y-as, links)")
                        break
                    else:
                        # update by incrementing variable to search area
                        locatie_outline_boven_y_as += 1
                        counter_y += 1 
                        # print("y links")
                        # print(wijk1[coordinates[1] + constante_x_links][coordinates[0] + locatie_outline_boven_y_as])

                
                for i in range(range_eengezins):

                    # if a house has been found in the area
                    if wijk1[coordinates[1] + locatie_outline_onder_x_as][coordinates[0] + locatie_outline_onder_y_as] != 0:
                        check = False
                        # print("House found in the area (x-as, onder)")
                        break

                    else:
                        # update by incrementing variable to search area
                        locatie_outline_onder_x_as -= 1
                        counter_x_onder -= 1 
                        # print("x onder")
                        # print(wijk1[coordinates[1] + locatie_outline_onder_x_as][coordinates[0] + locatie_outline_onder_y_as])

 

                for i in range(range_eengezins):

                    if wijk1[coordinates[1] + constante_x_rechts][coordinates[0] + locatie_outline_onder_y_as] != 0:
                        check = False
                        # print("House found in the area (y-as, rechts)")
                        break 

                    else:
                        # update by incrementing variable to search area
                        locatie_outline_onder_y_as -= 1
                        counter_y_onder -= 1 
                        # print("y rechts")
                        # print(wijk1[coordinates[1] + constante_x_rechts][coordinates[0] + locatie_outline_onder_y_as])
 


                locatie_outline_boven_x_as = locatie_outline_boven_x_as - counter_x - 1
                locatie_outline_boven_y_as = locatie_outline_boven_y_as - counter_y - 1
                constante_x_links = locatie_outline_boven_x_as

                locatie_outline_onder_x_as = locatie_outline_onder_x_as - counter_x_onder - 1
                locatie_outline_onder_y_as = locatie_outline_onder_y_as - counter_x_onder - 1
                constante_x_rechts = locatie_outline_onder_x_as

                counter_x = 0
                counter_y = 0 
                counter_x_onder = 0
                counter_y_onder = 0

                meter += 1 
                # print(meter)
                # When no houses found expand outline by 1 meter on every side
                range_eengezins = range_eengezins + 2
                # print(coordinates)
                self.total_eengezins = self.total_eengezins + self.percentage_eengezins
                # print(self.total_eengezins)

        return self.total_eengezins
        
        
        
        # coordinateslijst = Placing.eensgezinswoningen(self, eengezins_aantal)

        # for coordinates in coordinateslijst:

        #     # locate the basepoints
        #     # top_left = [coordinates[0], coordinates[1]]
        #     # print(top_left)
        #     # top_right = [coordinates[0], coordinates[1] + 8]
        #     # bottom_left = [coordinates[0] + 8, coordinates[1]]
        #     # bottom_right = [coordinates[0] + 8, coordinates[1] + 8]
        #     # top_middle = [coordinates[0], coordinates[1] + 4]
        #     # left_middle = [coordinates[0] + 4, coordinates[1]]
        #     # right_middle = [coordinates[0] + 4, coordinates[1] + 8]
        #     # bottom_middle = [coordinates[0] + 8, coordinates[1] + 4]

        #     top_left = [coordinates[1], coordinates[0]]
        #     print(top_left)
        #     top_right = [coordinates[1], coordinates[0] + 8]
        #     bottom_left = [coordinates[1] + 8, coordinates[0]]
        #     bottom_right = [coordinates[1] + 8, coordinates[0] + 8]
        #     top_middle = [coordinates[1], coordinates[0] + 4]
        #     left_middle = [coordinates[1] + 4, coordinates[0]]
        #     right_middle = [coordinates[1] + 4, coordinates[0] + 8]
        #     bottom_middle = [coordinates[1] + 8, coordinates[0] + 4]

        #     # make default value for checking whether the area checked around the house is free
        #     vrij = True
        #     meter_counter = 3

        #     # check whether there is free ground around the house
        #     while vrij == True:
            
        #         # if there are any houses in the area of the search command then stop searching
        #         if wijk1[top_left[0]][top_left[1] - meter_counter] or wijk1[top_left[0] - meter_counter][top_left[1]] or wijk1[top_right[0]][top_right[1] + meter_counter] or wijk1[top_right[0] - meter_counter][top_right[1]] or wijk1[bottom_left[0]][bottom_left[1] - meter_counter] or wijk1[bottom_left[0] + meter_counter][bottom_left[1]] or wijk1[bottom_right[0]][bottom_right[1] + meter_counter] or wijk1[bottom_right[0] + meter_counter][bottom_right[1]] or wijk1[top_middle[0] - meter_counter][top_middle[1]] or wijk1[left_middle[0]][left_middle[1] - meter_counter] or wijk1[right_middle[0]][right_middle[1] + meter_counter] or wijk1[bottom_middle[0] + meter_counter][bottom_middle[1] - meter_counter] != 0:
        #             print('begin')
        #             print(wijk1[top_left[0]][top_left[1] - meter_counter])
        #             print(wijk1[top_left[0] - meter_counter][top_left[1]])
        #             print(wijk1[top_right[0]][top_right[1] + meter_counter])
        #             print(wijk1[top_right[0] - meter_counter][top_right[1]])
        #             print(wijk1[bottom_left[0]][bottom_left[1] - meter_counter])
        #             print(wijk1[bottom_left[0] + meter_counter][bottom_left[1]])
        #             print(wijk1[bottom_right[0]][bottom_right[1] + meter_counter])
        #             print(wijk1[bottom_right[0] + meter_counter][bottom_right[1]])
        #             print(wijk1[top_middle[0] - meter_counter][top_middle[1]])
        #             print(wijk1[left_middle[0]][left_middle[1] - meter_counter])
        #             print(wijk1[right_middle[0]][right_middle[1] + meter_counter])
        #             print(wijk1[bottom_middle[0] + meter_counter][bottom_middle[1] - meter_counter])
                    
                    
        #             vrij = False
        #             print("break")
        #             print(meter_counter)
        #             print('eind')
        #         # if wijk1[top_left[0]][top_left[1] - meter_counter] or wijk1[top_left[0] - meter_counter][top_left[1]] or wijk1[top_right[0]][top_left[1] + meter_counter] or wijk1[top_right[0] - meter_counter][top_right[1]] or wijk1[bottom_left[0]][bottom_left[1] - meter_counter] or wijk1[bottom_left[0] + meter_counter][bottom_left[1]] or wijk1[bottom_right[0]][bottom_right[1] + meter_counter] or wijk1[bottom_right[0] + meter_counter][bottom_right[1]] or wijk1[top_middle[0] - meter_counter][top_middle[1]] or wijk1[left_middle[0]][left_middle[1] - meter_counter] or wijk1[right_middle[0]][right_middle[1] + meter_counter] or wijk1[bottom_middle[0] + meter_counter][bottom_middle[1] - meter_counter] == 1 or 2 or 3:
        #         #     print(wijk1[top_left[0]][top_left[1] - meter_counter])
        #         #     print(wijk1[top_left[0] - meter_counter][top_left[1]])
        #         #     print(wijk1[top_right[0]][top_right[1] + meter_counter])
        #         #     print(wijk1[top_right[0] - meter_counter][top_right[1]])
        #         #     print(wijk1[bottom_left[0]][bottom_left[1] - meter_counter])
        #         #     print(wijk1[bottom_left[0] + meter_counter][bottom_left[1]])
        #         #     print(wijk1[bottom_right[0]][bottom_right[1] + meter_counter])
        #         #     print(wijk1[bottom_right[0] + meter_counter][bottom_right[1]])
        #         #     print(wijk1[top_middle[0] - meter_counter][top_middle[1]])
        #         #     print(wijk1[left_middle[0]][left_middle[1] - meter_counter])
        #         #     print(wijk1[right_middle[0]][right_middle[1] + meter_counter])
        #         #     print(wijk1[bottom_middle[0] + meter_counter][bottom_middle[1] - meter_counter])
                    
        #             # self.total_eengezins = self.total_eengezins + self.percentage_eengezins
        #             # meter_counter += 1 
        #             # print('begin money')
        #             # print(self.total_eengezins)
        #             # print(meter_counter)
        #             # print('eind money')
                    
        #             # vrij = False
        #             # print("break")
        #             # print(meter_counter)
        #             # print('eind')

                
        #         # if there are no houses found in the area of the search command an extra amount of money to the total worth of the eengezinswoningen
        #         else:
                
        #             self.total_eengezins = self.total_eengezins + self.percentage_eengezins
        #             meter_counter += 1 
        #             print('begin money')
        #             print(self.total_eengezins)
        #             print(meter_counter)
        #             print('eind money')
                    

    def bungalow_cost(self, coordinaten, bungalow_aantal):

        # make default prices of houses
        self.bungalow = 399000
        self.bungalow_aantal = bungalow_aantal

        # calcualte percentage of extra housing worth per extra sqaure meter space
        self.percentage_bungalow = self.bungalow * 0.04

        # make default total prices
        self.total_bungalow = bungalow_aantal * self.bungalow


        coordinateslijst = coordinaten

        for coordinates in coordinaten:

            range_bungalow_x = 19
            range_bungalow_y = 15
            locatie_outline_boven_x_as =  -4
            locatie_outline_boven_y_as = -4
            locatie_outline_onder_x_as = 15
            locatie_outline_onder_y_as = 11
            constante_x_links = -4
            constante_x_rechts = 15

            check = True
            counter_x = 0
            counter_y = 0 
            counter_x_onder = 0
            counter_y_onder = 0


            while check == True:

                for i in range(range_bungalow_x):

                    if wijk1[coordinates[1] + locatie_outline_boven_x_as][coordinates[0] + locatie_outline_boven_y_as] != 0:
                        check = False
                        # print("House found in the area (x-as, boven)")
                        break
                    
                    else:
                        locatie_outline_boven_x_as += 1
                        counter_x += 1 
                        # print("x boven")
                        # print(wijk1[coordinates[1] + locatie_outline_boven_x_as][coordinates[0]+ locatie_outline_boven_y_as])

                
                for i in range(range_bungalow_y):

                    if wijk1[coordinates[1] + constante_x_links][coordinates[0] + locatie_outline_boven_y_as] != 0:
                        check = False
                        # print("House found in the area (y-as, links)")
                        break
                    else:
                        # update by incrementing variable to search area
                        locatie_outline_boven_y_as += 1
                        counter_y += 1 
                        # print("y links")
                        # print(wijk1[coordinates[1] + constante_x_links][coordinates[0] + locatie_outline_boven_y_as])

                for i in range(range_bungalow_x):
                    # if a house has been found in the area
                    if wijk1[coordinates[1] + locatie_outline_onder_x_as][coordinates[0] + locatie_outline_onder_y_as] != 0:
                        check = False
                        # print("House found in the area (x-as, onder)")
                        break

                    else:
                        # update by incrementing variable to search area
                        locatie_outline_onder_x_as -= 1
                        counter_x_onder -= 1 
                        # print("x onder")
                        # print(wijk1[coordinates[1] + locatie_outline_onder_x_as][coordinates[0] + locatie_outline_onder_y_as])

                for i in range(range_bungalow_y):
                    # if a house has been found in the area
                    if wijk1[coordinates[1] + constante_x_rechts][coordinates[0] + locatie_outline_onder_y_as] != 0:
                        check = False
                        # print("House found in the area (y-as, rechts)")
                        break 

                    else:
                        # update by incrementing variable to search area
                        locatie_outline_onder_y_as -= 1
                        counter_y_onder -= 1 
                        # print("y rechts")
                        # print(wijk1[coordinates[1] + constante_x_rechts][coordinates[0] + locatie_outline_onder_y_as])

                
                locatie_outline_boven_x_as = locatie_outline_boven_x_as - counter_x - 1
                locatie_outline_boven_y_as = locatie_outline_boven_y_as - counter_y - 1
                constante_x_links = locatie_outline_boven_x_as

                locatie_outline_onder_x_as = locatie_outline_onder_x_as - counter_x_onder - 1
                locatie_outline_onder_y_as = locatie_outline_onder_y_as - counter_x_onder - 1
                constante_x_rechts = locatie_outline_onder_x_as

                counter_x = 0
                counter_y = 0 
                counter_x_onder = 0
                counter_y_onder = 0

                range_bungalow_x += 2
                range_bungalow_y += 2  

                self.total_bungalow = self.total_bungalow + self.percentage_bungalow
                # print(self.total_bungalow)
        
        return self.total_bungalow

    def maison_cost(self, coordinaten, maison_aantal):
        
        # make default prices of houses
        self.maison = 610000
        self.maison_aantal = maison_aantal

        # calcualte percentage of extra housing worth per extra sqaure meter space
        self.percentage_maison = self.maison * 0.06

        # make default total prices
        self.total_maison = maison_aantal * self.maison

        coordinateslijst = coordinaten

        for coordinates in coordinaten:

            range_maison_x = 26
            range_maison_y = 24
            locatie_outline_boven_x_as = -7
            locatie_outline_boven_y_as = -7
            locatie_outline_onder_x_as = 19
            locatie_outline_onder_y_as = 17
            constante_x_links = -7
            constante_x_rechts = 19

            check = True
            counter_x = 0
            counter_y = 0 
            counter_x_onder = 0
            counter_y_onder = 0

            while check == True:

                for i in range(range_maison_x):

                    if wijk1[coordinates[1] + locatie_outline_boven_x_as][coordinates[0] + locatie_outline_boven_y_as] != 0:
                        check = False
                        # print("House found in the area (x-as, boven)")
                        break
                    
                    else:
                        locatie_outline_boven_x_as += 1
                        counter_x += 1 
                        # print("x boven")
                        # print(wijk1[coordinates[1] + locatie_outline_boven_x_as][coordinates[0]+ locatie_outline_boven_y_as])

                
                for i in range(range_maison_y):

                    if wijk1[coordinates[1] + constante_x_links][coordinates[0] + locatie_outline_boven_y_as] != 0:
                        check = False
                        # print("House found in the area (y-as, links)")
                        break
                    else:
                        # update by incrementing variable to search area
                        locatie_outline_boven_y_as += 1
                        counter_y += 1 
                        # print("y links")
                        # print(wijk1[coordinates[1] + constante_x_links][coordinates[0] + locatie_outline_boven_y_as])

                for i in range(range_maison_x):
                    # if a house has been found in the area
                    if wijk1[coordinates[1] + locatie_outline_onder_x_as][coordinates[0] + locatie_outline_onder_y_as] != 0:
                        check = False
                        # print("House found in the area (x-as, onder)")
                        break

                    else:
                        # update by incrementing variable to search area
                        locatie_outline_onder_x_as -= 1
                        counter_x_onder -= 1 
                        # print("x onder")
                        # print(wijk1[coordinates[1] + locatie_outline_onder_x_as][coordinates[0] + locatie_outline_onder_y_as])

                for i in range(range_maison_y):
                    # if a house has been found in the area
                    if wijk1[coordinates[1] + constante_x_rechts][coordinates[0] + locatie_outline_onder_y_as] != 0:
                        check = False
                        # print("House found in the area (y-as, rechts)")
                        break 

                    else:
                        # update by incrementing variable to search area
                        locatie_outline_onder_y_as -= 1
                        counter_y_onder -= 1 
                        # print("y rechts")
                        # print(wijk1[coordinates[1] + constante_x_rechts][coordinates[0] + locatie_outline_onder_y_as])

                
                locatie_outline_boven_x_as = locatie_outline_boven_x_as - counter_x - 1
                locatie_outline_boven_y_as = locatie_outline_boven_y_as - counter_y - 1
                constante_x_links = locatie_outline_boven_x_as

                locatie_outline_onder_x_as = locatie_outline_onder_x_as - counter_x_onder - 1
                locatie_outline_onder_y_as = locatie_outline_onder_y_as - counter_x_onder - 1
                constante_x_rechts = locatie_outline_onder_x_as

                counter_x = 0
                counter_y = 0 
                counter_x_onder = 0
                counter_y_onder = 0

                range_maison_x += 2
                range_maison_y += 2  

                self.total_maison = self.total_maison + self.percentage_maison
                # print(self.total_maison)

        return self.total_maison


    # def housing_costs(self, eengezins_aantal, bungalow_aantal, maison_aantal):

    #     # make default prices of houses
    #     self.eengezins = 285000
    #     self.bungalow = 399000
    #     self.maison = 610000
    #     self.eengezins_aantal = eengezins_aantal

    #     # calcualte percentage of extra housing worth per extra sqaure meter space
    #     self.percentage_eengezins = self.eengezins * 0.03
    #     self.percentage_bungalow = self.bungalow * 0.04
    #     self.percentage_maison = self.maison * 0.06

    #     # make default total prices
    #     self.total_eengezins = eengezins_aantal * self.eengezins
    #     self.total_bungalow = bungalow_aantal * self.bungalow
    #     self.total_maison = maison_aantal * self.maison

    #     coordinateslijst = Placing.eensgezinswoningen(self, eengezins_aantal)
    #     print(coordinateslijst)
    #     for coordinates in coordinateslijst:
    #         # locate the basepoints
    #         top_left = [coordinates[0], coordinates[1]]
    #         top_right = [coordinates[0], coordinates[1] + 8]
    #         bottom_left = [coordinates[0] + 8, coordinates[1]]
    #         bottom_right = [coordinates[0] + 8, coordinates[1] + 8]
    #         top_middle = [coordinates[0], coordinates[1] + 4]
    #         left_middle = [coordinates[0] + 4, coordinates[1]]
    #         right_middle = [coordinates[0] + 4, coordinates[1] + 8]
    #         bottom_middle = [coordinates[0] + 8, coordinates[1] + 4]

    #         # make default value for checking whether the area checked around the house is free
    #         vrij = True
    #         meter_counter = 3

    #         # check whether there is free ground around the house
    #         while vrij == True:
            
    #             # if there are any houses in the area of the search command then stop searching
    #             if wijk1[top_left[0]][top_left[1] - meter_counter] or wijk1[top_left[0] - meter_counter][top_left[1]] or wijk1[top_right[0]][top_left[1] + meter_counter] or wijk1[top_right[0] - meter_counter][top_right[1]] or wijk1[bottom_left[0]][bottom_left[1] - meter_counter] or wijk1[bottom_left[0] + meter_counter][bottom_left[1]] or wijk1[bottom_right[0]][bottom_right[1] + meter_counter] or wijk1[bottom_right[0] + meter_counter][bottom_right[1]] or wijk1[top_middle[0] - meter_counter][top_middle[1]] or wijk1[left_middle[0]][left_middle[1] - meter_counter] or wijk1[right_middle[0]][right_middle[1] + meter_counter] or wijk1[bottom_middle[0] + meter_counter][bottom_middle[1] - meter_counter] != 0:
    #                 vrij = False
    #                 print("break")
    #                 print(meter_counter)
                
    #             # if there are no houses found in the area of the search command an extra amount of money to the total worth of the eengezinswoningen
    #             else:
    #                 self.total_eengezins = self.total_eengezins + self.percentage_eengezins
    #                 meter_counter += 1 
    #                 print(self.total_eengezins)
    #                 print(meter_counter)



def main():
    # adding houses
    price = Kosten(12, 5, 3)
    place = Placing(12, 5, 3)
    # place = Placing(60, 25, 13)
    
    place.water()
    coordinaten_eensgezin = place.eensgezinswoningen(12)
    coordinaten_bungalow = place.bungalow(5)
    coordinaten_maison = place.maison(3)

    omzet_eengezin = price.eengezins_cost(coordinaten_eensgezin, 12)
    omzet_bungalow = price.bungalow_cost(coordinaten_bungalow, 5)
    omzet_maison = price.maison_cost(coordinaten_maison, 3)

    totaal = omzet_eengezin + omzet_bungalow + omzet_maison
    # print(omzet_eengezin)
    # print(omzet_bungalow)
    # print(omzet_maison)
    # print(totaal)

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