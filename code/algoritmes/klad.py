import random
import statistics
import csv
import numpy as np 
import matplotlib.pyplot as plt
import matplotlib.colors

class Placing: 

    """ This class consists out of methods which place the different houses on the created gridmap. This 
    is done by scanning the ground for empty space after which the houses are placed one by one.
    Furthermore the water is created and placed. """

    # save the amount of houses being placed when running the Placing class 
    def __init__(self, wijk1, aantal_eensgezins, aantal_maison, aantal_bungalow):
        
        self.wijk1 = wijk1
        self.aantal_eensgezins = aantal_eensgezins
        self.aantal_maison = aantal_maison
        self.aantal_bungalow = aantal_bungalow

    def water(self):

        """ This method adds an area of water to the created gridmap. """

        # create starting coordinate in the top left
        x_coor = -1
        y_coor = -1
        
        for i in range(0,32):
            
            # change the empty space value on the gridmap to the water value for every coordinate in the for loop
            self.wijk1[y_coor][x_coor] = 4
            x_coor += 1 
            y_coor = -1

            for i in range(0,180):
                y_coor += 1
                self.wijk1[y_coor][x_coor] = 4
                
        

    # adding eensgezinswoningen 

    def eensgezinswoningen(self, aantal_eensgezins, wijk1):

        """ This method searches the gridmap for empty areas by creating random coordinates. If the area
         around the randomized coordinate fits this specific type of house, the house is placed and saved
         in the coordinates list. """
        
        # create a coordinates list of the houses being placed
        eensgezins_coordinatenlijst = [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]
        coordinaten_maison = [[0,0],[0,0],[0,0]]
        coordinaten_bungalow =[[0,0],[0,0],[0,0],[0,0],[0,0]]
        coordinaten_eensgezin = eensgezins_coordinatenlijst

        counter = 0 
        
        # while the amount of houses needed to be placed has not been reached yet search for empty area
        while counter < aantal_eensgezins: 
            oud = 0
            oud_coor = 0 
            # print(oud_coor)

            if counter > 0:
                
                for i in range(0,50):
                    # set default value of empty gridmap area to False
                    vrij = False

                    # while no empty space has been found keep searching
                    while vrij == False:
                        
                        # create a random coordinate on the gridmap (not in the water)
                        x = random.randrange(32,150)
                        y_oud = random.randrange(2,170)


                        # set default value for nested break to False
                        nested_break = False

                        # check from the randomly chosen coordinate as the top left corner if there is empty space to place a house horizontally
                        for i in range(0,12):

                            # if the coordinate is no empty area to place a house break out of the scanning loop
                            if self.wijk1[y_oud - 2][x - 2 + i] == 1 or self.wijk1[y_oud - 2][x - 2 + i] == 2 or self.wijk1[y_oud - 2][x - 2 + i] == 3:

                                # change the nested break value to True
                                vrij = False
                                nested_break = True
                                break

                            # if the coordinate is empty
                            else:
                                
                                # change default value of empty gridmap area to True
                                vrij = True

                            # check from the randomly chosen coordinate as the top left corner if there is empty space to place a house vertically
                            for j in range(0,12):

                                # if the coordinate is no empty area to place a house break out of the scanning loop
                                if self.wijk1[y_oud - 2 + j][x - 2 + i] == 1 or self.wijk1[y_oud - 2 + j][x - 2 + i] == 2 or self.wijk1[y_oud - 2 + j][x - 2 + i] == 3:
                            
                                    # change the nested break value to True
                                    vrij = False
                                    nested_break = True
                                    break

                                # if the coordinate is empty
                                else:

                                    # change default value of empty gridmap area to True
                                    vrij = True
                            
                            # if there has been found no empty space break and find a new randomized coordinate
                            if nested_break:
                                break
                    
                    new_coor = [x, y_oud]
                    # print(new_coor)
                    # klad_coor_lijst.append(coor)

                    eensgezins_coordinatenlijst[counter] = new_coor

                
                    # print(eensgezins_coordinatenlijst[counter])

                    price = Kosten(wijk1, 12, 5, 3)
                    # print(price)
                    # hier Matthijs de ligt het probleem 
                    new = price.total(coordinaten_maison, coordinaten_bungalow, coordinaten_eensgezin)
                    # print("hoi")
                    # print(new)
                    # prijs_lijst.append(new)

                    if new > oud:
                        # print(oud)
                        oud = new
                        oud_coor = new_coor
                        # print(oud)
                        # print
                
                for i in range(0,len(eensgezins_coordinatenlijst)):
                    if eensgezins_coordinatenlijst[i] == [0,0]:
                        eensgezins_coordinatenlijst[i] = oud_coor

                eensgezins_coordinatenlijst[counter] = oud_coor
                
                # print("oud")
                # print(oud_coor)
                # print(oud)
                # print(eensgezins_coordinatenlijst[counter])
                # print(eensgezins_coordinatenlijst)

            # hoogste = max(prijs_lijst)
            # index = opbrengst.index(hoogste)
            # best_coor = klad_coor_lijst[index]
    

            else: 
                vrij = False

                # while no empty space has been found keep searching
                while vrij == False:
                    
                    # create a random coordinate on the gridmap (not in the water)
                    x = random.randrange(32,150)
                    y_oud = random.randrange(2,170)


                    # set default value for nested break to False
                    nested_break = False

                    # check from the randomly chosen coordinate as the top left corner if there is empty space to place a house horizontally
                    for i in range(0,12):

                        # if the coordinate is no empty area to place a house break out of the scanning loop
                        if self.wijk1[y_oud - 2][x - 2 + i] == 1 or self.wijk1[y_oud - 2][x - 2 + i] == 2 or self.wijk1[y_oud - 2][x - 2 + i] == 3:

                            # change the nested break value to True
                            vrij = False
                            nested_break = True
                            break

                        # if the coordinate is empty
                        else:
                            
                            # change default value of empty gridmap area to True
                            vrij = True

                        # check from the randomly chosen coordinate as the top left corner if there is empty space to place a house vertically
                        for j in range(0,12):

                            # if the coordinate is no empty area to place a house break out of the scanning loop
                            if self.wijk1[y_oud - 2 + j][x - 2 + i] == 1 or self.wijk1[y_oud - 2 + j][x - 2 + i] == 2 or self.wijk1[y_oud - 2 + j][x - 2 + i] == 3:
                        
                                # change the nested break value to True
                                vrij = False
                                nested_break = True
                                break

                            # if the coordinate is empty
                            else:

                                # change default value of empty gridmap area to True
                                vrij = True
                        
                        # if there has been found no empty space break and find a new randomized coordinate
                        if nested_break:
                            break

                eensgezins_coordinatenlijst[counter] = [x,y_oud]
                for i in range(0,len(eensgezins_coordinatenlijst)):
                    if eensgezins_coordinatenlijst[i] == [0,0]:
                        eensgezins_coordinatenlijst[i] = [x,y_oud]

            counter += 1 

            # if an empty area has been found save the randomized coordinate in the houses list
            for coor in eensgezins_coordinatenlijst:
                # print('begin')
                # print(coor)
                # print(eensgezins_coordinatenlijst)
                # print('eind')
                for i in range(0,12):
                
                    # change the outer 2 meters of the area for the house to "vrijstaand"
                    if i == 0 or i == 1 or i == 11 or i == 10:
                        self.wijk1[coor[1] - 2][coor[0] - 2 + i] = 5

                    # change the area inside the "vrijstaand" area to "eengezins" value
                    else:
                        # wijk1[y_oud][x] = 1
                        # y = y_oud + j
                        self.wijk1[coor[1]- 2][coor[0] - 2 + i] = 1

                    for j in range(0,12):

                        # change the outer 2 meters of the area for the house to "vrijstaand"
                        if j == 0 or j == 1 or j == 11 or j == 10 or i == 0 or i == 1 or i == 11 or i == 10: 
                            self.wijk1[coor[1] - 2 + j][coor[0] - 2 + i] = 5                        

                        # change the area inside the "vrijstaand" area to "eengezins" value
                        else: 
                            self.wijk1[coor[1] - 2 + j][coor[0] - 2 + i] = 1
                    
            # H = np.array(wijk1)
            # plt.imshow(H)
            # plt.pcolor(H, cmap = "Greens_r")
            # plt.show() 
        totaal = price.total(coordinaten_maison, coordinaten_bungalow, coordinaten_eensgezin)
        print("totaal na eengezin")
        print(totaal)
        return eensgezins_coordinatenlijst

    def maison(self, aantal_maison, wijk1, coordinaten_eensgezin):

        """ This method searches the gridmap for empty areas by creating random coordinates. If the area
         around the randomized coordinate fits this specific type of house, the house is placed and saved
         in the coordinates list. """
        coordinaten_maison = [[0,0],[0,0],[0,0]]
        maison_coordinatenlijst = coordinaten_maison
        coordinaten_bungalow =[[0,0],[0,0],[0,0],[0,0],[0,0]]

        # create a coordinates list of the houses being placed
        counter_maison = 0

        # while the amount of houses needed to be placed has not been reached yet search for empty area
        while counter_maison < aantal_maison: 
            oud = 0
            oud_coor = 0 
            # set default value of empty gridmap area to False

            # if counter_maison > 0:
              
            # while the amount of houses needed to be placed has not been reached yet search for empty area
            for i in range(0,50):
                vrij = False
                while vrij == False:
                    
                    # create a random coordinate on the gridmap (not in the water)
                    x = random.randrange(32,142)
                    y_oud = random.randrange(6,164)

                    nested_break = False

                    # check from the randomly chosen coordinate as the top left corner if there is empty space to place a house horizontally
                    for i in range(0,24):
                        # print(y_oud - 6, x - 6)
                        
                        # if the coordinate is no empty area to place a house break out of the scanning loop
                        if self.wijk1[y_oud - 6][x - 6 + i] == 1 or self.wijk1[y_oud - 6][x - 6 + i] == 2 or self.wijk1[y_oud - 6][x - 6 + i] == 3:
                            
                            # change the nested break value to True
                            vrij = False
                            nested_break = True
                            break

                        # if the coordinate is empty
                        else:

                            # change default value of empty gridmap area to True
                            vrij = True   

                        # check from the randomly chosen coordinate as the top left corner if there is empty space to place a house vertically    
                        for j in range(0,22):

                            # if the coordinate is no empty area to place a house break out of the scanning loop
                            if self.wijk1[y_oud - 6 + j][x - 6 + i] == 1 or self.wijk1[y_oud - 6 + j][x - 6 + i] == 2 or self.wijk1[y_oud - 6 + j][x - 6 + i] == 3:
                                
                                # change the nested break value to True
                                vrij = False
                                nested_break = True
                                break
                            
                            # if the coordinate is empty
                            else:
                                vrij = True

                        # if there has been found no empty space break and find a new randomized coordinate
                        if nested_break:
                            break
                new_coor = [x, y_oud]
                maison_coordinatenlijst[counter_maison] = new_coor
                # for i in range(0,len(maison_coordinatenlijst)):
                #     if maison_coordinatenlijst[i] == [0,0]:
                #         maison_coordinatenlijst[i] = new_coor
                
                # if an empty area has been found save the randomized coordinate in the houses list
                # print(counter_maison)
                # print(new_coor)
                # print(maison_coordinatenlijst[1])

                # print(maison_coordinatenlijst[0])
                price = Kosten(wijk1, 12, 5, 3)
                new = price.total(coordinaten_maison, coordinaten_bungalow, coordinaten_eensgezin)
                
                if new > oud:
                    # print(oud)
                    oud = new
                    oud_coor = new_coor
                    # print(oud)
                    # print
                
            for i in range(0,len(maison_coordinatenlijst)):
                if maison_coordinatenlijst[i] == [0,0]:
                    maison_coordinatenlijst[i] = oud_coor
            maison_coordinatenlijst[counter_maison] = oud_coor

            # else:
            #     vrij = False
            #     while vrij == False:
                    
            #         # create a random coordinate on the gridmap (not in the water)
            #         x = random.randrange(32,142)
            #         y_oud = random.randrange(6,164)

            #         nested_break = False

            #         # check from the randomly chosen coordinate as the top left corner if there is empty space to place a house horizontally
            #         for i in range(0,24):
            #             # print(y_oud - 6, x - 6)
                        
            #             # if the coordinate is no empty area to place a house break out of the scanning loop
            #             if self.wijk1[y_oud - 6][x - 6 + i] == 1 or self.wijk1[y_oud - 6][x - 6 + i] == 2 or self.wijk1[y_oud - 6][x - 6 + i] == 3:
                            
            #                 # change the nested break value to True
            #                 vrij = False
            #                 nested_break = True
            #                 break

            #             # if the coordinate is empty
            #             else:

            #                 # change default value of empty gridmap area to True
            #                 vrij = True   

            #             # check from the randomly chosen coordinate as the top left corner if there is empty space to place a house vertically    
            #             for j in range(0,22):

            #                 # if the coordinate is no empty area to place a house break out of the scanning loop
            #                 if self.wijk1[y_oud - 6 + j][x - 6 + i] == 1 or self.wijk1[y_oud - 6 + j][x - 6 + i] == 2 or self.wijk1[y_oud - 6 + j][x - 6 + i] == 3:
                                
            #                     # change the nested break value to True
            #                     vrij = False
            #                     nested_break = True
            #                     break
                            
            #                 # if the coordinate is empty
            #                 else:
            #                     vrij = True

            #             # if there has been found no empty space break and find a new randomized coordinate
            #             if nested_break:
            #                 break
                
            #     print(counter_maison)
            #     print(x)
            #     print(y_oud)
            #     maison_coordinatenlijst[counter_maison] = [x, y_oud]
                    
            counter_maison += 1
   
            for coor in maison_coordinatenlijst:
                for i in range(0,24):

                    # change the outer 2 meters of the area for the house to "vrijstaand"
                    if i == 0 or i == 1 or i == 2 or i == 3 or i == 4 or i == 5 or i == 18 or i == 19 or i == 20 or i == 21 or i == 22 or i == 23:
                        self.wijk1[coor[1] - 6][coor[0] - 6 + i] = 5

                    # change the area inside the "vrijstaand" area to "eengezins" value
                    else:
                        # wijk1[y_oud][x] = 1
                        # y = y_oud + j
                        self.wijk1[coor[1] - 6][coor[0] - 6 + i] = 3

                    for j in range(0,22):

                        # change the outer 2 meters of the area for the house to "vrijstaand"
                        if j == 0 or j == 1 or j == 2 or j == 3 or j == 4 or j == 5 or j == 16 or j == 17 or j == 18 or j == 19 or j == 20 or j == 21 or i == 0 or i == 1 or i == 2 or i == 3 or i == 4 or i == 5 or i == 18 or i == 19 or i == 20 or i == 21 or i == 22 or i == 23:
                            self.wijk1[coor[1] - 6 + j][coor[0] - 6 + i] = 5                        

                        # change the area inside the "vrijstaand" area to "eengezins" value
                        else: 
                            self.wijk1[coor[1] - 6 + j][coor[0] - 6 + i] = 3
                
         
                
        totaal = price.total(coordinaten_maison, coordinaten_bungalow, coordinaten_eensgezin)
        print('totaal na maison')
        print(totaal)
        return maison_coordinatenlijst

    def bungalow(self, aantal_bungalow, wijk1, coordinaten_eensgezin, coordinaten_maison):

        """ This method searches the gridmap for empty areas by creating random coordinates. If the area
         around the randomized coordinate fits this specific type of house, the house is placed and saved
         in the coordinates list. """
         
        # create a coordinates list of the houses being placed
        coordinaten_bungalow =[[0,0],[0,0],[0,0],[0,0],[0,0]]
        bungalow_coordinatenlijst = coordinaten_bungalow
        counter_bungalow = 0 

        # while the amount of houses needed to be placed has not been reached yet search for empty area
        while counter_bungalow < aantal_bungalow: 
            oud = 0
            oud_coor = 0
            
            for i in range(0,50):
                vrij = False

                # set default value of empty gridmap area to False
                while vrij == False:
                    
                    # create a random coordinate on the gridmap (not in the water)
                    x = random.randrange(32,146)
                    y_oud = random.randrange(3,170)

                    nested_break = False

                    # check from the randomly chosen coordinate as the top left corner if there is empty space to place a house horizontally
                    for i in range(0,17):
                        
                        # if the coordinate is no empty area to place a house break out of the scanning loop
                        if self.wijk1[y_oud - 3][x - 3 + i] == 1 or self.wijk1[y_oud - 3][x - 3 + i] == 2 or self.wijk1[y_oud - 3][x - 3 + i] == 3:
                            vrij = False
                            break

                        # change the nested break value to True
                        else:
                            vrij = True

                        # check from the randomly chosen coordinate as the top left corner if there is empty space to place a house vertically    
                        for j in range(0,13):
                            
                            # if the coordinate is no empty area to place a house break out of the scanning loop
                            if self.wijk1[y_oud - 3 + j][x - 3 + i] == 1 or self.wijk1[y_oud - 3 + j][x - 3 + i] == 2 or self.wijk1[y_oud - 3 + j][x - 3 + i] == 3:
                                vrij = False
                                nested_break = True
                                break
                            
                            # change the nested break value to True
                            else:
                                vrij = True

                        # if there has been found no empty space break and find a new randomized coordinate
                        if nested_break:
                            break
                new_coor = [x, y_oud]
                bungalow_coordinatenlijst[counter_bungalow] = new_coor

                
                price = Kosten(wijk1, 12, 5, 3)
                new = price.total(coordinaten_maison, coordinaten_bungalow, coordinaten_eensgezin)
                
                if new > oud:
                    # print(oud)
                    oud = new
                    oud_coor = new_coor
                    # print(oud)
                    # print
                
            for i in range(0,len(bungalow_coordinatenlijst)):
                if bungalow_coordinatenlijst[i] == [0,0]:
                    bungalow_coordinatenlijst[i] = oud_coor

            bungalow_coordinatenlijst[counter_bungalow] = oud_coor
            # if an empty area has been found save the randomized coordinate in the houses list
            counter_bungalow += 1            
            
            print(bungalow_coordinatenlijst)
        
            for coor in bungalow_coordinatenlijst:
                print(coor)
                for i in range(0,17):
                    
                    # change the outer 2 meters of the area for the house to "vrijstaand"
                    if i == 0 or i == 1 or i == 2 or i == 14 or i == 15 or i == 16 :
                        self.wijk1[coor[1] - 3][coor[0] - 3 + i] = 5

                    # change the area inside the "vrijstaand" area to "eengezins" value
                    else:
                        # wijk1[y_oud][x] = 1
                        # y = y_oud + j
                        self.wijk1[coor[1] - 3][coor[0] - 3 + i] = 2

                    for j in range(0,13):

                        # change the outer 2 meters of the area for the house to "vrijstaand"
                        if j == 0 or j == 1 or j == 2 or j == 10 or j == 11 or j == 12 or i == 0 or i == 1 or i == 2 or i == 14 or i == 15 or i == 16:
                            self.wijk1[coor[1] - 3 + j][coor[0] - 3 + i] = 5                        

                        # change the area inside the "vrijstaand" area to "eengezins" value
                        else: 
                            self.wijk1[coor[1] - 3 + j][coor[0] - 3 + i] = 2
        totaal = price.total(coordinaten_maison, coordinaten_bungalow, coordinaten_eensgezin)
        print('totaal na bungalow')
        print(totaal)
        return bungalow_coordinatenlijst

