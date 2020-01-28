import random
import statistics
import csv
import numpy as np 
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.colors


class Placing:

    """ All houses are being placed on the created gridmap called "neighbourhood". This 
    is done by scanning the ground for empty space after which the houses are placed one by one.
    Furthermore the water is created and placed. """

    def __init__(self, neighbourhood, houses, neighbourhood_type):
        
        self.neighbourhood = neighbourhood
        self.amount_single = int(houses * 0.6)
        self.amount_maison = int(houses * 0.15)
        self.amount_bungalow = int(houses * 0.25)
        self.neighbourhood_type = neighbourhood_type
        self.index_single = 1
        self.index_bungalow = 2
        self.index_maison = 3 
        self.index_water = 4
        self.index_free_space = 5

    def place_water(self):

        """ Depending on the type of neighbourhood, water is added on the gridmap. 
        The type of neighbourhood is given as an argument when calling the whole Class.
        The area where the water should be generated is changed from an "empty" value to a "water" value. """

        # change values in array to "water" values, when neighbourhood type is 1
        if self.neighbourhood_type == 1:
            self.neighbourhood[0:180, 0:32] = 4

        # change values in array to "water" values, when neighbourhood type is 2
        if self.neighbourhood_type == 2:
            self.neighbourhood[135:180, 0:32] = 4
            self.neighbourhood[0:45, 0:32] = 4
            self.neighbourhood[135:180, 128:160] = 4
            self.neighbourhood[0:45, 128:160] = 4

        # change values in array to "water" values, when neighbourhood type is 2
        if self.neighbourhood_type == 3:
            self.neighbourhood[50:130, 44:116] = 4

        return self.neighbourhood_type

    def place_single(self):

        """ Random coordinates for an single family home are generated and placed in the neighbourhood.
        If the area around the randomized coordinate fits this specific type of house, the house is placed and saved
        in the coordinates list. """

        # create empty coordinates list for each type of house
        single_coordinatenlijst = [[0,0]] * self.amount_single
        coordinaten_maison = [[0,0]] * self.amount_maison
        coordinaten_bungalow = [[0,0]] * self.amount_bungalow

        # amount of times a house is placed
        for i in range(0,self.amount_single):

            # generate random coordinates for the upper-left corner of a single family home
            # the coordinates should fit the range of the neighbourhood, which is dependent on the size of the house
            # the size of a single family home is 10x10 metres including obligatory free space
            # from the upper-left corner of the house, the ranges of the random coordinates should fall between 2-150 (x-axis) and 2-170 (y-axis)
            x = random.randrange(2,150)
            y = random.randrange(2,170)

            # create new coordinates whenever a coordinate does not meet the requirements
            check = True
            while check == True:

                # new coordinates when water present in new house
                if self.index_water in self.neighbourhood[y:(y+8),x:(x+8)]:
                    x = random.randrange(2,150)
                    y = random.randrange(2,170)

                # new coordinate when another house already present in new house
                elif self.index_single in self.neighbourhood[(y-2):(y+10),(x-2):(x+10)] or self.index_bungalow in self.neighbourhood[(y-2):(y+10),(x-2):(x+10)] or self.index_maison in self.neighbourhood[(y-2):(y+10),(x-2):(x+10)]:
                    x = random.randrange(2,150)
                    y = random.randrange(2,170)

                # new coordinate when obligatory free space from another house present in new house
                elif self.index_free_space in self.neighbourhood[y:(y+8),x:(x+8)]:
                    x = random.randrange(2,150)
                    y = random.randrange(2,170)

                # coordinate is valid
                else:
                    check = False

            # new coordinates are saved in coordinates list
            new_coor = [x,y]
            single_coordinatenlijst[i] = new_coor

            # draw house on the gridmap
            self.neighbourhood[(y - 2):(y + 10),(x - 2):(x + 10)] = 5
            self.neighbourhood[y:(y + 8),x:(x + 8)] = 1

        return single_coordinatenlijst

    def place_maison(self, coordinaten_single):

        """ Random coordinates for a maison are generated and placed in the neighbourhood.
        If the area around the randomized coordinate fits this specific type of house, the house is placed and saved
        in the coordinates list. """

        # create empty coordinates list of remaining house types
        coordinaten_maison = [[0,0]] * self.amount_maison
        maison_coordinatenlijst = coordinaten_maison
        coordinaten_bungalow = [[0,0]] * self.amount_bungalow

        # amount of times a house is placed
        for i in range(0,self.amount_maison):

            # generate random coordinates for the upper-left corner of a maison
            # the coordinates should fit the range of the neighbourhood, which is dependent on the size of the house
            # the size of a maison is 18x16 metres including obligatory free space
            # from the upper-left corner of the house, the ranges of the random coordinates should fall between 6-142 (x-axis) and 6-164 (y-axis)
            x = random.randrange(6,142)
            y = random.randrange(6,164)
            
            # create new coordinates whenever a coordinate does not meet the requirements
            check = True
            while check == True:

                # new coordinates when water present in new house
                if self.index_water in self.neighbourhood[y:(y+10),x:(x+12)]:
                    x = random.randrange(6,142)
                    y = random.randrange(6,164)

                # new coordinates when another house already present in new house
                elif self.index_single in self.neighbourhood[(y-6):(y+16),(x-6):(x+18)] or self.index_bungalow in self.neighbourhood[(y-6):(y+16),(x-6):(x+18)] or self.index_maison in self.neighbourhood[(y-6):(y+16),(x-6):(x+18)]:
                    x = random.randrange(6,142)
                    y = random.randrange(6,164)

                # new coordinates when obligatory free space from another house present in new house
                elif self.index_free_space in self.neighbourhood[y:(y+10),x:(x+12)]:
                    x = random.randrange(6,142)
                    y = random.randrange(6,164)

                # coordinate is valid
                else:
                    check = False

            # new coordinates are saved in coordinates list
            new_coor = [x,y]
            maison_coordinatenlijst[i] = new_coor

            # draw every house on the gridmap
            self.neighbourhood[(y - 6):(y + 16),(x - 6):(x + 18)] = 5
            self.neighbourhood[y:(y + 10),x:(x + 12)] = 3
        
        return maison_coordinatenlijst

    def place_bungalow(self, coordinaten_single, coordinaten_maison):

        """ Random coordinates for a bungalow are generated and placed in the neighbourhood.
        If the area around the randomized coordinate fits this specific type of house, the house is placed and saved
        in the coordinates list. """
         
        # create empty coordinates list for bungalow
        coordinaten_bungalow = [[0,0]] * self.amount_bungalow
        bungalow_coordinatenlijst = coordinaten_bungalow

        # amount of times a bungalow is placed
        for i in range(0,self.amount_bungalow):

            # generate random coordinates for the upper-left corner of a bungalow
            # the coordinates should fit the range of the neighbourhood, which is dependent on the size of the house
            # the size of a maison is 14x10 metres including obligatory free space
            # from the upper-left corner of the house, the ranges of the random coordinates should fall between 3-146 (x-axis) and 2-170 (y-axis)
            x = random.randrange(3,146)
            y = random.randrange(3,170)

            # create new coordinates whenever a coordinate does not meet the requirements
            check = True
            while check == True:

                # new coordinates when water present in new house
                if self.index_water in self.neighbourhood[y:(y+7),x:(x+11)]:
                    x = random.randrange(3,146)
                    y = random.randrange(3,170)

                # new coordinates when another house already present in new house
                elif self.index_single in self.neighbourhood[(y-3):(y+10),(x-3):(x+14)] or self.index_bungalow in self.neighbourhood[(y-3):(y+10),(x-3):(x+14)] or self.index_maison in self.neighbourhood[(y-3):(y+10),(x-3):(x+14)]:
                    x = random.randrange(3,146)
                    y = random.randrange(3,170)

                # new coordinates when obligatory free space from another house present in new house
                elif self.index_free_space in self.neighbourhood[y:(y+7),x:(x+11)]:
                    x = random.randrange(3,146)
                    y = random.randrange(3,170)
                
                # coordinate is valid
                else:
                    check = False

            # new coordinates are saved in coordinates list
            new_coor = [x,y]
            bungalow_coordinatenlijst[i] = new_coor

            # draw every house on the gridmap
            self.neighbourhood[(y - 3):(y + 10),(x - 3):(x + 14)] = 5
            self.neighbourhood[y:(y + 7),x:(x + 11)] = 2

        return bungalow_coordinatenlijst


