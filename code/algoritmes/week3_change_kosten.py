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
    def __init__(self, wijk, aantal_eensgezins, aantal_maison, aantal_bungalow):
        
        self.wijk = wijk
        self.aantal_eensgezins = aantal_eensgezins
        self.aantal_maison = aantal_maison
        self.aantal_bungalow = aantal_bungalow

    def water(self, top_left, bottom_right):

        """ This method adds areas of water to the created gridmap. 
         The areas of water are given in top-left to bottom-right coordinates of 
         the area that is supposed to be water. These coordinates are looped over and
         the values of these coordinates are changed to the water value. """

        # for every asked individual area of water create this area from the given coordinates
        for water_top_left, water_bottom_right in zip(top_left, bottom_right):
            
            # create the range of the water
            water_range_x = water_bottom_right[0] - water_top_left[0]
            water_range_y = water_bottom_right[1] - water_top_left[1]
            
            # create starting coordinate in the top left
            x_coor = water_top_left[0]
            y_coor = water_top_left[1]
            
            # move in the range of the x-axis
            for i in range(water_range_x):
                
                # change the coordinate value on the gridmap to the water value
                self.wijk[y_coor][x_coor] = 4

                # move in the range of the y-axis
                for j in range(water_range_y):
                    
                    # change the coordinate value on the gridmap to the water value
                    self.wijk[y_coor][x_coor] = 4

                    # move one coordinate on the y-axis
                    y_coor += 1

                # move one coordinate on the x-axis
                x_coor += 1 
                
                # move to the beginning y-axis value
                y_coor = water_top_left[1]                         

    # adding eensgezinswoningen 

    def eensgezinswoningen(self, aantal_eensgezins):

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

            if counter > 0:
                
                for i in range(0,20):
                    # set default value of empty gridmap area to False
                    vrij = False

                    # while no empty space has been found keep searching
                    while vrij == False:
                        
                        # set default to check if random coordinate is situated on water
                        self.water = True
                
                        # create random coordinate till a place is found where there is no water
                        while self.water == True:
                        
                            # create a random coordinate
                            x = random.randrange(2, 150)
                            y_oud = random.randrange(2,170)
                            
                            # if the corners of the house are not situated on water continue
                            if self.wijk[y_oud][x] != 4 and self.wijk[y_oud][x + 8] != 4 and self.wijk[y_oud + 8][x] != 4 and self.wijk[y_oud + 8][x + 8] != 4:
                                self.water = False

                        # set default value for nested break to False
                        nested_break = False

                        # check from the randomly chosen coordinate as the top left corner if there is empty space to place a house horizontally
                        for i in range(0,12):

                            # if the coordinate is no empty area to place a house break out of the scanning loop
                            if self.wijk[y_oud - 2][x - 2 + i] == 1 or self.wijk[y_oud - 2][x - 2 + i] == 2 or self.wijk[y_oud - 2][x - 2 + i] == 3:

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
                                if self.wijk[y_oud - 2 + j][x - 2 + i] == 1 or self.wijk[y_oud - 2 + j][x - 2 + i] == 2 or self.wijk[y_oud - 2 + j][x - 2 + i] == 3:
                            
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
                    eensgezins_coordinatenlijst[counter] = new_coor

                    price = Kosten(self.wijk, 12, 5, 3)
                    new = price.total(coordinaten_maison, coordinaten_bungalow, coordinaten_eensgezin)

                    if new > oud:
                        oud = new
                        oud_coor = new_coor
                
                for i in range(0,len(eensgezins_coordinatenlijst)):
                    if eensgezins_coordinatenlijst[i] == [0,0]:
                        eensgezins_coordinatenlijst[i] = oud_coor

                eensgezins_coordinatenlijst[counter] = oud_coor

            else: 
                vrij = False

                # while no empty space has been found keep searching
                while vrij == False:
                    
                    # set default to check if random coordinate is situated on water
                    self.water = True
                
                    # create random coordinate till a place is found where there is no water
                    while self.water == True:
                
                        # create a random coordinate
                        x = random.randrange(2, 150)
                        y_oud = random.randrange(2,170)
                        
                        # if the corners of the house are not situated on water continue
                        if self.wijk[y_oud][x] != 4 and self.wijk[y_oud][x + 8] != 4 and self.wijk[y_oud + 8][x] != 4 and self.wijk[y_oud + 8][x + 8] != 4:
                            self.water = False

                    # set default value for nested break to False
                    nested_break = False

                    # check from the randomly chosen coordinate as the top left corner if there is empty space to place a house horizontally
                    for i in range(0,12):

                        # if the coordinate is no empty area to place a house break out of the scanning loop
                        if self.wijk[y_oud - 2][x - 2 + i] == 1 or self.wijk[y_oud - 2][x - 2 + i] == 2 or self.wijk[y_oud - 2][x - 2 + i] == 3:

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
                            if self.wijk[y_oud - 2 + j][x - 2 + i] == 1 or self.wijk[y_oud - 2 + j][x - 2 + i] == 2 or self.wijk[y_oud - 2 + j][x - 2 + i] == 3:
                        
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
                
                for i in range(0,12):
                
                    # change the outer 2 meters of the area for the house to "vrijstaand"
                    if i == 0 or i == 1 or i == 11 or i == 10:
                        self.wijk[coor[1] - 2][coor[0] - 2 + i] = 5

                    # change the area inside the "vrijstaand" area to "eengezins" value
                    else:
                        self.wijk[coor[1]- 2][coor[0] - 2 + i] = 1

                    for j in range(0,12):

                        # change the outer 2 meters of the area for the house to "vrijstaand"
                        if j == 0 or j == 1 or j == 11 or j == 10 or i == 0 or i == 1 or i == 11 or i == 10: 
                            self.wijk[coor[1] - 2 + j][coor[0] - 2 + i] = 5                        

                        # change the area inside the "vrijstaand" area to "eengezins" value
                        else: 
                            self.wijk[coor[1] - 2 + j][coor[0] - 2 + i] = 1
                     
        totaal = price.total(coordinaten_maison, coordinaten_bungalow, coordinaten_eensgezin)

        return eensgezins_coordinatenlijst

    def maison(self, aantal_maison, coordinaten_eensgezin):

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
              
            # while the amount of houses needed to be placed has not been reached yet search for empty area
            for i in range(0,20):
                vrij = False
                while vrij == False:
                    
                    # set default to check if random coordinate is situated on water
                    self.water = True
                
                    # create random coordinate till a place is found where there is no water
                    while self.water == True:
                
                        # create a random coordinate
                        x = random.randrange(6, 142)
                        y_oud = random.randrange(6,164)

                        # if the corners of the house are not situated on water continue
                        if self.wijk[y_oud][x] != 4 and self.wijk[y_oud][x + 12] != 4 and self.wijk[y_oud + 10][x] != 4 and self.wijk[y_oud + 10][x + 12] != 4:
                            self.water = False

                    nested_break = False

                    # check from the randomly chosen coordinate as the top left corner if there is empty space to place a house horizontally
                    for i in range(0,24):
                        # print(y_oud - 6, x - 6)
                        
                        # if the coordinate is no empty area to place a house break out of the scanning loop
                        if self.wijk[y_oud - 6][x - 6 + i] == 1 or self.wijk[y_oud - 6][x - 6 + i] == 2 or self.wijk[y_oud - 6][x - 6 + i] == 3:
                            
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
                            if self.wijk[y_oud - 6 + j][x - 6 + i] == 1 or self.wijk[y_oud - 6 + j][x - 6 + i] == 2 or self.wijk[y_oud - 6 + j][x - 6 + i] == 3:
                                
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
                
                price = Kosten(self.wijk, 12, 5, 3)
                new = price.total(coordinaten_maison, coordinaten_bungalow, coordinaten_eensgezin)
                
                if new > oud:
                    oud = new
                    oud_coor = new_coor
                
            for i in range(0,len(maison_coordinatenlijst)):
                if maison_coordinatenlijst[i] == [0,0]:
                    maison_coordinatenlijst[i] = oud_coor
            maison_coordinatenlijst[counter_maison] = oud_coor
       
            counter_maison += 1
   
            for coor in maison_coordinatenlijst:
                for i in range(0,24):

                    # change the outer 2 meters of the area for the house to "vrijstaand"
                    if i == 0 or i == 1 or i == 2 or i == 3 or i == 4 or i == 5 or i == 18 or i == 19 or i == 20 or i == 21 or i == 22 or i == 23:
                        self.wijk[coor[1] - 6][coor[0] - 6 + i] = 5

                    # change the area inside the "vrijstaand" area to "eengezins" value
                    else:
                        self.wijk[coor[1] - 6][coor[0] - 6 + i] = 3

                    for j in range(0,22):

                        # change the outer 2 meters of the area for the house to "vrijstaand"
                        if j == 0 or j == 1 or j == 2 or j == 3 or j == 4 or j == 5 or j == 16 or j == 17 or j == 18 or j == 19 or j == 20 or j == 21 or i == 0 or i == 1 or i == 2 or i == 3 or i == 4 or i == 5 or i == 18 or i == 19 or i == 20 or i == 21 or i == 22 or i == 23:
                            self.wijk[coor[1] - 6 + j][coor[0] - 6 + i] = 5                        

                        # change the area inside the "vrijstaand" area to "eengezins" value
                        else: 
                            self.wijk[coor[1] - 6 + j][coor[0] - 6 + i] = 3
                
         
                
        totaal = price.total(coordinaten_maison, coordinaten_bungalow, coordinaten_eensgezin)
        
        return maison_coordinatenlijst

    def bungalow(self, aantal_bungalow, coordinaten_eensgezin, coordinaten_maison):

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
            
            for i in range(0,20):
                vrij = False

                # set default value of empty gridmap area to False
                while vrij == False:
                    
                    # set default to check if random coordinate is situated on water
                    self.water = True
                
                    # create random coordinate till a place is found where there is no water
                    while self.water is True:
                
                        # create a random coordinate
                        x = random.randrange(3, 146)
                        y_oud = random.randrange(3,170)

                        # if the corners of the house are not situated on water continue
                        if self.wijk[y_oud][x] != 4 and self.wijk[y_oud][x + 11] != 4 and self.wijk[y_oud + 7][x] != 4 and self.wijk[y_oud + 7][x +11] != 4:
                            self.water = False

                    nested_break = False

                    # check from the randomly chosen coordinate as the top left corner if there is empty space to place a house horizontally
                    for i in range(0,17):
                        
                        # if the coordinate is no empty area to place a house break out of the scanning loop
                        if self.wijk[y_oud - 3][x - 3 + i] == 1 or self.wijk[y_oud - 3][x - 3 + i] == 2 or self.wijk[y_oud - 3][x - 3 + i] == 3:
                            vrij = False
                            break

                        # change the nested break value to True
                        else:
                            vrij = True

                        # check from the randomly chosen coordinate as the top left corner if there is empty space to place a house vertically    
                        for j in range(0,13):
                            
                            # if the coordinate is no empty area to place a house break out of the scanning loop
                            if self.wijk[y_oud - 3 + j][x - 3 + i] == 1 or self.wijk[y_oud - 3 + j][x - 3 + i] == 2 or self.wijk[y_oud - 3 + j][x - 3 + i] == 3:
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
                
                price = Kosten(self.wijk, 12, 5, 3)
                new = price.total(coordinaten_maison, coordinaten_bungalow, coordinaten_eensgezin)
                
                if new > oud:
                    oud = new
                    oud_coor = new_coor
                
            for i in range(0,len(bungalow_coordinatenlijst)):
                if bungalow_coordinatenlijst[i] == [0,0]:
                    bungalow_coordinatenlijst[i] = oud_coor

            bungalow_coordinatenlijst[counter_bungalow] = oud_coor
            # if an empty area has been found save the randomized coordinate in the houses list
            counter_bungalow += 1            
                    
            for coor in bungalow_coordinatenlijst:

                for i in range(0,17):
                    
                    # change the outer 2 meters of the area for the house to "vrijstaand"
                    if i == 0 or i == 1 or i == 2 or i == 14 or i == 15 or i == 16 :
                        self.wijk[coor[1] - 3][coor[0] - 3 + i] = 5

                    # change the area inside the "vrijstaand" area to "eengezins" value
                    else:
                        self.wijk[coor[1] - 3][coor[0] - 3 + i] = 2

                    for j in range(0,13):

                        # change the outer 2 meters of the area for the house to "vrijstaand"
                        if j == 0 or j == 1 or j == 2 or j == 10 or j == 11 or j == 12 or i == 0 or i == 1 or i == 2 or i == 14 or i == 15 or i == 16:
                            self.wijk[coor[1] - 3 + j][coor[0] - 3 + i] = 5                        

                        # change the area inside the "vrijstaand" area to "eengezins" value
                        else: 
                            self.wijk[coor[1] - 3 + j][coor[0] - 3 + i] = 2

        totaal = price.total(coordinaten_maison, coordinaten_bungalow, coordinaten_eensgezin)

        return bungalow_coordinatenlijst