class Kosten():

    """ This class consists out of methods which calculate the price of the houses placed on the gridmap.
    The total price is firstly set at a default value. After this the methods can be called upon which
    adds the extra price per house when going over the map. """


    # save the amount of houses being placed when running the Placing class 
    def __init__(self, wijk1, eengezins_aantal, bungalow_aantal, maison_aantal):
        
        self.wijk1 = wijk1 
        self.eengezins_aantal = eengezins_aantal
        self.bungalow_aantal = bungalow_aantal
        self.maison_aantal = maison_aantal

        
    def eengezins_cost(self, coordinaten, eengezins_aantal):

        """ This method calculates the extra price per house depending on the free space that surrounds
         the house. This is done by looking up the coordinates of every house in the coordinates list
         saved when placing the houses. From these coordinates the free space around the houses are checked
         and the total house price is being adjusted. """

        # make default prices of houses
        self.eengezins = 285000 
        self.eengezins_aantal = eengezins_aantal

        # calcualte percentage of extra housing worth per extra sqaure meter space
        self.percentage_eengezins = self.eengezins * 0.03

        # make default total prices
        self.total_eengezins = eengezins_aantal * self.eengezins

        # getting the coordinates from placing class
        coordinateslijst = coordinaten

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

            check = True
            counter_x = 0
            counter_y = 0 
            counter_x_onder = 0
            counter_y_onder = 0
        
            while check == True:

                # check area of x-axis topside from the top left
                for i in range(range_eengezins):

                    # if a house has been found in the area stop checking
                    try:    
                        if self.wijk1[coordinates[1] + locatie_outline_boven_x_as][coordinates[0] + locatie_outline_boven_y_as] == 1 or self.wijk1[coordinates[1] + locatie_outline_boven_x_as][coordinates[0] + locatie_outline_boven_y_as] == 2 or self.wijk1[coordinates[1] + locatie_outline_boven_x_as][coordinates[0] + locatie_outline_boven_y_as] == 3:
                            check = False
                            break

                        else:
                            
                            # update by incrementing variable to search area
                            locatie_outline_boven_x_as += 1
                            counter_x += 1 
                    except IndexError:
                        locatie_outline_boven_x_as += 1
                        counter_x += 1 

                # check area of y-axis leftside from the top left
                for i in range(range_eengezins):

                    # if a house has been found in the area stop checking
                    try:    
                        if self.wijk1[coordinates[1] + constante_x_links][coordinates[0] + locatie_outline_boven_y_as] == 1 or self.wijk1[coordinates[1] + constante_x_links][coordinates[0] + locatie_outline_boven_y_as] == 2 or self.wijk1[coordinates[1] + constante_x_links][coordinates[0] + locatie_outline_boven_y_as] == 3 :
                            check = False
                            break

                        else:
                            
                            # update by incrementing variable to search area
                            locatie_outline_boven_y_as += 1
                            counter_y += 1 

                    except IndexError:
                        locatie_outline_boven_y_as += 1
                        counter_y += 1 
                    
                # check area of x-axis bottomside from the bottom right
                for i in range(range_eengezins):

                    # if a house has been found in the area stop checking
                    try:    
                        if self.wijk1[coordinates[1] + locatie_outline_onder_x_as][coordinates[0] + locatie_outline_onder_y_as] == 1 or self.wijk1[coordinates[1] + locatie_outline_onder_x_as][coordinates[0] + locatie_outline_onder_y_as] == 2 or self.wijk1[coordinates[1] + locatie_outline_onder_x_as][coordinates[0] + locatie_outline_onder_y_as] == 3:
                            check = False
                            break

                        else:
                            
                            # update by incrementing variable to search area
                            locatie_outline_onder_x_as -= 1
                            counter_x_onder -= 1 

                    except IndexError:
                        locatie_outline_onder_x_as -= 1
                        counter_x_onder -= 1 
                        
                # check area of y-axis rightside from the bottom right
                for i in range(range_eengezins):

                    # if a house has been found in the area stop checking
                    try:
                        if self.wijk1[coordinates[1] + constante_x_rechts][coordinates[0] + locatie_outline_onder_y_as] == 1 or self.wijk1[coordinates[1] + constante_x_rechts][coordinates[0] + locatie_outline_onder_y_as] == 2 or self.wijk1[coordinates[1] + constante_x_rechts][coordinates[0] + locatie_outline_onder_y_as] == 3:
                            check = False
                            break 

                        else:
                            
                            # update by incrementing variable to search area
                            locatie_outline_onder_y_as -= 1
                            counter_y_onder -= 1
                    
                    except IndexError:
                        locatie_outline_onder_y_as -= 1
                        counter_y_onder -= 1

                # reset tracers back to default values and increment by one in order to check next outline around the house
                locatie_outline_boven_x_as = locatie_outline_boven_x_as - counter_x - 1
                locatie_outline_boven_y_as = locatie_outline_boven_y_as - counter_y - 1
                constante_x_links = locatie_outline_boven_x_as

                # reset tracers back to default values and increment by one in order to check next outline around the house
                locatie_outline_onder_x_as = locatie_outline_onder_x_as - counter_x_onder - 1
                locatie_outline_onder_y_as = locatie_outline_onder_y_as - counter_x_onder - 1
                constante_x_rechts = locatie_outline_onder_x_as

                # reset counters back to default values
                counter_x = 0
                counter_y = 0 
                counter_x_onder = 0
                counter_y_onder = 0

                # When no houses found expand outline by 1 meter on every side
                range_eengezins = range_eengezins + 2

                # adjust price of the house by the percentage increase
                self.total_eengezins = self.total_eengezins + self.percentage_eengezins

        return self.total_eengezins
        
    def bungalow_cost(self, coordinaten, bungalow_aantal):

        """ This method calculates the extra price per house depending on the free space that surrounds
         the house. This is done by looking up the coordinates of every house in the coordinates list
         saved when placing the houses. From these coordinates the free space around the houses are checked
         and the total house price is being adjusted. """

        # make default prices of houses
        self.bungalow = 399000
        self.bungalow_aantal = bungalow_aantal

        # calcualte percentage of extra housing worth per extra sqaure meter space
        self.percentage_bungalow = self.bungalow * 0.04

        # make default total prices
        self.total_bungalow = bungalow_aantal * self.bungalow

        # getting the coordinates from placing class
        coordinateslijst = coordinaten

        # check the outline of every bungalow
        for coordinates in coordinaten:

            # create default variables for checking the outline

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

                # check area of x-axis topside from the top left
                for i in range(range_bungalow_x):

                    # if a house has been found in the area stop checking
                    try:
                        if self.wijk1[coordinates[1] + locatie_outline_boven_x_as][coordinates[0] + locatie_outline_boven_y_as] == 1 or self.wijk1[coordinates[1] + locatie_outline_boven_x_as][coordinates[0] + locatie_outline_boven_y_as] == 2 or self.wijk1[coordinates[1] + locatie_outline_boven_x_as][coordinates[0] + locatie_outline_boven_y_as] == 3:
                            check = False
                            break
                        
                        else:
                            
                            # update by incrementing variable to search area
                            locatie_outline_boven_x_as += 1
                            counter_x += 1

                    except IndexError:
                        locatie_outline_boven_x_as += 1
                        counter_x += 1
                
                # check area of y-axis leftside from the top left
                for i in range(range_bungalow_y):

                    # if a house has been found in the area stop checking
                    try:
                        if self.wijk1[coordinates[1] + constante_x_links][coordinates[0] + locatie_outline_boven_y_as] == 1 or self.wijk1[coordinates[1] + constante_x_links][coordinates[0] + locatie_outline_boven_y_as] == 2 or self.wijk1[coordinates[1] + constante_x_links][coordinates[0] + locatie_outline_boven_y_as] == 3:
                            check = False
                            break
                        else:

                            # update by incrementing variable to search area
                            locatie_outline_boven_y_as += 1
                            counter_y += 1 

                    except IndexError:
                        locatie_outline_boven_y_as += 1
                        counter_y += 1 

                # check area of x-axis bottomside from the bottom right
                for i in range(range_bungalow_x):
                    
                    # if a house has been found in the area stop checking
                    try: 
                        if self.wijk1[coordinates[1] + locatie_outline_onder_x_as][coordinates[0] + locatie_outline_onder_y_as] == 1 or self.wijk1[coordinates[1] + locatie_outline_onder_x_as][coordinates[0] + locatie_outline_onder_y_as] == 2 or self.wijk1[coordinates[1] + locatie_outline_onder_x_as][coordinates[0] + locatie_outline_onder_y_as] == 3:
                            check = False
                            break

                        else:

                            # update by incrementing variable to search area
                            locatie_outline_onder_x_as -= 1
                            counter_x_onder -= 1

                    except IndexError:
                        locatie_outline_onder_x_as -= 1
                        counter_x_onder -= 1

                # check area of y-axis rightside from the bottom right
                for i in range(range_bungalow_y):
                    
                    # if a house has been found in the area stop checking
                    try:
                        if self.wijk1[coordinates[1] + constante_x_rechts][coordinates[0] + locatie_outline_onder_y_as] == 1 or self.wijk1[coordinates[1] + constante_x_rechts][coordinates[0] + locatie_outline_onder_y_as] == 2 or self.wijk1[coordinates[1] + constante_x_rechts][coordinates[0] + locatie_outline_onder_y_as] == 3:
                            check = False
                            break 

                        else:

                            # update by incrementing variable to search area
                            locatie_outline_onder_y_as -= 1
                            counter_y_onder -= 1 

                    except IndexError:
                        locatie_outline_onder_y_as -= 1
                        counter_y_onder -= 1 
                            
                
                # reset tracers back to default values and increment by one in order to check next outline around the house
                locatie_outline_boven_x_as = locatie_outline_boven_x_as - counter_x - 1
                locatie_outline_boven_y_as = locatie_outline_boven_y_as - counter_y - 1
                constante_x_links = locatie_outline_boven_x_as

                # reset tracers back to default values and increment by one in order to check next outline around the house
                locatie_outline_onder_x_as = locatie_outline_onder_x_as - counter_x_onder - 1
                locatie_outline_onder_y_as = locatie_outline_onder_y_as - counter_x_onder - 1
                constante_x_rechts = locatie_outline_onder_x_as

                # reset counters back to default values
                counter_x = 0
                counter_y = 0 
                counter_x_onder = 0
                counter_y_onder = 0

                # When no houses found expand outline by 1 meter on every side
                range_bungalow_x += 2
                range_bungalow_y += 2  

                # adjust price of the house by the percentage increase
                self.total_bungalow = self.total_bungalow + self.percentage_bungalow
        
        return self.total_bungalow

    def maison_cost(self, coordinaten, maison_aantal):

        """ This method calculates the extra price per house depending on the free space that surrounds
         the house. This is done by looking up the coordinates of every house in the coordinates list
         saved when placing the houses. From these coordinates the free space around the houses are checked
         and the total house price is being adjusted. """
        
        # make default prices of houses
        self.maison = 610000
        self.maison_aantal = maison_aantal

        # calcualte percentage of extra housing worth per extra sqaure meter space
        self.percentage_maison = self.maison * 0.06

        # make default total prices
        self.total_maison = maison_aantal * self.maison

        # getting the coordinates from placing class
        coordinateslijst = coordinaten

        # check the outline of every bungalow
        for coordinates in coordinaten:

            # create default variables for checking the outline

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

                # check area of x-axis topside from the top left
                for i in range(range_maison_x):

                    # if a house has been found in the area stop checking
                    try:
                        if self.wijk1[coordinates[1] + locatie_outline_boven_x_as][coordinates[0] + locatie_outline_boven_y_as] == 1 or self.wijk1[coordinates[1] + locatie_outline_boven_x_as][coordinates[0] + locatie_outline_boven_y_as] == 2 or self.wijk1[coordinates[1] + locatie_outline_boven_x_as][coordinates[0] + locatie_outline_boven_y_as] == 3:
                            check = False
                            break
                        
                        else:
                            
                            # update by incrementing variable to search area
                            locatie_outline_boven_x_as += 1
                            counter_x += 1 

                    except IndexError:
                        locatie_outline_boven_x_as += 1
                        counter_x += 1

                # check area of y-axis leftside from the top left
                for i in range(range_maison_y):

                    # if a house has been found in the area stop checking
                    try: 
                        if self.wijk1[coordinates[1] + constante_x_links][coordinates[0] + locatie_outline_boven_y_as] == 1 or self.wijk1[coordinates[1] + constante_x_links][coordinates[0] + locatie_outline_boven_y_as] == 2 or self.wijk1[coordinates[1] + constante_x_links][coordinates[0] + locatie_outline_boven_y_as] == 3:
                            check = False
                            break
                        
                        else:

                            # update by incrementing variable to search area
                            locatie_outline_boven_y_as += 1
                            counter_y += 1 

                    except IndexError:
                        locatie_outline_boven_y_as += 1
                        counter_y += 1 

                # check area of x-axis bottomside from the bottom right
                for i in range(range_maison_x):
                    
                    # if a house has been found in the area stop checking
                    try:
                        if self.wijk1[coordinates[1] + locatie_outline_onder_x_as][coordinates[0] + locatie_outline_onder_y_as] == 1 or self.wijk1[coordinates[1] + locatie_outline_onder_x_as][coordinates[0] + locatie_outline_onder_y_as] == 2 or self.wijk1[coordinates[1] + locatie_outline_onder_x_as][coordinates[0] + locatie_outline_onder_y_as] == 3:
                            check = False
                            break

                        else:

                            # update by incrementing variable to search area
                            locatie_outline_onder_x_as -= 1
                            counter_x_onder -= 1 

                    except IndexError:
                        locatie_outline_onder_x_as -= 1
                        counter_x_onder -= 1 

                # check area of y-axis rightside from the bottom right
                for i in range(range_maison_y):
                    
                    # if a house has been found in the area stop checking
                    try:
                        if self.wijk1[coordinates[1] + constante_x_rechts][coordinates[0] + locatie_outline_onder_y_as] == 1 or self.wijk1[coordinates[1] + constante_x_rechts][coordinates[0] + locatie_outline_onder_y_as] == 2 or self.wijk1[coordinates[1] + constante_x_rechts][coordinates[0] + locatie_outline_onder_y_as] == 3:
                            check = False
                            break 

                        else:
                            # update by incrementing variable to search area
                            locatie_outline_onder_y_as -= 1
                            counter_y_onder -= 1 

                    except IndexError:
                        locatie_outline_onder_y_as -= 1
                        counter_y_onder -= 1 


                # reset tracers back to default values and increment by one in order to check next outline around the house
                locatie_outline_boven_x_as = locatie_outline_boven_x_as - counter_x - 1
                locatie_outline_boven_y_as = locatie_outline_boven_y_as - counter_y - 1
                constante_x_links = locatie_outline_boven_x_as

                # reset tracers back to default values and increment by one in order to check next outline around the house
                locatie_outline_onder_x_as = locatie_outline_onder_x_as - counter_x_onder - 1
                locatie_outline_onder_y_as = locatie_outline_onder_y_as - counter_x_onder - 1
                constante_x_rechts = locatie_outline_onder_x_as

                # reset counters back to default values
                counter_x = 0
                counter_y = 0 
                counter_x_onder = 0
                counter_y_onder = 0

                # When no houses found expand outline by 1 meter on every side
                range_maison_x += 2
                range_maison_y += 2  

                # adjust price of the house by the percentage increase
                self.total_maison = self.total_maison + self.percentage_maison

        return self.total_maison


    def total(self, coordinaten_maison, coordinaten_bungalow, coordinaten_eensgezin):
        
        omzet_eengezin = self.eengezins_cost(coordinaten_eensgezin, 12)
        omzet_bungalow = self.bungalow_cost(coordinaten_bungalow, 5)
        omzet_maison = self.maison_cost(coordinaten_maison, 3)
       
        totaal = omzet_eengezin + omzet_bungalow + omzet_maison

        return totaal