class Price():

    """ In each method, the price of a certain housetype is calculated. 
    In the last method, the total price of the neighbourhood will be calculated.
    All houses have a default price, but for every meter of free space around a house, the value of a house will increase. """

    def __init__(self, neighbourhood, single_amount, bungalow_amount, maison_amount):
        
        self.neighbourhood = neighbourhood
        self.single_amount = single_amount
        self.bungalow_amount = bungalow_amount
        self.maison_amount = maison_amount
        
    def single_cost(self, coordinates):

        """ The total price for each single family house is calculated. 
        The extra price per house is dependent on the free space that surrounds the house. 
        This is done by looking up the coordinates of every house in the coordinates list saved when placing the houses. 
        From these coordinates the free space around the houses are checked and the total house price is being adjusted. """

        # set default price of a single family home
        self.single = 285000 

        # calculate percentage of extra housing worth per extra square meter space
        self.percentage_single = self.single * 0.03

        # make default total price of all single family houses
        self.total_single = self.single_amount * self.single

        # retrieve coordinates
        coordinateslist = coordinates

        # check the outline of every single family house for extra free space
        for coordinate in coordinateslist:
            single = 1 
            bungalow = 2 
            maison = 3      

            # free space is calculated by checking the distance between house and its surroundings.
            distance = 3 

            x_coordinaat = coordinate[0]
            y_coordinaat = coordinate[1]

            # check for free space around house until another house is found
            check = True
            while check == True:

                # the distance between house and its surroundings is increased by one for each run to check for more free space
                # the free space around a house is checked on each side (up, down, left and right)
                x = x_coordinaat - distance
                x_ver = x_coordinaat + 8 + distance
                y = y_coordinaat - distance
                y_ver = y_coordinaat + 8 + distance

                # reset coordinates when out of boundary, because extra free space is able to 'go over' the boundaries
                if x < 0:
                    x = 0 

                if x_ver > 160:
                    x_ver = 160

                if y < 0:
                    y = 0

                if y_ver > 180:
                    y_ver = 180

                # remove current house from the gridmap
                self.neighbourhood[(y_coordinaat - 2):(y_coordinaat + 10),(x_coordinaat - 2):(x_coordinaat + 10)] = 0
    
                # check for other house in given range of free space
                try:
                    if single in self.neighbourhood[y:y_ver, x:x_ver] or bungalow in self.neighbourhood[y:y_ver, x:x_ver] or maison in self.neighbourhood[y:y_ver, x:x_ver]:
                        check = False

                    # when no house is found, recalculate total price and add one extra meter of free space
                    else:
                        self.total_single = self.total_single + self.percentage_single
                        distance += 1
                
                # check for IndexError to be sure a coordinate does not go out of range
                except IndexError:
                    if single in self.neighbourhood[y:y_ver, x:x_ver] or bungalow in self.neighbourhood[y:y_ver, x:x_ver] or maison in self.neighbourhood[y:y_ver, x:x_ver]:
                        check = False
                    else:
                        self.total_single = self.total_single + self.percentage_single
                        distance += 1

            # redraw house on the gridmap
            self.neighbourhood[(y_coordinaat - 2):(y_coordinaat + 10),(x_coordinaat - 2):(x_coordinaat + 10)] = 5
            self.neighbourhood[y_coordinaat:(y_coordinaat + 8),x_coordinaat:(x_coordinaat + 8)] = 1

        return self.total_single
        
    def bungalow_cost(self, coordinates):

        """ The total price for each bungalow is calculated. 
        The extra price per house is dependent on the free space that surrounds the house. 
        This is done by looking up the coordinates of every house in the coordinates list saved when placing the houses. 
        From these coordinates the free space around the houses are checked and the total house price is being adjusted. """

        # set default price of a bungalow
        self.bungalow = 399000

        # calculate percentage of extra housing worth per extra square meter space
        self.percentage_bungalow = self.bungalow * 0.04

        # make default total price of all bungalows
        self.total_bungalow = self.bungalow_amount * self.bungalow

        # retrieve coordinates
        coordinateslist = coordinates

        # check the outline of every bungalow for extra free space
        for coordinate in coordinateslist:

            single = 1 
            bungalow = 2 
            maison = 3
            
            # free space is calculated by checking the distance between house and its surroundings.
            distance = 4

            x_coordinaat = coordinate[0]
            y_coordinaat = coordinate[1]
                        
            # check for free space around house until another house is found
            check = True
            while check == True:

                # distance between house and its surroundings is increased by one for each run to check for more free space
                # free space around a house is checked on each side (up, down, left and right)
                x = x_coordinaat - distance
                x_ver = x_coordinaat + 11 + distance
                y = y_coordinaat - distance
                y_ver = y_coordinaat + 7 + distance

                # reset coordinates when out of boundary, because extra free space is able to 'go over' the boundaries
                if x < 0:
                    x = 0 

                if x_ver > 160:
                    x_ver=160

                if y < 0:
                    y = 0
            
                if y_ver > 180:
                    y_ver = 180
   
                # remove current house from the gridmap
                self.neighbourhood[(y_coordinaat - 3):(y_coordinaat + 10),(x_coordinaat - 3):(x_coordinaat + 14)] = 0

                # check for other house in given range of free space
                try: 
                    if single in self.neighbourhood[y:y_ver, x:x_ver] or bungalow in self.neighbourhood[y:y_ver, x:x_ver] or maison in self.neighbourhood[y:y_ver, x:x_ver]:
                        check = False

                    # when no house is found, recalculate total price and add one extra meter of free space
                    else:
                        self.total_single = self.total_single + self.percentage_single
                        distance += 1 

                # check for IndexError to be sure a coordinate does not go out of range
                except IndexError:
                    if single in self.neighbourhood[y:y_ver, x:x_ver] or bungalow in self.neighbourhood[y:y_ver, x:x_ver] or maison in self.neighbourhood[y:y_ver, x:x_ver]:
                        check = False
                    else:
                        self.total_single = self.total_single + self.percentage_single
                        distance += 1 

            # redraw house on the gridmap
            self.neighbourhood[(y_coordinaat - 3):(y_coordinaat + 10),(x_coordinaat - 3):(x_coordinaat + 14)] = 5
            self.neighbourhood[y_coordinaat:(y_coordinaat + 7),x_coordinaat:(x_coordinaat + 11)] = 2

        return self.total_bungalow

    def maison_cost(self, coordinates):

        """ The total price for each maison is calculated. 
        The extra price per house is dependent on the free space that surrounds the house. 
        This is done by looking up the coordinates of every house in the coordinates list saved when placing the houses. 
        From these coordinates the free space around the houses are checked and the total house price is being adjusted. """
        
        # set default price of a maison
        self.maison = 610000

        # calculate percentage of extra housing worth per extra square meter space
        self.percentage_maison = self.maison * 0.06

        # make default total price of all maisons
        self.total_maison = self.maison_amount * self.maison

        # getting the coordinates from placing class
        coordinateslist = coordinates

        # check the outline of every maison
        for coordinate in coordinateslist:

            # free space is calculated by checking the distance between house and its surroundings.
            distance = 7

            x_coordinaat = coordinate[0]
            y_coordinaat = coordinate[1]
            
            single = 1 
            bungalow = 2 
            maison = 3 
            
            # check for free space around house until another house is found
            check = True
            while check == True:

                # distance between house and its surroundings is increased by one for each run to check for more free space
                # free space around a house is checked on each side (up, down, left and right)
                x = x_coordinaat - distance
                x_ver = x_coordinaat + 12 + distance
                y = y_coordinaat - distance
                y_ver = y_coordinaat + 10 + distance

                # reset coordinates when out of boundary, because extra free space is able to 'go over' the boundaries
                if x < 0:
                    x = 0 

                if x_ver > 160:
                    x_ver = 160

                if y < 0:
                    y = 0
                
                if y_ver > 180:
                    y_ver = 180
                
                # remove current house from the gridmap
                self.neighbourhood[(y_coordinaat-6):(y_coordinaat+16), (x_coordinaat-6):(x_coordinaat+18)] = 0

                # check for other house in given range of free space
                try: 
                    if single in self.neighbourhood[y:y_ver, x:x_ver] or bungalow in self.neighbourhood[y:y_ver, x:x_ver] or maison in self.neighbourhood[y:y_ver, x:x_ver]:
                        check = False

                    # when no house is found, recalculate total price and add one extra meter of free space
                    else:
                        self.total_maison = self.total_maison + self.percentage_maison
                        distance += 1

                # check for IndexError to be sure a coordinate does not go out of range
                except IndexError:
                    if single in self.neighbourhood[y:y_ver, x:x_ver] or bungalow in self.neighbourhood[y:y_ver, x:x_ver] or maison in self.neighbourhood[y:y_ver, x:x_ver]:
                        check = False
                    else:
                        self.total_maison = self.total_maison + self.percentage_maison
                        distance += 1

            # redraw house on the gridmap
            self.neighbourhood[(y_coordinaat - 6):(y_coordinaat + 16),(x_coordinaat - 6):(x_coordinaat + 18)] = 5
            self.neighbourhood[y_coordinaat:(y_coordinaat + 10),x_coordinaat:(x_coordinaat + 12)] = 3
        
        return self.total_maison

    def total(self, coordinaten_maison, coordinaten_bungalow, coordinaten_single):
        
        """ The total price of the whole neighbourhood is calculated. 
        This is done by adding up each housing type's total price.
        Each housing type their method is called. """

        omzet_single = self.single_cost(coordinaten_single)
        omzet_bungalow = self.bungalow_cost(coordinaten_bungalow)
        omzet_maison = self.maison_cost(coordinaten_maison)
       
        total_price = omzet_single + omzet_bungalow + omzet_maison

        return total_price