class Kosten():

    """ This class consists out of methods which calculate the price of the houses placed on the gridmap.
    The total price is firstly set at a default value. After this the methods can be called upon which
    adds the extra price per house when going over the map. """


    # save the amount of houses being placed when running the Placing class 
    def __init__(self, wijk, eengezins_aantal, bungalow_aantal, maison_aantal):
        
        self.wijk = wijk
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

            # range_eengezins = 14
            # locatie_outline_boven_x_as =  -3
            # locatie_outline_boven_y_as = -3
            # locatie_outline_onder_x_as = 11
            # locatie_outline_onder_y_as = 11
            # constante_x_links = -3
            # constante_x_rechts = 11

            # check = True
            # counter_x = 0
            # counter_y = 0 
            # counter_x_onder = 0
            # counter_y_onder = 0
            eensgezinswoning = 1 
            bungalow = 2 
            maison = 3      
      
            afstand_tot_huis = 3 
            x_coordinaat = coordinates[0]
            y_coordinaat = coordinates[1]
            som = 0 


            while check == True:
                x = x_coordinaat - afstand_tot_huis
                x_ver = x_coordinaat + 8 + afstand_tot_huis
                y = y_coordinaat - afstand_tot_huis
                y_ver = y_coordinaat + 8 + afstand_tot_huis

                try:
                    if eensgezinswoning in self.wijk[x:x_ver, y:y_ver] or bungalow in self.wijk[x:x_ver, y:y_ver] or maison in self.wijk[x:x_ver, y:y_ver]:
                        check = False
                    else:
                        self.total_eengezins = self.total_eengezins + self.percentage_eengezins
                        afstand_tot_huis += 1
                
                except IndexError:
                    if eensgezinswoning in self.wijk[x:x_ver, y:y_ver] or bungalow in self.wijk[x:x_ver, y:y_ver] or maison in self.wijk[x:x_ver, y:y_ver]:
                        check = False
                    else:
                        self.total_eengezins = self.total_eengezins + self.percentage_eengezins
                        afstand_tot_huis += 1

                


            # while som < 241 or som > 600:
            #     x = x_coordinaat - afstand_tot_huis
            #     x_ver = x_coordinaat + 8 + afstand_tot_huis
            #     y = y_coordinaat - afstand_tot_huis
            #     y_ver = y_coordinaat + 8 + afstand_tot_huis
                
            #     try: 
            #         som = np.sum(self.wijk[x:x_ver, y:y_ver])
            #         if som < 241:
            #             self.total_eengezins = self.total_eengezins + self.percentage_eengezins
            #             afstand_tot_huis += 1 
            #     except IndexError:
            #         som = np.sum(self.wijk[(x_coordinaat - afstand_tot_huis):(x_coordinaat + 8 + afstand_tot_huis), (y_coordinaat - afstand_tot_huis):(y_coordinaat + 8 + afstand_tot_huis)])
            #         if som < 241:
            #             self.total_eengezins = self.total_eengezins + self.percentage_eengezins
            #             afstand_tot_huis += 1
            #         break
                    
            
                







            # while check == True:

            #     # check area of x-axis topside from the top left
            #     for i in range(range_eengezins):

            #         # if a house has been found in the area stop checking
            #         try:    
            #             if self.wijk[coordinates[1] + locatie_outline_boven_x_as][coordinates[0] + locatie_outline_boven_y_as] == 1 or self.wijk[coordinates[1] + locatie_outline_boven_x_as][coordinates[0] + locatie_outline_boven_y_as] == 2 or self.wijk[coordinates[1] + locatie_outline_boven_x_as][coordinates[0] + locatie_outline_boven_y_as] == 3:
            #                 check = False
            #                 break

            #             else:
                            
            #                 # update by incrementing variable to search area
            #                 locatie_outline_boven_x_as += 1
            #                 counter_x += 1 
            #         except IndexError:
            #             locatie_outline_boven_x_as += 1
            #             counter_x += 1 

            #     # check area of y-axis leftside from the top left
            #     for i in range(range_eengezins):

            #         # if a house has been found in the area stop checking
            #         try:    
            #             if self.wijk[coordinates[1] + constante_x_links][coordinates[0] + locatie_outline_boven_y_as] == 1 or self.wijk[coordinates[1] + constante_x_links][coordinates[0] + locatie_outline_boven_y_as] == 2 or self.wijk[coordinates[1] + constante_x_links][coordinates[0] + locatie_outline_boven_y_as] == 3 :
            #                 check = False
            #                 break

            #             else:
                            
            #                 # update by incrementing variable to search area
            #                 locatie_outline_boven_y_as += 1
            #                 counter_y += 1 

            #         except IndexError:
            #             locatie_outline_boven_y_as += 1
            #             counter_y += 1 
                    
            #     # check area of x-axis bottomside from the bottom right
            #     for i in range(range_eengezins):

            #         # if a house has been found in the area stop checking
            #         try:    
            #             if self.wijk[coordinates[1] + locatie_outline_onder_x_as][coordinates[0] + locatie_outline_onder_y_as] == 1 or self.wijk[coordinates[1] + locatie_outline_onder_x_as][coordinates[0] + locatie_outline_onder_y_as] == 2 or self.wijk[coordinates[1] + locatie_outline_onder_x_as][coordinates[0] + locatie_outline_onder_y_as] == 3:
            #                 check = False
            #                 break

            #             else:
                            
            #                 # update by incrementing variable to search area
            #                 locatie_outline_onder_x_as -= 1
            #                 counter_x_onder -= 1 

            #         except IndexError:
            #             locatie_outline_onder_x_as -= 1
            #             counter_x_onder -= 1 
                        
            #     # check area of y-axis rightside from the bottom right
            #     for i in range(range_eengezins):

            #         # if a house has been found in the area stop checking
            #         try:
            #             if self.wijk[coordinates[1] + constante_x_rechts][coordinates[0] + locatie_outline_onder_y_as] == 1 or self.wijk[coordinates[1] + constante_x_rechts][coordinates[0] + locatie_outline_onder_y_as] == 2 or self.wijk[coordinates[1] + constante_x_rechts][coordinates[0] + locatie_outline_onder_y_as] == 3:
            #                 check = False
            #                 break 

            #             else:
                            
            #                 # update by incrementing variable to search area
            #                 locatie_outline_onder_y_as -= 1
            #                 counter_y_onder -= 1
                    
            #         except IndexError:
            #             locatie_outline_onder_y_as -= 1
            #             counter_y_onder -= 1

            #     # reset tracers back to default values and increment by one in order to check next outline around the house
            #     locatie_outline_boven_x_as = locatie_outline_boven_x_as - counter_x - 1
            #     locatie_outline_boven_y_as = locatie_outline_boven_y_as - counter_y - 1
            #     constante_x_links = locatie_outline_boven_x_as

            #     # reset tracers back to default values and increment by one in order to check next outline around the house
            #     locatie_outline_onder_x_as = locatie_outline_onder_x_as - counter_x_onder - 1
            #     locatie_outline_onder_y_as = locatie_outline_onder_y_as - counter_x_onder - 1
            #     constante_x_rechts = locatie_outline_onder_x_as

            #     # reset counters back to default values
            #     counter_x = 0
            #     counter_y = 0 
            #     counter_x_onder = 0
            #     counter_y_onder = 0

            #     # When no houses found expand outline by 1 meter on every side
            #     range_eengezins = range_eengezins + 2

            #     # adjust price of the house by the percentage increase
            #     if check == True:
            #         self.total_eengezins = self.total_eengezins + self.percentage_eengezins

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

            # range_bungalow_x = 19
            # range_bungalow_y = 15
            # locatie_outline_boven_x_as =  -4
            # locatie_outline_boven_y_as = -4
            # locatie_outline_onder_x_as = 15
            # locatie_outline_onder_y_as = 11
            # constante_x_links = -4
            # constante_x_rechts = 15

            # check = True
            # counter_x = 0
            # counter_y = 0 
            # counter_x_onder = 0
            # counter_y_onder = 0


            eensgezinswoning = 1 
            bungalow = 2 
            maison = 3 
            
            afstand_tot_huis = 4
            x_coordinaat = coordinates[0]
            y_coordinaat = coordinates[1]
            som = 0 
            
            while check == True:
                x = x_coordinaat - afstand_tot_huis
                x_ver = x_coordinaat + 11 + afstand_tot_huis
                y = y_coordinaat - afstand_tot_huis
                y_ver = y_coordinaat + 7 + afstand_tot_huis

                try: 
                    if eensgezinswoning in self.wijk[x:x_ver, y:y_ver] or bungalow in self.wijk[x:x_ver, y:y_ver] or maison in self.wijk[x:x_ver, y:y_ver]:
                        check = False
                    else:
                        self.total_eengezins = self.total_eengezins + self.percentage_eengezins
                        afstand_tot_huis += 1 
               
                except IndexError:
                    if eensgezinswoning in self.wijk[x:x_ver, y:y_ver] or bungalow in self.wijk[x:x_ver, y:y_ver] or maison in self.wijk[x:x_ver, y:y_ver]:
                        check = False
                    else:
                        self.total_eengezins = self.total_eengezins + self.percentage_eengezins
                        afstand_tot_huis += 1 





            
            
            # while som < 466 or som > 1000:
            #     x = x_coordinaat - afstand_tot_huis
            #     x_ver = x_coordinaat + 11 + afstand_tot_huis
            #     y = y_coordinaat - afstand_tot_huis
            #     y_ver = y_coordinaat + 7 + afstand_tot_huis
                
            #     try: 
            #         som = np.sum(self.wijk[x:x_ver, y:y_ver])
            #         if som < 466:
            #             self.total_eengezins = self.total_eengezins + self.percentage_eengezins
            #             afstand_tot_huis += 1 
            #     except IndexError:
            #         som = np.sum(self.wijk[(x_coordinaat - afstand_tot_huis):(x_coordinaat + 8 + afstand_tot_huis), (y_coordinaat - afstand_tot_huis):(y_coordinaat + 8 + afstand_tot_huis)])
            #         if som < 466:
            #             self.total_eengezins = self.total_eengezins + self.percentage_eengezins
            #             afstand_tot_huis += 1
            #         break
            
            
            
            # while check == True:

            #     # check area of x-axis topside from the top left
            #     for i in range(range_bungalow_x):

            #         # if a house has been found in the area stop checking
            #         try:
            #             if self.wijk[coordinates[1] + locatie_outline_boven_x_as][coordinates[0] + locatie_outline_boven_y_as] == 1 or self.wijk[coordinates[1] + locatie_outline_boven_x_as][coordinates[0] + locatie_outline_boven_y_as] == 2 or self.wijk[coordinates[1] + locatie_outline_boven_x_as][coordinates[0] + locatie_outline_boven_y_as] == 3:
            #                 check = False
            #                 break
                        
            #             else:
                            
            #                 # update by incrementing variable to search area
            #                 locatie_outline_boven_x_as += 1
            #                 counter_x += 1

            #         except IndexError:
            #             locatie_outline_boven_x_as += 1
            #             counter_x += 1
                
            #     # check area of y-axis leftside from the top left
            #     for i in range(range_bungalow_y):

            #         # if a house has been found in the area stop checking
            #         try:
            #             if self.wijk[coordinates[1] + constante_x_links][coordinates[0] + locatie_outline_boven_y_as] == 1 or self.wijk[coordinates[1] + constante_x_links][coordinates[0] + locatie_outline_boven_y_as] == 2 or self.wijk[coordinates[1] + constante_x_links][coordinates[0] + locatie_outline_boven_y_as] == 3:
            #                 check = False
            #                 break
            #             else:

            #                 # update by incrementing variable to search area
            #                 locatie_outline_boven_y_as += 1
            #                 counter_y += 1 

            #         except IndexError:
            #             locatie_outline_boven_y_as += 1
            #             counter_y += 1 

            #     # check area of x-axis bottomside from the bottom right
            #     for i in range(range_bungalow_x):
                    
            #         # if a house has been found in the area stop checking
            #         try: 
            #             if self.wijk[coordinates[1] + locatie_outline_onder_x_as][coordinates[0] + locatie_outline_onder_y_as] == 1 or self.wijk[coordinates[1] + locatie_outline_onder_x_as][coordinates[0] + locatie_outline_onder_y_as] == 2 or self.wijk[coordinates[1] + locatie_outline_onder_x_as][coordinates[0] + locatie_outline_onder_y_as] == 3:
            #                 check = False
            #                 break

            #             else:

            #                 # update by incrementing variable to search area
            #                 locatie_outline_onder_x_as -= 1
            #                 counter_x_onder -= 1

            #         except IndexError:
            #             locatie_outline_onder_x_as -= 1
            #             counter_x_onder -= 1

            #     # check area of y-axis rightside from the bottom right
            #     for i in range(range_bungalow_y):
                    
            #         # if a house has been found in the area stop checking
            #         try:
            #             if self.wijk[coordinates[1] + constante_x_rechts][coordinates[0] + locatie_outline_onder_y_as] == 1 or self.wijk[coordinates[1] + constante_x_rechts][coordinates[0] + locatie_outline_onder_y_as] == 2 or self.wijk[coordinates[1] + constante_x_rechts][coordinates[0] + locatie_outline_onder_y_as] == 3:
            #                 check = False
            #                 break 

            #             else:

            #                 # update by incrementing variable to search area
            #                 locatie_outline_onder_y_as -= 1
            #                 counter_y_onder -= 1 

            #         except IndexError:
            #             locatie_outline_onder_y_as -= 1
            #             counter_y_onder -= 1 
                            
                
            #     # reset tracers back to default values and increment by one in order to check next outline around the house
            #     locatie_outline_boven_x_as = locatie_outline_boven_x_as - counter_x - 1
            #     locatie_outline_boven_y_as = locatie_outline_boven_y_as - counter_y - 1
            #     constante_x_links = locatie_outline_boven_x_as

            #     # reset tracers back to default values and increment by one in order to check next outline around the house
            #     locatie_outline_onder_x_as = locatie_outline_onder_x_as - counter_x_onder - 1
            #     locatie_outline_onder_y_as = locatie_outline_onder_y_as - counter_x_onder - 1
            #     constante_x_rechts = locatie_outline_onder_x_as

            #     # reset counters back to default values
            #     counter_x = 0
            #     counter_y = 0 
            #     counter_x_onder = 0
            #     counter_y_onder = 0

            #     # When no houses found expand outline by 1 meter on every side
            #     range_bungalow_x += 2
            #     range_bungalow_y += 2  

            #     # adjust price of the house by the percentage increase
            #     if check == True:
            #         self.total_bungalow = self.total_bungalow + self.percentage_bungalow
        
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

            # range_maison_x = 26
            # range_maison_y = 24
            # locatie_outline_boven_x_as = -7
            # locatie_outline_boven_y_as = -7
            # locatie_outline_onder_x_as = 19
            # locatie_outline_onder_y_as = 17
            # constante_x_links = -7
            # constante_x_rechts = 19

            # check = True
            # counter_x = 0
            # counter_y = 0 
            # counter_x_onder = 0
            # counter_y_onder = 0

            afstand_tot_huis = 7
            x_coordinaat = coordinates[0]
            y_coordinaat = coordinates[1]
            som = 0 
            
            eensgezinswoning = 1 
            bungalow = 2 
            maison = 3 
            
            while check == True:
                x = x_coordinaat - afstand_tot_huis
                x_ver = x_coordinaat + 12 + afstand_tot_huis
                y = y_coordinaat - afstand_tot_huis
                y_ver = y_coordinaat + 10 + afstand_tot_huis
                
                try: 
                    if eensgezinswoning in self.wijk[x:x_ver, y:y_ver] or bungalow in self.wijk[x:x_ver, y:y_ver] or maison in self.wijk[x:x_ver, y:y_ver]:
                        check = False
                    else:
                        self.total_eengezins = self.total_eengezins + self.percentage_eengezins
                        afstand_tot_huis += 1
                except IndexError:
                    if eensgezinswoning in self.wijk[x:x_ver, y:y_ver] or bungalow in self.wijk[x:x_ver, y:y_ver] or maison in self.wijk[x:x_ver, y:y_ver]:
                        check = False
                    else:
                        self.total_eengezins = self.total_eengezins + self.percentage_eengezins
                        afstand_tot_huis += 1

            
            
            # while som < 720 or som > 1000:
            #     x = x_coordinaat - afstand_tot_huis
            #     x_ver = x_coordinaat + 12 + afstand_tot_huis
            #     y = y_coordinaat - afstand_tot_huis
            #     y_ver = y_coordinaat + 10 + afstand_tot_huis
                
            #     try: 
            #         som = np.sum(self.wijk[x:x_ver, y:y_ver])
            #         if som < 720:
            #             self.total_eengezins = self.total_eengezins + self.percentage_eengezins
            #             afstand_tot_huis += 1 
            #     except IndexError:
            #         som = np.sum(self.wijk[(x_coordinaat - afstand_tot_huis):(x_coordinaat + 8 + afstand_tot_huis), (y_coordinaat - afstand_tot_huis):(y_coordinaat + 8 + afstand_tot_huis)])
            #         if som < 720:
            #             self.total_eengezins = self.total_eengezins + self.percentage_eengezins
            #             afstand_tot_huis += 1
            #         else: 
            #             break
            
            
            
            
            
            # while check == True:

            #     # check area of x-axis topside from the top left
            #     for i in range(range_maison_x):

            #         # if a house has been found in the area stop checking
            #         try:
            #             if self.wijk[coordinates[1] + locatie_outline_boven_x_as][coordinates[0] + locatie_outline_boven_y_as] == 1 or self.wijk[coordinates[1] + locatie_outline_boven_x_as][coordinates[0] + locatie_outline_boven_y_as] == 2 or self.wijk[coordinates[1] + locatie_outline_boven_x_as][coordinates[0] + locatie_outline_boven_y_as] == 3:
            #                 check = False
            #                 break
                        
            #             else:
                            
            #                 # update by incrementing variable to search area
            #                 locatie_outline_boven_x_as += 1
            #                 counter_x += 1 

            #         except IndexError:
            #             locatie_outline_boven_x_as += 1
            #             counter_x += 1

            #     # check area of y-axis leftside from the top left
            #     for i in range(range_maison_y):

            #         # if a house has been found in the area stop checking
            #         try: 
            #             if self.wijk[coordinates[1] + constante_x_links][coordinates[0] + locatie_outline_boven_y_as] == 1 or self.wijk[coordinates[1] + constante_x_links][coordinates[0] + locatie_outline_boven_y_as] == 2 or self.wijk[coordinates[1] + constante_x_links][coordinates[0] + locatie_outline_boven_y_as] == 3:
            #                 check = False
            #                 break
                        
            #             else:

            #                 # update by incrementing variable to search area
            #                 locatie_outline_boven_y_as += 1
            #                 counter_y += 1 

            #         except IndexError:
            #             locatie_outline_boven_y_as += 1
            #             counter_y += 1 

            #     # check area of x-axis bottomside from the bottom right
            #     for i in range(range_maison_x):
                    
            #         # if a house has been found in the area stop checking
            #         try:
            #             if self.wijk[coordinates[1] + locatie_outline_onder_x_as][coordinates[0] + locatie_outline_onder_y_as] == 1 or self.wijk[coordinates[1] + locatie_outline_onder_x_as][coordinates[0] + locatie_outline_onder_y_as] == 2 or self.wijk[coordinates[1] + locatie_outline_onder_x_as][coordinates[0] + locatie_outline_onder_y_as] == 3:
            #                 check = False
            #                 break

            #             else:

            #                 # update by incrementing variable to search area
            #                 locatie_outline_onder_x_as -= 1
            #                 counter_x_onder -= 1 

            #         except IndexError:
            #             locatie_outline_onder_x_as -= 1
            #             counter_x_onder -= 1 

            #     # check area of y-axis rightside from the bottom right
            #     for i in range(range_maison_y):
                    
            #         # if a house has been found in the area stop checking
            #         try:
            #             if self.wijk[coordinates[1] + constante_x_rechts][coordinates[0] + locatie_outline_onder_y_as] == 1 or self.wijk[coordinates[1] + constante_x_rechts][coordinates[0] + locatie_outline_onder_y_as] == 2 or self.wijk[coordinates[1] + constante_x_rechts][coordinates[0] + locatie_outline_onder_y_as] == 3:
            #                 check = False
            #                 break 

            #             else:
            #                 # update by incrementing variable to search area
            #                 locatie_outline_onder_y_as -= 1
            #                 counter_y_onder -= 1 

            #         except IndexError:
            #             locatie_outline_onder_y_as -= 1
            #             counter_y_onder -= 1 


            #     # reset tracers back to default values and increment by one in order to check next outline around the house
            #     locatie_outline_boven_x_as = locatie_outline_boven_x_as - counter_x - 1
            #     locatie_outline_boven_y_as = locatie_outline_boven_y_as - counter_y - 1
            #     constante_x_links = locatie_outline_boven_x_as

            #     # reset tracers back to default values and increment by one in order to check next outline around the house
            #     locatie_outline_onder_x_as = locatie_outline_onder_x_as - counter_x_onder - 1
            #     locatie_outline_onder_y_as = locatie_outline_onder_y_as - counter_x_onder - 1
            #     constante_x_rechts = locatie_outline_onder_x_as

            #     # reset counters back to default values
            #     counter_x = 0
            #     counter_y = 0 
            #     counter_x_onder = 0
            #     counter_y_onder = 0

            #     # When no houses found expand outline by 1 meter on every side
            #     range_maison_x += 2
            #     range_maison_y += 2  

            #     # adjust price of the house by the percentage increase
            #     if check == True:
            #         self.total_maison = self.total_maison + self.percentage_maison

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
    
    def move_maison(self, coordinaten_maison, coordinaten_bungalow, coordinaten_eensgezin, wijk):
        self.coordinaten_maison = coordinaten_maison
        self.coordinaten_bungalow = coordinaten_bungalow
        self.coordinaten_eensgezin = coordinaten_eensgezin

        price = Kosten(wijk, 12, 5, 3)
        counter = 0 

        for coordinaten in coordinaten_maison:
            
            lijst = []
            opbrengst = []
            lijst.append(coordinaten)

            new = price.total(coordinaten_maison, coordinaten_bungalow, coordinaten_eensgezin)
            opbrengst.append(new)

            # Linksboven
            wijk[coordinaten[0]:(coordinaten[0]+12) , coordinaten[1]:(coordinaten[1]+10)] = 0
            x = (coordinaten[0] - 1)
            y = (coordinaten[1] - 1)
            linksboven = [x,y]
            lijst.append(linksboven)

            # Draw
            wijk[x:x+12, y:y+10] = 3
            
            # Calculate
            coordinaten_maison[counter] = linksboven
            new = price.total(coordinaten_maison, coordinaten_bungalow, coordinaten_eensgezin)
            if wijk[x-6][y-6] == 1 or wijk[x-6][y-6] == 2 or wijk[x-6][y-6] == 3:
                new = 0
            else: 
                # Draw
                wijk[x:x+12, y:y+10] = 3
            
                # Calculate
                coordinaten_maison[counter] = linksboven
                new = price.total(coordinaten_maison, coordinaten_bungalow, coordinaten_eensgezin)

                opbrengst.append(new)

            # Boven
            wijk[x:x+12, y:y+10] = 0
            x = (coordinaten[0])
            y = (coordinaten[1] - 1)
            boven = [x,y]
            lijst.append(boven)

            # Draw
            wijk[x:x+12, y:y+10] = 3

            # Calculate
            coordinaten_maison[counter] = boven
            new = price.total(coordinaten_maison, coordinaten_bungalow, coordinaten_eensgezin)
            opbrengst.append(new)

            # Rechtsboven
            wijk[x:x+12, y:y+10] = 0
            x = coordinaten[0] + 1
            y = coordinaten[1] - 1
            rechtsboven = [x,y]
            lijst.append(rechtsboven)

            # Draw
            wijk[x:x+12, y:y+10] = 3

            # Calculate
            coordinaten_maison[counter] = rechtsboven
            new = price.total(coordinaten_maison, coordinaten_bungalow, coordinaten_eensgezin)
            opbrengst.append(new)

            # Rechts
            wijk[x:x+12, y:y+10] = 0
            x = coordinaten[0] + 1
            y = coordinaten[1]
            rechts = [x,y]
            lijst.append(rechts)

            # Draw
            wijk[x:x+12, y:y+10] = 3

            # Calculate
            coordinaten_maison[counter] = rechts
            new = price.total(coordinaten_maison, coordinaten_bungalow, coordinaten_eensgezin)
            opbrengst.append(new)

            # Rechtsonder
            wijk[x:x+12, y:y+10] = 0
            x = coordinaten[0] + 1
            y = coordinaten[1] + 1
            rechtsonder = [x,y]
            lijst.append(rechtsonder)

            # Draw
            wijk[x:x+12, y:y+10] = 3

            # Calculate
            coordinaten_maison[counter] = rechtsonder
            new = price.total(coordinaten_maison, coordinaten_bungalow, coordinaten_eensgezin)
            opbrengst.append(new)

            # Onder
            wijk[x:x+12, y:y+10] = 0
            x = coordinaten[0] 
            y = coordinaten[1] + 1
            onder = [x,y]
            lijst.append(onder)

            # Draw
            wijk[x:x+12, y:y+10] = 3

            # Calculate
            coordinaten_maison[counter] = onder
            new = price.total(coordinaten_maison, coordinaten_bungalow, coordinaten_eensgezin)
            opbrengst.append(new)

            # Linksonder
            wijk[x:x+12, y:y+10] = 0
            x = coordinaten[0] - 1
            y = coordinaten[1] + 1
            linksonder = [x,y]
            lijst.append(linksonder)

            # Draw
            wijk[x:x+12, y:y+10] = 3

            # Calculate
            coordinaten_maison[counter] = linksonder
            new = price.total(coordinaten_maison, coordinaten_bungalow, coordinaten_eensgezin)
            opbrengst.append(new)

            # Links
            wijk[x:x+12, y:y+10] = 0
            x = coordinaten[0] - 1
            y = coordinaten[1]
            links = [x,y]
            lijst.append(links)
            
            # Draw
            wijk[x:x+12, y:y+10] = 3

            # Calculate
            coordinaten_maison[counter] = links
            new = price.total(coordinaten_maison, coordinaten_bungalow, coordinaten_eensgezin)
            opbrengst.append(new)

            # Getting the best option
            hoogste = max(opbrengst)
            index = opbrengst.index(hoogste)
            best_coor = lijst[index]
            # Draw
            wijk[best_coor[0]: best_coor[0]+12, best_coor[1]: best_coor[1]+10]

            coordinaten_maison[counter] = best_coor

            counter += 1

            
    def move_eensgezin(self, coordinaten_maison, coordinaten_bungalow, coordinaten_eensgezin, wijk):
        self.coordinaten_maison = coordinaten_maison
        self.coordinaten_bungalow = coordinaten_bungalow
        self.coordinaten_eensgezin = coordinaten_eensgezin

        price = Kosten(wijk, 12, 5, 3)
        counter = 0 

        for coordinaten in coordinaten_eensgezin:
            
            lijst = []
            opbrengst = []

            lijst.append(coordinaten)
            
            new = price.total(coordinaten_maison, coordinaten_bungalow, coordinaten_eensgezin)
            opbrengst.append(new)

            # Linksboven
            wijk[coordinaten[0]:(coordinaten[0]+8) , coordinaten[1]:(coordinaten[1]+8)] = 0
            x = (coordinaten[0] - 1)
            y = (coordinaten[1] - 1)
            linksboven = [x,y]
            lijst.append(linksboven)

            # Draw
            wijk[x:x+8, y:y+8] = 1
            
            # Calculate
            coordinaten_eensgezin[counter] = linksboven
            new = price.total(coordinaten_maison, coordinaten_bungalow, coordinaten_eensgezin)
            opbrengst.append(new)

            # Boven
            wijk[x:x+8, y:y+8] = 0
            x = (coordinaten[0])
            y = (coordinaten[1] - 1)
            boven = [x,y]
            lijst.append(boven)

            # Draw
            wijk[x:x+8, y:y+8] = 1

            # Calculate
            coordinaten_eensgezin[counter] = boven
            new = price.total(coordinaten_maison, coordinaten_bungalow, coordinaten_eensgezin)
            opbrengst.append(new)

            # Rechtsboven
            wijk[x:x+8, y:y+8] = 0
            x = coordinaten[0] + 1
            y = coordinaten[1] - 1
            rechtsboven = [x,y]
            lijst.append(rechtsboven)

            # Draw
            wijk[x:x+8, y:y+8] = 1

            # Calculate
            coordinaten_eensgezin[counter] = rechtsboven
            new = price.total(coordinaten_maison, coordinaten_bungalow, coordinaten_eensgezin)
            opbrengst.append(new)

            # Rechts
            wijk[x:x+8, y:y+8] = 0
            x = coordinaten[0] + 1
            y = coordinaten[1]
            rechts = [x,y]
            lijst.append(rechts)

            # Draw
            wijk[x:x+8, y:y+8] = 1

            # Calculate
            coordinaten_eensgezin[counter] = rechts
            new = price.total(coordinaten_maison, coordinaten_bungalow, coordinaten_eensgezin)
            opbrengst.append(new)

            # Rechtsonder
            wijk[x:x+8, y:y+8] = 0
            x = coordinaten[0] + 1
            y = coordinaten[1] + 1
            rechtsonder = [x,y]
            lijst.append(rechtsonder)

            # Draw
            wijk[x:x+8, y:y+8] = 1

            # Calculate
            coordinaten_eensgezin[counter] = rechtsonder
            new = price.total(coordinaten_maison, coordinaten_bungalow, coordinaten_eensgezin)
            opbrengst.append(new)

            # Onder
            wijk[x:x+8, y:y+8] = 0
            x = coordinaten[0] 
            y = coordinaten[1] + 1
            onder = [x,y]
            lijst.append(onder)

            # Draw
            wijk[x:x+8, y:y+8] = 1

            # Calculate
            coordinaten_eensgezin[counter] = onder
            new = price.total(coordinaten_maison, coordinaten_bungalow, coordinaten_eensgezin)
            opbrengst.append(new)

            # Linksonder
            wijk[x:x+8, y:y+8] = 0
            x = coordinaten[0] - 1
            y = coordinaten[1] + 1
            linksonder = [x,y]
            lijst.append(linksonder)

            # Draw
            wijk[x:x+8, y:y+8] = 1

            # Calculate
            coordinaten_eensgezin[counter] = linksonder
            new = price.total(coordinaten_maison, coordinaten_bungalow, coordinaten_eensgezin)
            opbrengst.append(new)

            # Links
            wijk[x:x+8, y:y+8] = 0
            x = coordinaten[0] - 1
            y = coordinaten[1]
            links = [x,y]
            lijst.append(links)
            
            # Draw
            wijk[x:x+8, y:y+8] = 1

            # Calculate
            coordinaten_eensgezin[counter] = links
            new = price.total(coordinaten_maison, coordinaten_bungalow, coordinaten_eensgezin)
            opbrengst.append(new)

            # Getting the best option
            hoogste = max(opbrengst)
            index = opbrengst.index(hoogste)
            best_coor = lijst[index]

            # Draw
            wijk[best_coor[0]: best_coor[0]+8, best_coor[1]: best_coor[1]+8]

            coordinaten_eensgezin[counter] = best_coor

            counter += 1
            
            
            
            
            # # Linksboven
            # linksboven = [(coordinaten[0] - 1), (coordinaten[1] - 1)]
            # lijst.append(linksboven)
            # coordinaten_eensgezin[counter] = linksboven
            # new = price.total(coordinaten_maison, coordinaten_bungalow, coordinaten_eensgezin)
            # opbrengst.append(new)


            # # Boven
            # boven = [(coordinaten[0]), (coordinaten[1] - 1)]
            # lijst.append(boven)
            # coordinaten_eensgezin[counter] = boven
            # new = price.total(coordinaten_maison, coordinaten_bungalow, coordinaten_eensgezin)
            # opbrengst.append(new)

            # # Rechtsboven
            # rechtsboven = [(coordinaten[0] + 1), (coordinaten[1] - 1)]
            # lijst.append(rechtsboven)
            # coordinaten_eensgezin[counter] = rechtsboven
            # new = price.total(coordinaten_maison, coordinaten_bungalow, coordinaten_eensgezin)
            # opbrengst.append(new)

            # # Rechts
            # rechts = [(coordinaten[0] + 1), (coordinaten[1])]
            # lijst.append(rechts)
            # coordinaten_eensgezin[counter] = rechts
            # new = price.total(coordinaten_maison, coordinaten_bungalow, coordinaten_eensgezin)
            # opbrengst.append(new)

            # # Rechtsonder
            # rechtsonder = [(coordinaten[0] + 1), (coordinaten[1] + 1)]
            # lijst.append(rechtsonder)
            # coordinaten_eensgezin[counter] = rechtsonder
            # new = price.total(coordinaten_maison, coordinaten_bungalow, coordinaten_eensgezin)
            # opbrengst.append(new)

            # # Onder
            # onder = [(coordinaten[0]), (coordinaten[1] + 1)]
            # lijst.append(onder)
            # coordinaten_eensgezin[counter] = onder
            # new = price.total(coordinaten_maison, coordinaten_bungalow, coordinaten_eensgezin)
            # opbrengst.append(new)

            # # Linksonder
            # linksonder = [(coordinaten[0] - 1), (coordinaten[1] + 1)]
            # lijst.append(linksonder)
            # coordinaten_eensgezin[counter] = linksonder
            # new = price.total(coordinaten_maison, coordinaten_bungalow, coordinaten_eensgezin)
            # opbrengst.append(new)

            # # Links
            # links = [(coordinaten[0] - 1), (coordinaten[1])]
            # lijst.append(links)
            # coordinaten_eensgezin[counter] = links
            # new = price.total(coordinaten_maison, coordinaten_bungalow, coordinaten_eensgezin)
            # opbrengst.append(new)

            # # Getting the best option
            # hoogste = max(opbrengst)
            # index = opbrengst.index(hoogste)
            # best_coor = lijst[index]
            # coordinaten_eensgezin[counter] = best_coor

            # counter += 1 
            

    def move_bungalow(self, coordinaten_maison, coordinaten_bungalow, coordinaten_eensgezin, wijk):
        self.coordinaten_maison = coordinaten_maison
        self.coordinaten_bungalow = coordinaten_bungalow
        self.coordinaten_eensgezin = coordinaten_eensgezin

        price = Kosten(wijk, 12, 5, 3)
        counter = 0 

        for coordinaten in coordinaten_bungalow:
            lijst = []
            opbrengst = []

            lijst.append(coordinaten)
         
            new = price.total(coordinaten_maison, coordinaten_bungalow, coordinaten_eensgezin)
            opbrengst.append(new)

            # Linksboven
            wijk[coordinaten[0]:(coordinaten[0]+11) , coordinaten[1]:(coordinaten[1]+7)] = 0
            x = (coordinaten[0] - 1)
            y = (coordinaten[1] - 1)
            linksboven = [x,y]
            lijst.append(linksboven)

            # Draw
            wijk[x:x+11, y:y+7] = 2
            
            # Calculate
            coordinaten_bungalow[counter] = linksboven
            new = price.total(coordinaten_maison, coordinaten_bungalow, coordinaten_eensgezin)
            opbrengst.append(new)

            # Boven
            wijk[x:x+11, y:y+7] = 0
            x = (coordinaten[0])
            y = (coordinaten[1] - 1)
            boven = [x,y]
            lijst.append(boven)

            # Draw
            wijk[x:x+11, y:y+7] = 2

            # Calculate
            coordinaten_bungalow[counter] = boven
            new = price.total(coordinaten_maison, coordinaten_bungalow, coordinaten_eensgezin)
            opbrengst.append(new)

            # Rechtsboven
            wijk[x:x+11, y:y+7] = 0
            x = coordinaten[0] + 1
            y = coordinaten[1] - 1
            rechtsboven = [x,y]
            lijst.append(rechtsboven)

            # Draw
            wijk[x:x+11, y:y+7] = 2

            # Calculate
            coordinaten_bungalow[counter] = rechtsboven
            new = price.total(coordinaten_maison, coordinaten_bungalow, coordinaten_eensgezin)
            opbrengst.append(new)

            # Rechts
            wijk[x:x+11, y:y+7] = 0
            x = coordinaten[0] + 1
            y = coordinaten[1]
            rechts = [x,y]
            lijst.append(rechts)

            # Draw
            wijk[x:x+11, y:y+7] = 2

            # Calculate
            coordinaten_bungalow[counter] = rechts
            new = price.total(coordinaten_maison, coordinaten_bungalow, coordinaten_eensgezin)
            opbrengst.append(new)

            # Rechtsonder
            wijk[x:x+11, y:y+7] = 0
            x = coordinaten[0] + 1
            y = coordinaten[1] + 1
            rechtsonder = [x,y]
            lijst.append(rechtsonder)

            # Draw
            wijk[x:x+11, y:y+7] = 2

            # Calculate
            coordinaten_bungalow[counter] = rechtsonder
            new = price.total(coordinaten_maison, coordinaten_bungalow, coordinaten_eensgezin)
            opbrengst.append(new)

            # Onder
            wijk[x:x+11, y:y+7] = 0
            x = coordinaten[0] 
            y = coordinaten[1] + 1
            onder = [x,y]
            lijst.append(onder)

            # Draw
            wijk[x:x+11, y:y+7] = 2

            # Calculate
            coordinaten_bungalow[counter] = onder
            new = price.total(coordinaten_maison, coordinaten_bungalow, coordinaten_eensgezin)
            opbrengst.append(new)

            # Linksonder
            wijk[x:x+11, y:y+7] = 0
            x = coordinaten[0] - 1
            y = coordinaten[1] + 1
            linksonder = [x,y]
            lijst.append(linksonder)

            # Draw
            wijk[x:x+11, y:y+7] = 2

            # Calculate
            coordinaten_bungalow[counter] = linksonder
            new = price.total(coordinaten_maison, coordinaten_bungalow, coordinaten_eensgezin)
            opbrengst.append(new)

            # Links
            wijk[x:x+11, y:y+7] = 0
            x = coordinaten[0] - 1
            y = coordinaten[1]
            links = [x,y]
            lijst.append(links)
            
            # Draw
            wijk[x:x+11, y:y+7] = 2

            # Calculate
            coordinaten_bungalow[counter] = links
            new = price.total(coordinaten_maison, coordinaten_bungalow, coordinaten_eensgezin)
            opbrengst.append(new)

            # Getting the best option
            hoogste = max(opbrengst)
            index = opbrengst.index(hoogste)
            best_coor = lijst[index]
            
            # Draw
            wijk[best_coor[0]: best_coor[0]+8, best_coor[1]: best_coor[1]+8]

            coordinaten_bungalow[counter] = best_coor

            counter += 1
            # lijst = []
            # opbrengst = []

            # lijst.append(coordinaten)
            # coordinates = coordinaten_bungalow
         
            # new = price.total(coordinaten_bungalow, coordinates, coordinaten_eensgezin)
            # opbrengst.append(new)

            # # Linksboven
            # linksboven = [(coordinaten[0] - 1), (coordinaten[1] - 1)]
            # lijst.append(linksboven)
            # coordinaten_bungalow[counter] = linksboven
            # new = price.total(coordinaten_maison, coordinaten_bungalow, coordinaten_eensgezin)
            # opbrengst.append(new)

            # # Boven
            # boven = [(coordinaten[0]), (coordinaten[1] - 1)]
            # lijst.append(boven)
            # coordinaten_bungalow[counter] = boven
            # new = price.total(coordinaten_maison, coordinaten_bungalow, coordinaten_eensgezin)
            # opbrengst.append(new)

            # # Rechtsboven
            # rechtsboven = [(coordinaten[0] + 1), (coordinaten[1] - 1)]
            # lijst.append(rechtsboven)
            # coordinaten_bungalow[counter] = rechtsboven
            # new = price.total(coordinaten_maison, coordinaten_bungalow, coordinaten_eensgezin)
            # opbrengst.append(new)

            # # Rechts
            # rechts = [(coordinaten[0] + 1), (coordinaten[1])]
            # lijst.append(rechts)
            # coordinaten_bungalow[counter] = rechts
            # new = price.total(coordinaten_maison, coordinaten_bungalow, coordinaten_eensgezin)
            # opbrengst.append(new)

            # # Rechtsonder
            # rechtsonder = [(coordinaten[0] + 1), (coordinaten[1] + 1)]
            # lijst.append(rechtsonder)
            # coordinaten_bungalow[counter] = rechtsonder
            # new = price.total(coordinaten_maison, coordinaten_bungalow, coordinaten_eensgezin)
            # opbrengst.append(new)

            # # Onder
            # onder = [(coordinaten[0]), (coordinaten[1] + 1)]
            # lijst.append(onder)
            # coordinaten_bungalow[counter] = onder
            # new = price.total(coordinaten_maison, coordinaten_bungalow, coordinaten_eensgezin)
            # opbrengst.append(new)

            # # Linksonder
            # linksonder = [(coordinaten[0] - 1), (coordinaten[1] + 1)]
            # lijst.append(linksonder)
            # coordinaten_bungalow[counter] = linksonder
            # new = price.total(coordinaten_maison, coordinaten_bungalow, coordinaten_eensgezin)
            # opbrengst.append(new)

            # # Links
            # links = [(coordinaten[0] - 1), (coordinaten[1])]
            # lijst.append(links)
            # coordinaten_bungalow[counter] = links
            # new = price.total(coordinaten_maison, coordinaten_bungalow, coordinaten_eensgezin)
            # opbrengst.append(new)

            # # Getting the best option
            # hoogste = max(opbrengst)
            # index = opbrengst.index(hoogste)
            # best_coor = lijst[index]
            # coordinaten_bungalow[counter] = best_coor

            # counter += 1 