class Move(): 

    def __init__(self):
        pass
    
    def move_maison(self, coordinaten_maison, coordinaten_bungalow, coordinaten_eensgezin, wijk1):
        self.coordinaten_maison = coordinaten_maison
        self.coordinaten_bungalow = coordinaten_bungalow
        self.coordinaten_eensgezin = coordinaten_eensgezin

        price = Kosten(wijk1, 12, 5, 3)
        counter = 0 

        for coordinaten in coordinaten_maison:
            
            lijst = []
            opbrengst = []

            lijst.append(coordinaten)
            coordinates = coordinaten_maison
         
            new = price.total(coordinates, coordinaten_bungalow, coordinaten_eensgezin)
            opbrengst.append(new)

            # Linksboven
            linksboven = [(coordinaten[0] - 1), (coordinaten[1] - 1)]
            lijst.append(linksboven)
            coordinaten_maison[counter] = linksboven
            new = price.total(coordinaten_maison, coordinaten_bungalow, coordinaten_eensgezin)
            opbrengst.append(new)

            # Boven
            boven = [(coordinaten[0]), (coordinaten[1] - 1)]
            lijst.append(boven)
            coordinaten_maison[counter] = boven
            new = price.total(coordinaten_maison, coordinaten_bungalow, coordinaten_eensgezin)
            opbrengst.append(new)

            # Rechtsboven
            rechtsboven = [(coordinaten[0] + 1), (coordinaten[1] - 1)]
            lijst.append(rechtsboven)
            coordinaten_maison[counter] = rechtsboven
            new = price.total(coordinaten_maison, coordinaten_bungalow, coordinaten_eensgezin)
            opbrengst.append(new)

            # Rechts
            rechts = [(coordinaten[0] + 1), (coordinaten[1])]
            lijst.append(rechts)
            coordinaten_maison[counter] = rechts
            new = price.total(coordinaten_maison, coordinaten_bungalow, coordinaten_eensgezin)
            opbrengst.append(new)

            # Rechtsonder
            rechtsonder = [(coordinaten[0] + 1), (coordinaten[1] + 1)]
            lijst.append(rechtsonder)
            coordinaten_maison[counter] = rechtsonder
            new = price.total(coordinaten_maison, coordinaten_bungalow, coordinaten_eensgezin)
            opbrengst.append(new)

            # Onder
            onder = [(coordinaten[0]), (coordinaten[1] + 1)]
            lijst.append(onder)
            coordinaten_maison[counter] = onder
            new = price.total(coordinaten_maison, coordinaten_bungalow, coordinaten_eensgezin)
            opbrengst.append(new)

            # Linksonder
            linksonder = [(coordinaten[0] - 1), (coordinaten[1] + 1)]
            lijst.append(linksonder)
            coordinaten_maison[counter] = linksonder
            new = price.total(coordinaten_maison, coordinaten_bungalow, coordinaten_eensgezin)
            opbrengst.append(new)

            # Links
            links = [(coordinaten[0] - 1), (coordinaten[1])]
            lijst.append(links)
            coordinaten_maison[counter] = links
            new = price.total(coordinaten_maison, coordinaten_bungalow, coordinaten_eensgezin)
            opbrengst.append(new)

            # Getting the best option
            hoogste = max(opbrengst)
            index = opbrengst.index(hoogste)
            best_coor = lijst[index]
            coordinaten_maison[counter] = best_coor

            counter += 1

            
    def move_eensgezin(self, coordinaten_maison, coordinaten_bungalow, coordinaten_eensgezin, wijk1):
        self.coordinaten_maison = coordinaten_maison
        self.coordinaten_bungalow = coordinaten_bungalow
        self.coordinaten_eensgezin = coordinaten_eensgezin

        price = Kosten(wijk1, 12, 5, 3)
        counter = 0 

        for coordinaten in coordinaten_eensgezin:
            
            lijst = []
            opbrengst = []

            lijst.append(coordinaten)
            coordinates = coordinaten_eensgezin
         
            new = price.total(coordinaten_maison, coordinaten_bungalow, coordinates)
            opbrengst.append(new)

            # Linksboven
            linksboven = [(coordinaten[0] - 1), (coordinaten[1] - 1)]
            lijst.append(linksboven)
            coordinaten_eensgezin[counter] = linksboven
            new = price.total(coordinaten_maison, coordinaten_bungalow, coordinaten_eensgezin)
            opbrengst.append(new)

            # Boven
            boven = [(coordinaten[0]), (coordinaten[1] - 1)]
            lijst.append(boven)
            coordinaten_eensgezin[counter] = boven
            new = price.total(coordinaten_maison, coordinaten_bungalow, coordinaten_eensgezin)
            opbrengst.append(new)

            # Rechtsboven
            rechtsboven = [(coordinaten[0] + 1), (coordinaten[1] - 1)]
            lijst.append(rechtsboven)
            coordinaten_eensgezin[counter] = rechtsboven
            new = price.total(coordinaten_maison, coordinaten_bungalow, coordinaten_eensgezin)
            opbrengst.append(new)

            # Rechts
            rechts = [(coordinaten[0] + 1), (coordinaten[1])]
            lijst.append(rechts)
            coordinaten_eensgezin[counter] = rechts
            new = price.total(coordinaten_maison, coordinaten_bungalow, coordinaten_eensgezin)
            opbrengst.append(new)

            # Rechtsonder
            rechtsonder = [(coordinaten[0] + 1), (coordinaten[1] + 1)]
            lijst.append(rechtsonder)
            coordinaten_eensgezin[counter] = rechtsonder
            new = price.total(coordinaten_maison, coordinaten_bungalow, coordinaten_eensgezin)
            opbrengst.append(new)

            # Onder
            onder = [(coordinaten[0]), (coordinaten[1] + 1)]
            lijst.append(onder)
            coordinaten_eensgezin[counter] = onder
            new = price.total(coordinaten_maison, coordinaten_bungalow, coordinaten_eensgezin)
            opbrengst.append(new)

            # Linksonder
            linksonder = [(coordinaten[0] - 1), (coordinaten[1] + 1)]
            lijst.append(linksonder)
            coordinaten_eensgezin[counter] = linksonder
            new = price.total(coordinaten_maison, coordinaten_bungalow, coordinaten_eensgezin)
            opbrengst.append(new)

            # Links
            links = [(coordinaten[0] - 1), (coordinaten[1])]
            lijst.append(links)
            coordinaten_eensgezin[counter] = links
            new = price.total(coordinaten_maison, coordinaten_bungalow, coordinaten_eensgezin)
            opbrengst.append(new)

            # Getting the best option
            hoogste = max(opbrengst)
            index = opbrengst.index(hoogste)
            best_coor = lijst[index]
            coordinaten_eensgezin[counter] = best_coor

            counter += 1 
            

    def move_bungalow(self, coordinaten_maison, coordinaten_bungalow, coordinaten_eensgezin, wijk1):
        self.coordinaten_maison = coordinaten_maison
        self.coordinaten_bungalow = coordinaten_bungalow
        self.coordinaten_eensgezin = coordinaten_eensgezin

        price = Kosten(wijk1, 12, 5, 3)
        counter = 0 

        for coordinaten in coordinaten_bungalow:
            
            lijst = []
            opbrengst = []

            lijst.append(coordinaten)
            coordinates = coordinaten_bungalow
         
            new = price.total(coordinaten_bungalow, coordinates, coordinaten_eensgezin)
            opbrengst.append(new)

            # Linksboven
            linksboven = [(coordinaten[0] - 1), (coordinaten[1] - 1)]
            lijst.append(linksboven)
            coordinaten_bungalow[counter] = linksboven
            new = price.total(coordinaten_maison, coordinaten_bungalow, coordinaten_eensgezin)
            opbrengst.append(new)

            # Boven
            boven = [(coordinaten[0]), (coordinaten[1] - 1)]
            lijst.append(boven)
            coordinaten_bungalow[counter] = boven
            new = price.total(coordinaten_maison, coordinaten_bungalow, coordinaten_eensgezin)
            opbrengst.append(new)

            # Rechtsboven
            rechtsboven = [(coordinaten[0] + 1), (coordinaten[1] - 1)]
            lijst.append(rechtsboven)
            coordinaten_bungalow[counter] = rechtsboven
            new = price.total(coordinaten_maison, coordinaten_bungalow, coordinaten_eensgezin)
            opbrengst.append(new)

            # Rechts
            rechts = [(coordinaten[0] + 1), (coordinaten[1])]
            lijst.append(rechts)
            coordinaten_bungalow[counter] = rechts
            new = price.total(coordinaten_maison, coordinaten_bungalow, coordinaten_eensgezin)
            opbrengst.append(new)

            # Rechtsonder
            rechtsonder = [(coordinaten[0] + 1), (coordinaten[1] + 1)]
            lijst.append(rechtsonder)
            coordinaten_bungalow[counter] = rechtsonder
            new = price.total(coordinaten_maison, coordinaten_bungalow, coordinaten_eensgezin)
            opbrengst.append(new)

            # Onder
            onder = [(coordinaten[0]), (coordinaten[1] + 1)]
            lijst.append(onder)
            coordinaten_bungalow[counter] = onder
            new = price.total(coordinaten_maison, coordinaten_bungalow, coordinaten_eensgezin)
            opbrengst.append(new)

            # Linksonder
            linksonder = [(coordinaten[0] - 1), (coordinaten[1] + 1)]
            lijst.append(linksonder)
            coordinaten_bungalow[counter] = linksonder
            new = price.total(coordinaten_maison, coordinaten_bungalow, coordinaten_eensgezin)
            opbrengst.append(new)

            # Links
            links = [(coordinaten[0] - 1), (coordinaten[1])]
            lijst.append(links)
            coordinaten_bungalow[counter] = links
            new = price.total(coordinaten_maison, coordinaten_bungalow, coordinaten_eensgezin)
            opbrengst.append(new)

            # Getting the best option
            hoogste = max(opbrengst)
            index = opbrengst.index(hoogste)
            best_coor = lijst[index]
            coordinaten_bungalow[counter] = best_coor

            counter += 1 