class Move(): 

    def __init__(self, neighbourhood, neighbourhood_type, houses):

        self.index_free_space = 5
        self.index_water = 4
        self.index_maison = 3 
        self.index_bungalow = 2
        self.index_single = 1
        self.neighbourhood_type = neighbourhood_type
        self.neighbourhood = neighbourhood
        self.houses = houses
        self.amount_single = int(houses * 0.6)
        self.amount_maison = int(houses * 0.15)
        self.amount_bungalow = int(houses * 0.25)

        self.place = Placing(self.neighbourhood, self.houses, self.neighbourhood_type)
    
    def possible_move(self, x, y, x_len, y_len, free_space):
    
        """ For every possible move of a house, the move should be checked whether it is a valid move.
        A single move should meet a certain set of requirements which are presented in the if-statements.
        For every single move, the 'moved' coordinates are given as input and these coordinates are checked.
        When a move is seen as valid, this method will return true. """ 

        # check for water
        if self.index_water in self.neighbourhood[y:(y+y_len),x:(x+x_len)]:
           return False
        
        # check for other house
        elif self.index_single in self.neighbourhood[(y-free_space):(y+y_len+free_space),(x-free_space):(x+x_len+free_space)] or self.index_bungalow in self.neighbourhood[(y-free_space):(y+y_len+free_space),(x-free_space):(x+x_len+free_space)] or self.index_maison in self.neighbourhood[(y-free_space):(y+y_len+free_space),(x-free_space):(x+x_len+free_space)]:
            return False

        # check for obligatory free space of other houses
        elif self.index_free_space in self.neighbourhood[y:(y+y_len),x:(x+x_len)]:
           return False
        
        # check for neighbourhood borders
        elif x+x_len+free_space > 160 or x-free_space<0:
            return False
        
        elif y+y_len+free_space>180 or y-free_space<0:
            return False

        else:
            return True
        
    def move_maison(self, coordinaten_maison, coordinaten_bungalow, coordinaten_single):

        self.coordinaten_maison = coordinaten_maison
        self.coordinaten_bungalow = coordinaten_bungalow
        self.coordinaten_single = coordinaten_single

        price = Price(self.neighbourhood, self.amount_single, self.amount_bungalow, self.amount_maison)

        # set counter for indexation within coordinates lists
        counter = 0 

        # check for every maison the best possible move
        for coordinates in coordinaten_maison:
            
            # set default empty lists. 'list' and 'move_price' respectively store the coordinates and price of each move in a certain direction.
            list = []
            move_price = []

            # save coordinate and price of initial situation
            list.append(coordinates)

            new = price.total(coordinaten_maison, coordinaten_bungalow, coordinaten_single)
            move_price.append(new)

            # top left coordinates
            x = (coordinates[0] - 1)
            y = (coordinates[1] - 1)

            # remove current house from the gridmap, and place water when obligatory free space of house is in water
            self.neighbourhood[coordinates[1]-6:(coordinates[1]+16), coordinates[0]-6:(coordinates[0]+18)] = 0
            self.place.place_water()

            # check for valid move with given coordinates (x,y), maison length (12,10) and obligatory free space (6) as input
            if self.possible_move(x, y, 12, 10, 6) == True:

                # save top left coordinates
                linksboven = [x,y]
                list.append(linksboven)
                coordinaten_maison[counter] = linksboven
                
                # save top left price
                new = price.total(coordinaten_maison, coordinaten_bungalow, coordinaten_single)
                move_price.append(new)

                # remove moved house from the gridmap, and place water when obligatory free space of house is in water
                self.neighbourhood[y-6:y+16, x-6:x+18] = 0
                self.place.place_water()

            # add zeroes to coordinates and prices list to ensure the length of the lists remain equal
            else:
                list.append([0,0])
                move_price.append(0.00)

            # top coordinates
            x = (coordinates[0])
            y = (coordinates[1] - 1)
            
            # check for valid move with given coordinates (x,y), maison length (12,10) and obligatory free space (6) as input
            if self.possible_move(x, y, 12, 10, 6) == True:
                
                # save top coordinates
                top = [x,y]
                list.append(top)
                coordinaten_maison[counter] = top
                
                # save top price
                new = price.total(coordinaten_maison, coordinaten_bungalow, coordinaten_single)
                move_price.append(new)

                # remove moved house from the gridmap, and place water when obligatory free space of house is in water
                self.neighbourhood[y-6:y+16, x-6:x+18] = 0
                self.place.place_water()

            # add zeroes to coordinates and prices list to ensure the length of the lists remain equal
            else:
                list.append([0,0])
                move_price.append(0.00)
            
            # top right coordinates
            x = coordinates[0] + 1
            y = coordinates[1] - 1

            # check for valid move with given coordinates (x,y), maison length (12,10) and obligatory free space (6) as input
            if self.possible_move(x, y, 12, 10, 6) == True:

                # save top right coordinates
                top_right = [x,y]
                list.append(top_right)
                coordinaten_maison[counter] = top_right
                
                # save top right price
                new = price.total(coordinaten_maison, coordinaten_bungalow, coordinaten_single)
                move_price.append(new)

                # remove moved house from the gridmap, and place water when obligatory free space of house is in water
                self.neighbourhood[y-6:y+16, x-6:x+18] = 0
                self.place.place_water()

            # add zeroes to coordinates and prices list to ensure the length of the lists remain equal
            else:
                list.append([0,0])
                move_price.append(0.00)

            # right coordinates
            x = coordinates[0] + 1
            y = coordinates[1]

            # check for valid move with given coordinates (x,y), maison length (12,10) and obligatory free space (6) as input
            if self.possible_move(x, y, 12, 10, 6) == True:
            
                # save right coordinates
                right = [x,y]
                list.append(right)
                coordinaten_maison[counter] = right
                
                # save right price
                new = price.total(coordinaten_maison, coordinaten_bungalow, coordinaten_single)
                move_price.append(new)

                # remove moved house from the gridmap, and place water when obligatory free space of house is in water
                self.neighbourhood[y-6:y+16, x-6:x+18] = 0
                self.place.place_water()

            # add zeroes to coordinates and prices list to ensure the length of the lists remain equal
            else:
                list.append([0,0])
                move_price.append(0.00)
            
            # bottom right coordinates
            x = coordinates[0] + 1
            y = coordinates[1] + 1

            # check for valid move with given coordinates (x,y), maison length (12,10) and obligatory free space (6) as input
            if self.possible_move(x, y, 12, 10, 6) == True:
                
                # save bottom right coordinates
                bottom_right = [x,y]
                list.append(bottom_right)
                coordinaten_maison[counter] = bottom_right
                
                # save bottom right price
                new = price.total(coordinaten_maison, coordinaten_bungalow, coordinaten_single)
                move_price.append(new)

                # remove moved house from the gridmap, and place water when obligatory free space of house is in water
                self.neighbourhood[y-6:y+16, x-6:x+18] = 0
                self.place.place_water()

            # add zeroes to coordinates and prices list to ensure the length of the lists remain equal
            else:
                list.append([0,0])
                move_price.append(0.00)
        
            # bottom coordinates
            x = coordinates[0] 
            y = coordinates[1] + 1

            # check for valid move with given coordinates (x,y), maison length (12,10) and obligatory free space (6) as input
            if self.possible_move(x, y, 12, 10, 6) == True:
                
                # save bottom coordinates
                bottom = [x,y]
                list.append(bottom)
                coordinaten_maison[counter] = bottom
                
                # save bottom price
                new = price.total(coordinaten_maison, coordinaten_bungalow, coordinaten_single)
                move_price.append(new)

                # remove moved house from the gridmap, and place water when obligatory free space of house is in water
                self.neighbourhood[y-6:y+16, x-6:x+18] = 0
                self.place.place_water()

            # add zeroes to coordinates and prices list to ensure the length of the lists remain equal
            else:
                list.append([0,0])
                move_price.append(0.00)
            
            # bottom left coordinates
            x = coordinates[0] - 1
            y = coordinates[1] + 1

            # check for valid move with given coordinates (x,y), maison length (12,10) and obligatory free space (6) as input
            if self.possible_move(x, y, 12, 10, 6) == True:
                
                # save bottom left coordinates
                bottom_left = [x,y]
                list.append(bottom_left)
                coordinaten_maison[counter] = bottom_left

                # save bottom left price
                new = price.total(coordinaten_maison, coordinaten_bungalow, coordinaten_single)
                move_price.append(new)

                # remove moved house from the gridmap, and place water when obligatory free space of house is in water
                self.neighbourhood[y-6:y+16, x-6:x+18] = 0
                self.place.place_water()

            # add zeroes to coordinates and prices list to ensure the length of the lists remain equal
            else:
                list.append([0,0])
                move_price.append(0.00)     

            # left coordinates
            x = coordinates[0] - 1
            y = coordinates[1]
            
            # check for valid move with given coordinates (x,y), maison length (12,10) and obligatory free space (6) as input
            if self.possible_move(x, y, 12, 10, 6) == True:
                
                # save left coordinates
                left = [x,y]
                list.append(left)
                coordinaten_maison[counter] = left
                
                # save left price
                new = price.total(coordinaten_maison, coordinaten_bungalow, coordinaten_single)
                move_price.append(new)

                # remove moved house from the gridmap, and place water when obligatory free space of house is in water
                self.neighbourhood[y-6:y+16, x-6:x+18] = 0
                self.place.place_water()
            
            # add zeroes to coordinates and prices list to ensure the length of the lists remain equal
            else:
                list.append([0,0])
                move_price.append(0.00) 
            
            # obtain the best move with highest price
            hoogste = max(move_price)
            index = move_price.index(hoogste)
            best_coor = list[index]

            y = best_coor[1]
            x = best_coor[0]
            
            # draw move on the map
            self.neighbourhood[(y - 6):(y + 16),(x - 6):(x + 18)] = 5
            self.neighbourhood[y:(y + 10),x:(x + 12)] = 3

            # change moved coordinates
            coordinaten_maison[counter] = best_coor
            counter += 1
    
        return coordinaten_maison          

    def move_single(self, coordinaten_maison, coordinaten_bungalow, coordinaten_single):
        self.coordinaten_maison = coordinaten_maison
        self.coordinaten_bungalow = coordinaten_bungalow
        self.coordinaten_single = coordinaten_single

        price = Price(self.neighbourhood, self.amount_single, self.amount_bungalow, self.amount_maison)

        # set counter for indexation within coordinates lists
        counter = 0

        # check for every single family home the best possible move
        for coordinates in coordinaten_single:
            
            # set default empty lists. 'list' and 'move_price' respectively store the coordinates and price of each move in a certain direction.
            list = []
            move_price = []

            # save coordinate and price of initial situation
            list.append(coordinates)
            new = price.total(coordinaten_maison, coordinaten_bungalow, coordinaten_single)
            move_price.append(new)

            # remove current house from the gridmap, and place water when obligatory free space of house is in water
            self.neighbourhood[coordinates[1]-2:(coordinates[1]+10) , coordinates[0]-2:(coordinates[0]+10)] = 0
            self.place.place_water()

            # top left coordinates
            x = (coordinates[0] - 1)
            y = (coordinates[1] - 1)

            # check for valid move with given coordinates (x,y), single family house length (8,8) and obligatory free space (2) as input
            if self.possible_move(x,y,8,8,2) == True:
                
                # save top left coordinates
                linksboven = [x,y]
                list.append(linksboven)
                coordinaten_single[counter] = linksboven
                
                # save top left price
                new = price.total(coordinaten_maison, coordinaten_bungalow, coordinaten_single)
                move_price.append(new)

                # remove moved house from the gridmap, and place water when obligatory free space of house is in water
                self.neighbourhood[y-2:y+10, x-2:x+10] = 0
                self.place.place_water()

            # add zeroes to coordinates and prices list to ensure the length of the lists remain equal
            else:
                list.append([0,0])
                move_price.append(0.00)

            # top coordinates
            x = (coordinates[0])
            y = (coordinates[1] - 1)
            
            # check for valid move with given coordinates (x,y), single family house length (8,8) and obligatory free space (2) as input
            if self.possible_move(x,y,8,8,2) == True:
                
                # save top coordinates
                top = [x,y]
                list.append(top)
                coordinaten_single[counter] = top

                # save top price
                new = price.total(coordinaten_maison, coordinaten_bungalow, coordinaten_single)
                move_price.append(new)

                # remove moved house from the gridmap, and place water when obligatory free space of house is in water                
                self.neighbourhood[y-2:y+10, x-2:x+10] = 0
                self.place.place_water()

            # add zeroes to coordinates and prices list to ensure the length of the lists remain equal            
            else:
                list.append([0,0])
                move_price.append(0.00)
        
            # top right coordinates
            x = coordinates[0] + 1
            y = coordinates[1] - 1

            # check for valid move with given coordinates (x,y), single family house length (8,8) and obligatory free space (2) as input
            if self.possible_move(x,y,8,8,2) == True:
                
                # save top right coordinates
                top_right = [x,y]
                list.append(top_right)
                coordinaten_single[counter] = top_right

                # save top right price
                new = price.total(coordinaten_maison, coordinaten_bungalow, coordinaten_single)
                move_price.append(new)

                # remove moved house from the gridmap, and place water when obligatory free space of house is in water                
                self.neighbourhood[y-2:y+10, x-2:x+10] = 0
                self.place.place_water()

            # add zeroes to coordinates and prices list to ensure the length of the lists remain equal            
            else:
                list.append([0,0])
                move_price.append(0.00)

            # right coordinates
            x = coordinates[0] + 1
            y = coordinates[1]

            # check for valid move with given coordinates (x,y), single family house length (8,8) and obligatory free space (2) as input
            if self.possible_move(x,y,8,8,2) == True:
                
                # save right coordinates
                right = [x,y]
                list.append(right)
                coordinaten_single[counter] = right

                # save right price
                new = price.total(coordinaten_maison, coordinaten_bungalow, coordinaten_single)
                move_price.append(new)

                # remove moved house from the gridmap, and place water when obligatory free space of house is in water
                self.neighbourhood[y-2:y+10, x-2:x+10] = 0
                self.place.place_water()
            
            # add zeroes to coordinates and prices list to ensure the length of the lists remain equal
            else:
                list.append([0,0])
                move_price.append(0.00)

            # bottom right coordinates
            x = coordinates[0] + 1
            y = coordinates[1] + 1

            # check for valid move with given coordinates (x,y), single family house length (8,8) and obligatory free space (2) as input
            if self.possible_move(x,y,8,8,2) == True:
                
                # save bottom right coordinates
                bottom_right = [x,y]
                list.append(bottom_right)
                coordinaten_single[counter] = bottom_right

                # save bottom right price
                new = price.total(coordinaten_maison, coordinaten_bungalow, coordinaten_single)
                move_price.append(new)

                # remove moved house from the gridmap, and place water when obligatory free space of house is in water
                self.neighbourhood[y-2:y+10, x-2:x+10] = 0
                self.place.place_water()
            
            # add zeroes to coordinates and prices list to ensure the length of the lists remain equal
            else:
                list.append([0,0])
                move_price.append(0.00)

            # bottom coordinates
            x = coordinates[0] 
            y = coordinates[1] + 1

            # check for valid move with given coordinates (x,y), single family house length (8,8) and obligatory free space (2) as input
            if self.possible_move(x,y,8,8,2) == True:
                
                # save bottom coordinates
                bottom = [x,y]
                list.append(bottom)
                coordinaten_single[counter] = bottom

                # save bottom price
                new = price.total(coordinaten_maison, coordinaten_bungalow, coordinaten_single)
                move_price.append(new)

                # remove moved house from the gridmap, and place water when obligatory free space of house is in water
                self.neighbourhood[y-2:y+10, x-2:x+10] = 0
                self.place.place_water()

            # add zeroes to coordinates and prices list to ensure the length of the lists remain equal
            else:
                list.append([0,0])
                move_price.append(0.00)

            # bottom left coordinates
            x = coordinates[0] - 1
            y = coordinates[1] + 1

            # check for valid move with given coordinates (x,y), single family house length (8,8) and obligatory free space (2) as input
            if self.possible_move(x,y,8,8,2) == True:
                
                # save bottom left coordinates
                bottom_left = [x,y]
                list.append(bottom_left)
                coordinaten_single[counter] = bottom_left

                # save bottom left price
                new = price.total(coordinaten_maison, coordinaten_bungalow, coordinaten_single)
                move_price.append(new)

                # remove moved house from the gridmap, and place water when obligatory free space of house is in water
                self.neighbourhood[y-2:y+10, x-2:x+10] = 0
                self.place.place_water()

            # add zeroes to coordinates and prices list to ensure the length of the lists remain equal
            else:
                list.append([0,0])
                move_price.append(0.00)

            # left coordinates
            x = coordinates[0] - 1
            y = coordinates[1]
            
            # check for valid move with given coordinates (x,y), single family house length (8,8) and obligatory free space (2) as input
            if self.possible_move(x,y,8,8,2) == True:

                # save left coordinates
                left = [x,y]
                list.append(left)
                coordinaten_single[counter] = left

                # save left price
                new = price.total(coordinaten_maison, coordinaten_bungalow, coordinaten_single)
                move_price.append(new)

                # remove moved house from the gridmap, and place water when obligatory free space of house is in water
                self.neighbourhood[y-2:y+10, x-2:x+10] = 0
                self.place.place_water()
            
            # add zeroes to coordinates and prices list to ensure the length of the lists remain equal
            else:
                list.append([0,0])
                move_price.append(0.00)

            # obtain the best move with highest price
            hoogste = max(move_price)
            index = move_price.index(hoogste)
            best_coor = list[index]

            y = best_coor[1]
            x = best_coor[0]

            # draw move on the map
            self.neighbourhood[(y - 2):(y + 10),(x - 2):(x + 10)] = 5
            self.neighbourhood[y:(y + 8),x:(x + 8)] = 1
            
            # change moved coordinates
            coordinaten_single[counter] = best_coor
            counter += 1          

    def move_bungalow(self, coordinaten_maison, coordinaten_bungalow, coordinaten_single):
        self.coordinaten_maison = coordinaten_maison
        self.coordinaten_bungalow = coordinaten_bungalow
        self.coordinaten_single = coordinaten_single

        price = Price(self.neighbourhood, self.amount_single, self.amount_bungalow, self.amount_maison)
        
        # set counter for indexation within coordinates lists
        counter = 0 

        # check for every single family home the best possible move
        for coordinates in coordinaten_bungalow:
            
            # set default empty lists. 'list' and 'move_price' respectively store the coordinates and price of each move in a certain direction.
            list = []
            move_price = []
            
            # save coordinate and price of initial situation
            list.append(coordinates)
            new = price.total(coordinaten_maison, coordinaten_bungalow, coordinaten_single)
            move_price.append(new)

            # remove current house from the gridmap, and place water when obligatory free space of house is in water
            self.neighbourhood[coordinates[1]-3:(coordinates[1]+10), coordinates[0]-3:(coordinates[0]+14)] = 0
            self.place.place_water()
            
            # top left coordinates
            x = (coordinates[0] - 1)
            y = (coordinates[1] - 1)
            
            # check for valid move with given coordinates (x,y), bungalow length (11,7) and obligatory free space (3) as input
            if self.possible_move(x, y, 11, 7, 3) == True:
                
                # save top left coordinates
                linksboven = [x,y]
                list.append(linksboven)
                coordinaten_bungalow[counter] = linksboven
                
                # save top left price
                new = price.total(coordinaten_maison, coordinaten_bungalow, coordinaten_single)
                move_price.append(new)

                # remove moved house from the gridmap, and place water when obligatory free space of house is in water
                self.neighbourhood[y-3:y+10, x-3:x+14] = 0
                self.place.place_water()
            
            # add zeroes to coordinates and prices list to ensure the length of the lists remain equal
            else:
                list.append([0,0])
                move_price.append(0.00)
            
            # top coordinates
            x = (coordinates[0])
            y = (coordinates[1] - 1)
            
            # check for valid move with given coordinates (x,y), bungalow length (11,7) and obligatory free space (3) as input
            if self.possible_move(x, y, 11, 7, 3) == True:
                
                # save top coordinates
                top = [x,y]
                list.append(top)
                coordinaten_bungalow[counter] = top

                # save top price
                new = price.total(coordinaten_maison, coordinaten_bungalow, coordinaten_single)
                move_price.append(new)
                
                # remove moved house from the gridmap, and place water when obligatory free space of house is in water
                self.neighbourhood[y-3:y+10, x-3:x+14] = 0
                self.place.place_water()

            # add zeroes to coordinates and prices list to ensure the length of the lists remain equal
            else:
                list.append([0,0])
                move_price.append(0.00)

            # top right coordinates
            x = coordinates[0] + 1
            y = coordinates[1] - 1

            # check for valid move with given coordinates (x,y), bungalow length (11,7) and obligatory free space (3) as input
            if self.possible_move(x, y, 11, 7, 3) == True:
                
                # save top right coordinates
                top_right = [x,y]
                list.append(top_right)
                coordinaten_bungalow[counter] = top_right

                # save top right price
                new = price.total(coordinaten_maison, coordinaten_bungalow, coordinaten_single)
                move_price.append(new)

                # remove moved house from the gridmap, and place water when obligatory free space of house is in water
                self.neighbourhood[y-3:y+10, x-3:x+14] = 0
                self.place.place_water()
            
            # add zeroes to coordinates and prices list to ensure the length of the lists remain equal
            else:
                list.append([0,0])
                move_price.append(0.00)

            # right coordinates
            x = coordinates[0] + 1
            y = coordinates[1]

            # check for valid move with given coordinates (x,y), bungalow length (11,7) and obligatory free space (3) as input
            if self.possible_move(x, y, 11, 7, 3) == True:
                
                # save right coordinates
                right = [x,y]
                list.append(right)
                coordinaten_bungalow[counter] = right

                # save right price
                new = price.total(coordinaten_maison, coordinaten_bungalow, coordinaten_single)
                move_price.append(new)

                # remove moved house from the gridmap, and place water when obligatory free space of house is in water
                self.neighbourhood[y-3:y+10, x-3:x+14] = 0
                self.place.place_water()

            # add zeroes to coordinates and prices list to ensure the length of the lists remain equal
            else:
                list.append([0,0])
                move_price.append(0.00)

            # bottom right coordinates
            x = coordinates[0] + 1
            y = coordinates[1] + 1

            # check for valid move with given coordinates (x,y), bungalow length (11,7) and obligatory free space (3) as input
            if self.possible_move(x, y, 11, 7, 3) == True:
                
                # save bottom right coordinates
                bottom_right = [x,y]
                list.append(bottom_right)
                coordinaten_bungalow[counter] = bottom_right

                # save bottom right price
                new = price.total(coordinaten_maison, coordinaten_bungalow, coordinaten_single)
                move_price.append(new)

                # remove moved house from the gridmap, and place water when obligatory free space of house is in water
                self.neighbourhood[y-3:y+10, x-3:x+14] = 0
                self.place.place_water()

            # add zeroes to coordinates and prices list to ensure the length of the lists remain equal
            else:
                list.append([0,0])
                move_price.append(0.00)

            # bottom coordinates
            x = coordinates[0] 
            y = coordinates[1] + 1
            
            # check for valid move with given coordinates (x,y), bungalow length (11,7) and obligatory free space (3) as input
            if self.possible_move(x, y, 11, 7, 3) == True:
                
                # save bottom coordinates
                bottom = [x,y]
                list.append(bottom)
                coordinaten_bungalow[counter] = bottom

                # save bottom price
                new = price.total(coordinaten_maison, coordinaten_bungalow, coordinaten_single)
                move_price.append(new)
                
                # remove moved house from the gridmap, and place water when obligatory free space of house is in water
                self.neighbourhood[y-3:y+10, x-3:x+14] = 0
                self.place.place_water()
            
            # add zeroes to coordinates and prices list to ensure the length of the lists remain equal
            else:
                list.append([0,0])
                move_price.append(0.00)

            # bottom left coordinates
            x = coordinates[0] - 1
            y = coordinates[1] + 1

            # check for valid move with given coordinates (x,y), bungalow length (11,7) and obligatory free space (3) as input
            if self.possible_move(x, y, 11, 7, 3) == True:
                
                # save bottom left coordinates
                bottom_left = [x,y]
                list.append(bottom_left)
                coordinaten_bungalow[counter] = bottom_left

                # save bottom left price
                new = price.total(coordinaten_maison, coordinaten_bungalow, coordinaten_single)
                move_price.append(new)

                # remove moved house from the gridmap, and place water when obligatory free space of house is in water
                self.neighbourhood[y-3:y+10, x-3:x+14] = 0
                self.place.place_water()

            # add zeroes to coordinates and prices list to ensure the length of the lists remain equal
            else:
                list.append([0,0])
                move_price.append(0.00)

            # left coordinates
            x = coordinates[0] - 1
            y = coordinates[1]
            
            # check for valid move with given coordinates (x,y), bungalow length (11,7) and obligatory free space (3) as input
            if self.possible_move(x, y, 11, 7, 3) == True:
                
                # save left coordinates
                left = [x,y]
                list.append(left)
                coordinaten_bungalow[counter] = left

                # save left coordinates
                new = price.total(coordinaten_maison, coordinaten_bungalow, coordinaten_single)
                move_price.append(new)

                # remove moved house from the gridmap, and place water when obligatory free space of house is in water
                self.neighbourhood[y-3:y+10, x-3:x+14] = 0
                self.place.place_water()
            
            # add zeroes to coordinates and prices list to ensure the length of the lists remain equal
            else:
                list.append([0,0])
                move_price.append(0.00)

            # obtain the best move with highest price
            hoogste = max(move_price)
            index = move_price.index(hoogste)
            best_coor = list[index]
            
            y = best_coor[1]
            x = best_coor[0]
            
            # draw move on the map
            self.neighbourhood[(y - 3):(y + 10),(x - 3):(x + 14)] = 5
            self.neighbourhood[y:(y + 7),x:(x + 11)] = 2

            # change moved coordinates
            coordinaten_bungalow[counter] = best_coor
            counter += 1