def main():
    
    wijk_type = 1
    runs = 1

    total_prices = []

    for i in range(runs):
        # create a 160 x 180 gridmap
        x, y = (160, 180) 
        wijk = [[0 for i in range(x)] for j in range(y)] 

        # adding houses
        price = Kosten(wijk, 12, 5, 3)
        place = Placing(wijk, 12, 5, 3)
        move = Move()

        # create the possible water area coordinates for the gridmap outline
        wijk1_top_left = [[0, 0]]
        wijk1_bottom_right = [[32, 180]]
        wijk2_top_left = [[0, 135], [0, 0], [128, 135], [128, 0]]
        wijk2_bottom_right = [[32, 180], [32, 45], [160, 180], [160, 45]]
        wijk3_top_left = [[44, 50]]
        wijk3_bottom_right = [[116, 130]]

        # save wijk coordinates for water placement
        if wijk_type == 1:
            wijk_top_left = wijk1_top_left
            wijk_bottom_right = wijk1_bottom_right
        if wijk_type == 2:
            wijk_top_left = wijk2_top_left
            wijk_bottom_right = wijk2_bottom_right
        if wijk_type == 3:
            wijk_top_left = wijk3_top_left
            wijk_bottom_right = wijk3_bottom_right

        # create the different water values of the gridmap
        place.water(wijk_top_left, wijk_bottom_right)

        coordinaten_eensgezin = place.eensgezinswoningen(12)
        coordinaten_maison = place.maison(3, coordinaten_eensgezin)
        coordinaten_bungalow = place.bungalow(5, coordinaten_eensgezin, coordinaten_maison)

        # print("Voor move")
        # print(coordinaten_eensgezin)
        # print(coordinaten_bungalow)
        # print(coordinaten_maison)

        totaal = price.total(coordinaten_maison, coordinaten_bungalow, coordinaten_eensgezin)

        # for i in range(0,3):
        #     move.move_maison(coordinaten_maison, coordinaten_bungalow, coordinaten_eensgezin, wijk)
        #     move.move_eensgezin(coordinaten_maison, coordinaten_bungalow, coordinaten_eensgezin, wijk)
        #     move.move_bungalow(coordinaten_maison, coordinaten_bungalow, coordinaten_eensgezin, wijk)

        # print("Na move")
        # print(coordinaten_eensgezin)
        # print(coordinaten_bungalow)
        # print(coordinaten_maison)



        totaal = price.total(coordinaten_maison, coordinaten_bungalow, coordinaten_eensgezin)
        total_prices.append(totaal)

        # save current wijk with the highest price 
        if totaal >= max(total_prices):
            wijk_max = wijk
            print(max(total_prices))

    # calculate and show statistics
    mean = statistics.mean(total_prices)
    print()
    print("Wijk", wijk_type, ":", runs, "runs")
    print("Mean:", mean)
    print("Max:", max(total_prices))
    print()

    # create visualization
    H = np.array(wijk_max)
    plt.imshow(H)

    ca = np.array([[0, 102, 204, 0],
                  [1, 255, 51, 51],
                  [2, 255, 153, 51],
                  [3, 255, 255, 51],
                  [4, 102, 178, 255],
                  [5, 192, 192, 192]])
    colors = ca[ca[:,0].argsort()][:,1:]/255.
    cmap = matplotlib.colors.ListedColormap(colors)
    plt.pcolor(H, cmap = cmap)
    plt.title("Visualisatie Wijk " + str(wijk_type))
    plt.show()

    # create boxplot
    fig, ax1 = plt.subplots()
    ax1.boxplot(total_prices)
    ax1.yaxis.grid(True, linestyle='-', which='major', color='lightgrey', alpha=0.5)
    plt.title("Boxplot Wijk " + str(wijk_type))
    ax1.set_ylabel("Price")
    plt.xticks([1], ["Wijk" + str(wijk_type)])
    bottom = 7500000
    top = 10000000
    ax1.set_ylim(bottom, top)
    plt.show()

    # saving in csv file
    with open("wijk1.csv","w+") as my_csv:
        csvWriter = csv.writer(my_csv,delimiter=',')
        csvWriter.writerows(wijk_max)


if __name__ == '__main__':
    main()