def main():
    
    total_prices = []
    for i in range(0,2):
        # create a 160 x 180 gridmap
        x, y = (160, 180) 
        wijk1 = [[0 for i in range(x)] for j in range(y)] 

        # adding houses
        price = Kosten(wijk1, 12, 5, 3)
        place = Placing(wijk1, 12, 5, 3)
        move = Move()
        
        place.water()
        coordinaten_eensgezin = place.eensgezinswoningen(12, wijk1)
        coordinaten_maison = place.maison(3, wijk1, coordinaten_eensgezin)
        coordinaten_bungalow = place.bungalow(5, wijk1, coordinaten_eensgezin, coordinaten_maison)

        print("coordinaten before")
        print(coordinaten_eensgezin)
        print(coordinaten_bungalow)
        print(coordinaten_maison)

        totaal = price.total(coordinaten_maison, coordinaten_bungalow, coordinaten_eensgezin)
        print("before")
        print(totaal)

        for i in range(0,3):
            move.move_maison(coordinaten_maison, coordinaten_bungalow, coordinaten_eensgezin, wijk1)
            move.move_eensgezin(coordinaten_maison, coordinaten_bungalow, coordinaten_eensgezin, wijk1)
            move.move_bungalow(coordinaten_maison, coordinaten_bungalow, coordinaten_eensgezin, wijk1)
        
        print("coordinaten after")
        print(coordinaten_eensgezin)
        print(coordinaten_bungalow)
        print(coordinaten_maison)
        totaal = price.total(coordinaten_maison, coordinaten_bungalow, coordinaten_eensgezin)
        print("after")
        print(totaal)
        total_prices.append(totaal)

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
    
    mean = statistics.mean(total_prices)
    print(mean)
    print(max(total_prices))


    #     # showing picture
    # H = np.array(wijk1)
    # plt.imshow(H)
    # plt.pcolor(H, cmap = "Greens_r")

    # plt.show()
    # plt.savefig("blueprint.png")


        # # saving in csv file
        # with open("wijk1.csv","w+") as my_csv:
        #     csvWriter = csv.writer(my_csv,delimiter=',')
        #     csvWriter.writerows(wijk1)

if __name__ == '__main__':
    main()