def main():
    
    # settings
    neighbourhood_type = 2
    houses = 20
    runs = 100

    # initialize variables
    amount_single = int(houses * 0.6)
    amount_bungalow = int(houses * 0.25)
    amount_maison = int(houses * 0.15)
    highest_price_move = 0
    total_prices = []
    total_prices_move = []

    for i in range(runs):
        print("Run", (i+1))

        # create a 160 x 180 gridmap
        x, y = (160, 180) 
        neighbourhood = [[0 for i in range(x)] for j in range(y)]
        neighbourhood = np.array(neighbourhood)

        # adding houses
        price = Price(neighbourhood, amount_single, amount_bungalow, amount_maison)
        place = Placing(neighbourhood, houses, neighbourhood_type)
        move = Move(neighbourhood, neighbourhood_type, houses)

        # create the different water values of the gridmap
        place.place_water()

        coordinaten_single = place.place_single()
        coordinaten_maison = place.place_maison(coordinaten_single)
        coordinaten_bungalow = place.place_bungalow(coordinaten_single, coordinaten_maison)

        total_price = price.total(coordinaten_maison, coordinaten_bungalow, coordinaten_single)
        total_prices.append(total_price)

        # save current neighbourhood with the highest price
        if total_price >= max(total_prices):
            neighbourhood_max = neighbourhood
            print(max(total_prices))

        # perform move for first time
        move.move_maison(coordinaten_maison, coordinaten_bungalow, coordinaten_single)
        move.move_single(coordinaten_maison, coordinaten_bungalow, coordinaten_single)
        move.move_bungalow(coordinaten_maison, coordinaten_bungalow, coordinaten_single)

        # intialize variables before while loop
        new_move = price.total(coordinaten_maison, coordinaten_bungalow, coordinaten_single)
        oud_move = total_price
        counter = 1

        # move until no move is possible
        while new_move > oud_move:
            counter += 1
            move.move_single(coordinaten_maison, coordinaten_bungalow, coordinaten_single)
            move.move_maison(coordinaten_maison, coordinaten_bungalow, coordinaten_single)
            move.move_bungalow(coordinaten_maison, coordinaten_bungalow, coordinaten_single)
            
            # new values
            oud_move = new_move
            new_move = price.total(coordinaten_maison, coordinaten_bungalow, coordinaten_single)
        
        # save price after move
        price_move = price.total(coordinaten_maison, coordinaten_bungalow, coordinaten_single)
        total_prices_move.append(price_move)

        # save highest price after move
        if price_move >= highest_price_move:
            highest_price_move = price_move
            neighbourhood_move = neighbourhood

    # calculate and show statistics
    mean = statistics.mean(total_prices_move)
    print()
    print("Wijk", neighbourhood_type, ":", runs, "runs")
    print("Mean:", mean)
    print("Max:", highest_price_move)
    print()

    # create visualization
    H = np.array(neighbourhood_move)
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
    plt.title("Wijk " + str(neighbourhood_type) + " | " + str(houses) + " houses | " + str(runs) + " runs | " + str(max(total_prices)) + " €")
    plt.axis('off')

    # create legend for visualization
    sing = mpatches.Patch(color=colors[1], label="Single")
    bung = mpatches.Patch(color=colors[2], label="Bungalow")
    mais = mpatches.Patch(color=colors[3], label="Maison")
    wat = mpatches.Patch(color=colors[4], label="Water")
    extr = mpatches.Patch(color=colors[5], label="Free space")
    plt.legend(handles=[wat,sing,bung,mais,extr], bbox_to_anchor=(1.01, 0.5), loc='center left')

    # create boxplot
    fig, ax1 = plt.subplots()
    ax1.boxplot(total_prices)
    ax1.yaxis.grid(True, linestyle='-', which='major', color='lightgrey', alpha=0.5)
    plt.title("Boxplot Wijk " + str(neighbourhood_type))
    ax1.set_ylabel("Price")
    plt.xticks([1], ["Wijk" + str(neighbourhood_type)])
    plt.show()

    # saving in csv file
    with open("output_move.csv","w+") as my_csv:
        csvWriter = csv.writer(my_csv,delimiter=',')
        csvWriter.writerows(neighbourhood_move)


if __name__ == '__main__':
    main()