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

    def __init__(self, neighbourhood, houses, neighbourhood_type, random_range):
        
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
        self.random_range = random_range

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
            
            # set default value for the highest price of a placed house
            highest_price = 0

            # amount of times a random coordinate is placed checked for a house
            for j in range(0,self.random_range):

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

                # excluding the first house placement, check the price of the given coordinates
                if i == 0:
                    highest_price_coor = [x,y]
                    break

                # new coordinates are saved in coordinates list
                new_coor = [x,y]
                single_coordinatenlijst[i] = new_coor

                # house is drawn in neighbourhood before checking the price.
                self.neighbourhood[(y - 2):(y + 10),(x - 2):(x + 10)] = 5
                self.neighbourhood[y:(y + 8),x:(x + 8)] = 1

                # calculate price of current neighborhood with the new house
                price = Price(self.neighbourhood, self.amount_single, self.amount_bungalow, self.amount_maison)
                new_price = price.single_cost(single_coordinatenlijst)

                # redraw neighbourhood so that new house is removed from neighbourhood and water is placed again
                self.neighbourhood[(y - 2):(y + 10),(x - 2):(x + 10)] = 0
                self.place_water()

                # save current highest price and coordinates
                if new_price > highest_price:
                    highest_price = new_price
                    highest_price_coor = new_coor

            # fill empty coordinates with coordinates of other house
            for b in range(0,len(single_coordinatenlijst)):
                if single_coordinatenlijst[b] == [0,0]:
                    single_coordinatenlijst[b] = highest_price_coor

            # save coordinates in coordinates list
            single_coordinatenlijst[i] = highest_price_coor

            # draw every house on the gridmap
            for coor in single_coordinatenlijst:
                y = coor[1]
                x = coor[0]
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

            # set default value for the highest price of a placed house
            highest_price = 0
            
            # amount of times a random coordinate is placed and checked for a house
            for j in range(0,self.random_range):

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
                    
                # excluding the first house placement, check the price of the given coordinates
                if i == 0:
                    highest_price_coor = [x,y]
                    break

                # new coordinates are saved in coordinates list
                new_coor = [x,y]
                maison_coordinatenlijst[i] = new_coor

                # house is drawn in neighbourhood before checking the price.
                self.neighbourhood[(y - 6):(y + 16),(x - 6):(x + 18)] = 5
                self.neighbourhood[y:(y + 10),x:(x + 12)] = 3

                # calculate price of current neighborhood with the new house
                price = Price(self.neighbourhood, self.amount_single, self.amount_bungalow, self.amount_maison)
                new_mais = price.maison_cost(maison_coordinatenlijst)
                new_sing = price.single_cost(coordinaten_single)
                new_price = new_mais + new_sing

                # redraw neighbourhood so that new house is removed from neighbourhood and water is placed again
                self.neighbourhood[(y - 6):(y + 16),(x - 6):(x + 18)] = 0
                self.place_water()
        
                # save current highest price and coordinates
                if new_price > highest_price:
                    highest_price = new_price
                    highest_price_coor = new_coor

            # fill empty coordinates with coordinates of other house
            for b in range(0,len(maison_coordinatenlijst)):
                if maison_coordinatenlijst[b] == [0,0]:
                    maison_coordinatenlijst[b] = highest_price_coor

            # save coordinates in coordinates list
            maison_coordinatenlijst[i] = highest_price_coor

            # draw every house on the gridmap
            for coor in maison_coordinatenlijst:
                y = coor[1]
                x = coor[0]
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

            # set default value for the highest price of a placed house
            highest_price = 0

            # amount of times a random coordinate is placed and checked for a house
            for j in range(0,self.random_range):

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

                # excluding the first house placement, check the price of the given coordinates
                if i == 0:
                    highest_price_coor = [x,y]
                    break

                # new coordinates are saved in coordinates list
                new_coor = [x,y]
                bungalow_coordinatenlijst[i] = new_coor

                # house is drawn in neighbourhood before checking the price.
                self.neighbourhood[(y - 3):(y + 10),(x - 3):(x + 14)] = 5
                self.neighbourhood[y:(y + 7),x:(x + 11)] = 2

                # calculate price of current neighborhood with the new house
                price = Price(self.neighbourhood, self.amount_single, self.amount_bungalow, self.amount_maison)
                new_price = price.total(coordinaten_maison, bungalow_coordinatenlijst, coordinaten_single)

                # redraw neighbourhood so that new house is removed from neighbourhood and water is placed again
                self.neighbourhood[(y - 3):(y + 10),(x - 3):(x + 14)] = 0
                self.place_water()

                # save current highest price and coordinates
                if new_price > highest_price:
                    highest_price = new_price
                    highest_price_coor = new_coor

            # fill empty coordinates with coordinates of other house
            for b in range(0,len(bungalow_coordinatenlijst)):
                if bungalow_coordinatenlijst[b] == [0,0]:
                    bungalow_coordinatenlijst[b] = highest_price_coor

            # save coordinates in coordinates list
            bungalow_coordinatenlijst[i] = highest_price_coor

            # draw every house on the gridmap
            for coor in bungalow_coordinatenlijst:
                y = coor[1]
                x = coor[0]
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

def main():
    
    # settings
    neighbourhood_type = 1
    houses = 20
    runs = 10
    random_range = 10

    # initialize variables
    amount_single = int(houses * 0.6)
    amount_bungalow = int(houses * 0.25)
    amount_maison = int(houses * 0.15)
    total_prices = []

    for i in range(runs):
        print("Run", (i+1))

        # create a 160 x 180 gridmap
        x, y = (160, 180) 
        neighbourhood = [[0 for i in range(x)] for j in range(y)]
        neighbourhood = np.array(neighbourhood)

        # adding houses
        price = Price(neighbourhood, amount_single, amount_bungalow, amount_maison)
        place = Placing(neighbourhood, houses, neighbourhood_type, random_range)

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
            
    # calculate and show statistics
    mean = statistics.mean(total_prices)
    median = statistics.median(total_prices)
    print()
    print("Wijk", neighbourhood_type, ":", runs, "runs")
    print("Mean:", mean)
    print("Max:", max(total_prices))
    print()

    # create visualization
    H = np.array(neighbourhood_max)
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
    plt.title("Greedy", fontsize= 20)
    ax1.set_ylabel("Price (€)", fontsize = 15)
    ax1.tick_params(axis = 'y', labelsize = 12)
    plt.xticks([1], ["Greedy"],fontsize= 15)
    bottom = 7000000
    top = 15000000
    ax1.set_ylim(bottom, top)
    props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
    text = "Mean: € " + str(mean) + "\nMedian: € " + str(median) + "\nMax: € " + str(max(total_prices))
    ax1.text(0.05, 0.95, text, transform=ax1.transAxes, fontsize=11,
        verticalalignment='top', bbox=props)
    plt.show()

    # saving in csv file
    with open("output_greedy.csv","w+") as my_csv:
        csvWriter = csv.writer(my_csv,delimiter=',')
        csvWriter.writerows(neighbourhood_max)


if __name__ == '__main__':
    main()