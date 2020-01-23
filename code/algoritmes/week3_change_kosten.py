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
    def __init__(self, wijk, aantal_eensgezins, aantal_maison, aantal_bungalow, wijk_type):
        
        self.wijk = wijk
        self.aantal_eensgezins = aantal_eensgezins
        self.aantal_maison = aantal_maison
        self.aantal_bungalow = aantal_bungalow
        self.wijk_type = wijk_type
        self.index_eengezinswoning = 1
        self.index_bungalow = 2
        self.index_maison = 3 
        self.index_water = 4
        self.index_vrijstand = 5

    def water(self):

        """ This method adds areas of water to the created gridmap. 
         The type of neighbourhood is given as an argument when calling the method.
         The method checks which neighbourhood type is given and creates the water area for that type.
         The area where the water should be generated is changed from an "empty" value to the "water" value. """

        # self.wijk_type = wijk_type

        # if the wijk type given is 1 create the water for wijk 1
        if self.wijk_type == 1:

            # change the values in the selected area from the array to the "water" value
            self.wijk[0:180, 0:32] = 4

        # if the wijk type given is 2 create the water for wijk 2
        if self.wijk_type == 2:

            # change the values in the selected area from the array to the "water" value
            self.wijk[135:180, 0:32] = 4
            self.wijk[0:45, 0:32] = 4
            self.wijk[135:180, 128:160] = 4
            self.wijk[0:45, 128:160] = 4

        # if the wijk type given is 3 create the water for wijk 3
        if self.wijk_type == 3:

            # change the values in the selected area from the array to the "water" value
            self.wijk[50:130, 44:116] = 4

        return self.wijk_type

    def eensgezinswoningen(self, aantal_eensgezins):

        """ This method searches the gridmap for empty areas by creating random coordinates. If the area
         around the randomized coordinate fits this specific type of house, the house is placed and saved
         in the coordinates list. """

        # eensgezins_coordinatenlijst = [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]
        eensgezins_coordinatenlijst = [[0,0]] * 12
        # coordinaten_maison = [[0,0],[0,0],[0,0]]
        coordinaten_maison = [[0,0]] * 3
        # coordinaten_bungalow =[[0,0],[0,0],[0,0],[0,0],[0,0]]
        coordinaten_bungalow = [[0,0]] * 5

        for i in range(0,aantal_eensgezins):
            
            highest_price = 0

            for j in range(0,5):

                x = random.randrange(2,150)
                y = random.randrange(2,170)

                check = True
                while check == True:

                    if self.index_water in self.wijk[y:(y+8),x:(x+8)]:
                        x = random.randrange(2,150)
                        y = random.randrange(2,170)

                    elif self.index_eengezinswoning in self.wijk[(y-2):(y+10),(x-2):(x+10)] or self.index_bungalow in self.wijk[(y-2):(y+10),(x-2):(x+10)] or self.index_maison in self.wijk[(y-2):(y+10),(x-2):(x+10)]:
                        x = random.randrange(2,150)
                        y = random.randrange(2,170)

                    elif self.index_vrijstand in self.wijk[y:(y+8),x:(x+8)]:
                        x = random.randrange(2,150)
                        y = random.randrange(2,170)
                        
                    else:
                        check = False

                if i == 0:
                    highest_price_coor = [x,y]
                    break

                new_coor = [x,y]
                eensgezins_coordinatenlijst[i] = new_coor

                self.wijk[(y - 2):(y + 10),(x - 2):(x + 10)] = 5
                self.wijk[y:(y + 8),x:(x + 8)] = 1

                price = Kosten(self.wijk, 12, 5, 3)
                new_price = price.eengezins_cost(eensgezins_coordinatenlijst, self.aantal_eensgezins)

                self.wijk[(y - 2):(y + 10),(x - 2):(x + 10)] = 0
                self.water()

                if new_price > highest_price:
                    highest_price = new_price
                    highest_price_coor = new_coor

            for b in range(0,len(eensgezins_coordinatenlijst)):
                if eensgezins_coordinatenlijst[b] == [0,0]:
                    eensgezins_coordinatenlijst[b] = highest_price_coor

            eensgezins_coordinatenlijst[i] = highest_price_coor

            for coor in eensgezins_coordinatenlijst:
                y = coor[1]
                x = coor[0]
                self.wijk[(y - 2):(y + 10),(x - 2):(x + 10)] = 5
                self.wijk[y:(y + 8),x:(x + 8)] = 1

        return eensgezins_coordinatenlijst

    def maison(self, aantal_maison, coordinaten_eensgezin):

        """ This method searches the gridmap for empty areas by creating random coordinates. If the area
         around the randomized coordinate fits this specific type of house, the house is placed and saved
         in the coordinates list. """

        # coordinaten_maison = [[0,0],[0,0],[0,0]]
        coordinaten_maison = [[0,0]] * 3
        maison_coordinatenlijst = coordinaten_maison
        # coordinaten_bungalow =[[0,0],[0,0],[0,0],[0,0],[0,0]]
        coordinaten_bungalow = [[0,0]] * 5

        for i in range(0,aantal_maison):

            highest_price = 0
            
            for j in range(0,5):

                x = random.randrange(6,142)
                y = random.randrange(6,164)
                
                check = True
                while check == True:

                    if self.index_water in self.wijk[y:(y+10),x:(x+12)]:
                        x = random.randrange(6,142)
                        y = random.randrange(6,164)

                    elif self.index_eengezinswoning in self.wijk[(y-6):(y+16),(x-6):(x+18)] or self.index_bungalow in self.wijk[(y-6):(y+16),(x-6):(x+18)] or self.index_maison in self.wijk[(y-6):(y+16),(x-6):(x+18)]:
                        x = random.randrange(6,142)
                        y = random.randrange(6,164)

                    elif self.index_vrijstand in self.wijk[y:(y+10),x:(x+12)]:
                        x = random.randrange(6,142)
                        y = random.randrange(6,164)

                    else:
                        check = False
                    
                if i == 0:
                    highest_price_coor = [x,y]
                    break

                new_coor = [x,y]
                maison_coordinatenlijst[i] = new_coor

                self.wijk[(y - 6):(y + 16),(x - 6):(x + 18)] = 5
                self.wijk[y:(y + 10),x:(x + 12)] = 3

                price = Kosten(self.wijk, 12, 5, 3)
                new_mais = price.maison_cost(maison_coordinatenlijst, self.aantal_maison)
                new_eens = price.eengezins_cost(coordinaten_eensgezin, self.aantal_eensgezins)
                new_price = new_mais + new_eens

                self.wijk[(y - 6):(y + 16),(x - 6):(x + 18)] = 0
                self.water()
        
                if new_price > highest_price:
                    highest_price = new_price
                    highest_price_coor = new_coor

            for b in range(0,len(maison_coordinatenlijst)):
                if maison_coordinatenlijst[b] == [0,0]:
                    maison_coordinatenlijst[b] = highest_price_coor

            maison_coordinatenlijst[i] = highest_price_coor

            for coor in maison_coordinatenlijst:
                y = coor[1]
                x = coor[0]
                self.wijk[(y - 6):(y + 16),(x - 6):(x + 18)] = 5
                self.wijk[y:(y + 10),x:(x + 12)] = 3

        return maison_coordinatenlijst

    def bungalow(self, aantal_bungalow, coordinaten_eensgezin, coordinaten_maison):

        """ This method searches the gridmap for empty areas by creating random coordinates. If the area
         around the randomized coordinate fits this specific type of house, the house is placed and saved
         in the coordinates list. """
         
        # create a coordinates list of the houses being placed
        # coordinaten_bungalow =[[0,0],[0,0],[0,0],[0,0],[0,0]]
        coordinaten_bungalow = [[0,0]] * 5
        bungalow_coordinatenlijst = coordinaten_bungalow

        for i in range(0,aantal_bungalow):

            highest_price = 0

            for j in range(0,5):
  
                x = random.randrange(3,146)
                y = random.randrange(3,170)

                check = True
                while check == True:

                    if self.index_water in self.wijk[y:(y+7),x:(x+11)]:
                        x = random.randrange(3,146)
                        y = random.randrange(3,170)

                    elif self.index_eengezinswoning in self.wijk[(y-3):(y+10),(x-3):(x+14)] or self.index_bungalow in self.wijk[(y-3):(y+10),(x-3):(x+14)] or self.index_maison in self.wijk[(y-3):(y+10),(x-3):(x+14)]:
                        x = random.randrange(3,146)
                        y = random.randrange(3,170)

                    elif self.index_vrijstand in self.wijk[y:(y+7),x:(x+11)]:
                        x = random.randrange(3,146)
                        y = random.randrange(3,170)
                    
                    else:
                        check = False

                if i == 0:
                    highest_price_coor = [x,y]
                    break

                new_coor = [x,y]
                bungalow_coordinatenlijst[i] = new_coor

                self.wijk[(y - 3):(y + 10),(x - 3):(x + 14)] = 5
                self.wijk[y:(y + 7),x:(x + 11)] = 2

                price = Kosten(self.wijk, 12, 5, 3)
                new_price = price.total(coordinaten_maison, bungalow_coordinatenlijst, coordinaten_eensgezin)

                self.wijk[(y - 3):(y + 10),(x - 3):(x + 14)] = 0
                self.water()
                # self.wijk[y:(y + 7),x:(x + 11)] = 0

                if new_price > highest_price:
                    highest_price = new_price
                    highest_price_coor = new_coor

            for b in range(0,len(bungalow_coordinatenlijst)):
                if bungalow_coordinatenlijst[b] == [0,0]:
                    bungalow_coordinatenlijst[b] = highest_price_coor

            bungalow_coordinatenlijst[i] = highest_price_coor

            for coor in bungalow_coordinatenlijst:
                y = coor[1]
                x = coor[0]
                self.wijk[(y - 3):(y + 10),(x - 3):(x + 14)] = 5
                self.wijk[y:(y + 7),x:(x + 11)] = 2

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
            eensgezinswoning = 1 
            bungalow = 2 
            maison = 3      
      
            afstand_tot_huis = 3 
            x_coordinaat = coordinates[0]
            y_coordinaat = coordinates[1]
            som = 0 

            check = True
            while check == True:
                x = x_coordinaat - afstand_tot_huis
                x_ver = x_coordinaat + 8 + afstand_tot_huis
                y = y_coordinaat - afstand_tot_huis
                y_ver = y_coordinaat + 8 + afstand_tot_huis

                self.wijk[(y_coordinaat - 2):(y_coordinaat + 10),(x_coordinaat - 2):(x_coordinaat + 10)] = 0
    
                try:
                    if eensgezinswoning in self.wijk[y:y_ver, x:x_ver] or bungalow in self.wijk[y:y_ver, x:x_ver] or maison in self.wijk[y:y_ver, x:x_ver]:
                        check = False
                    else:
                        self.total_eengezins = self.total_eengezins + self.percentage_eengezins
                        afstand_tot_huis += 1
                
                except IndexError:
                    if eensgezinswoning in self.wijk[y:y_ver, x:x_ver] or bungalow in self.wijk[y:y_ver, x:x_ver] or maison in self.wijk[y:y_ver, x:x_ver]:
                        check = False
                    else:
                        self.total_eengezins = self.total_eengezins + self.percentage_eengezins
                        afstand_tot_huis += 1

            self.wijk[(y_coordinaat - 2):(y_coordinaat + 10),(x_coordinaat - 2):(x_coordinaat + 10)] = 5
            self.wijk[y_coordinaat:(y_coordinaat + 8),x_coordinaat:(x_coordinaat + 8)] = 1

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

            eensgezinswoning = 1 
            bungalow = 2 
            maison = 3 
            
            afstand_tot_huis = 4
            x_coordinaat = coordinates[0]
            y_coordinaat = coordinates[1]
            som = 0 
            
            check = True

            while check == True:
                x = x_coordinaat - afstand_tot_huis
                x_ver = x_coordinaat + 11 + afstand_tot_huis
                y = y_coordinaat - afstand_tot_huis
                y_ver = y_coordinaat + 7 + afstand_tot_huis
                
                self.wijk[(y_coordinaat - 3):(y_coordinaat + 10),(x_coordinaat - 3):(x_coordinaat + 14)] = 0

                try: 
                    if eensgezinswoning in self.wijk[y:y_ver, x:x_ver] or bungalow in self.wijk[y:y_ver, x:x_ver] or maison in self.wijk[y:y_ver, x:x_ver]:
                        check = False
                    else:
                        self.total_eengezins = self.total_eengezins + self.percentage_eengezins
                        afstand_tot_huis += 1 
               
                except IndexError:
                    if eensgezinswoning in self.wijk[y:y_ver, x:x_ver] or bungalow in self.wijk[y:y_ver, x:x_ver] or maison in self.wijk[y:y_ver, x:x_ver]:
                        check = False
                    else:
                        self.total_eengezins = self.total_eengezins + self.percentage_eengezins
                        afstand_tot_huis += 1 


            self.wijk[(y_coordinaat - 3):(y_coordinaat + 10),(x_coordinaat - 3):(x_coordinaat + 14)] = 5
            self.wijk[y_coordinaat:(y_coordinaat + 7),x_coordinaat:(x_coordinaat + 11)] = 2

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

            afstand_tot_huis = 7
            x_coordinaat = coordinates[0]
            y_coordinaat = coordinates[1]
            som = 0 
            
            eensgezinswoning = 1 
            bungalow = 2 
            maison = 3 
            
            check = True
            while check == True:
                x = x_coordinaat - afstand_tot_huis
                x_ver = x_coordinaat + 12 + afstand_tot_huis
                y = y_coordinaat - afstand_tot_huis
                y_ver = y_coordinaat + 10 + afstand_tot_huis
                
                self.wijk[(y_coordinaat-6):(y_coordinaat+16), (x_coordinaat-6):(x_coordinaat+18)] = 0

                try: 
                    if eensgezinswoning in self.wijk[y:y_ver, x:x_ver] or bungalow in self.wijk[y:y_ver, x:x_ver] or maison in self.wijk[y:y_ver, x:x_ver]:
                        check = False
                    else:
                        self.total_maison = self.total_maison + self.percentage_maison
                        afstand_tot_huis += 1
                except IndexError:
                    if eensgezinswoning in self.wijk[y:y_ver, x:x_ver] or bungalow in self.wijk[y:y_ver, x:x_ver] or maison in self.wijk[y:y_ver, x:x_ver]:
                        check = False
                    else:
                        self.total_maison = self.total_maison + self.percentage_maison
                        afstand_tot_huis += 1

            self.wijk[(y_coordinaat - 6):(y_coordinaat + 16),(x_coordinaat - 6):(x_coordinaat + 18)] = 5
            self.wijk[y_coordinaat:(y_coordinaat + 10),x_coordinaat:(x_coordinaat + 12)] = 3

        
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
        self.wijk = wijk

        price = Kosten(wijk, 12, 5, 3)
        counter = 0 

        for coordinaten in coordinaten_maison:
            
            lijst = []
            opbrengst = []
            lijst.append(coordinaten)

            new = price.total(coordinaten_maison, coordinaten_bungalow, coordinaten_eensgezin)
            opbrengst.append(new)

            # Linksboven
            self.wijk[(coordinaten[1]-2):(coordinaten[1]+10),(coordinaten[0]-2):(coordinaten[1]+10)] = 0
            x = (coordinaten[0] - 1)
            y = (coordinaten[1] - 1)
            linksboven = [x,y]
            lijst.append(linksboven)

            # Draw
            self.wijk[(y - 6):(y + 16),(x - 6):(x + 18)] = 5
            self.wijk[y:(y + 10),x:(x + 12)] = 3      

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
    runs = 10

    total_prices = []

    for i in range(runs):
        # create a 160 x 180 gridmap
        x, y = (160, 180) 
        wijk = [[0 for i in range(x)] for j in range(y)]
        wijk = np.array(wijk) 

        # adding houses
        price = Kosten(wijk, 12, 5, 3)
        place = Placing(wijk, 12, 5, 3, wijk_type)
        # move = Move()
        move = Move(wijk, wijk_type)

        # create the different water values of the gridmap
        place.water()

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

        totaal = price.total(coordinaten_maison, coordinaten_bungalow, coordinaten_eensgezin)
        total_prices.append(totaal)

        # save current wijk with the highest price
        highest_price_move = 0
        if totaal >= max(total_prices):
            wijk_max = wijk
            print(max(total_prices))
            # for i in range(0,3):
            #     move.move_maison(coordinaten_maison, coordinaten_bungalow, coordinaten_eensgezin, wijk)
            #     move.move_eensgezin(coordinaten_maison, coordinaten_bungalow, coordinaten_eensgezin, wijk)
            #     move.move_bungalow(coordinaten_maison, coordinaten_bungalow, coordinaten_eensgezin, wijk)
            price_move = price.total(coordinaten_maison, coordinaten_bungalow, coordinaten_eensgezin)
            if price_move >= highest_price_move:
                highest_price_move = price_move


    # calculate and show statistics
    mean = statistics.mean(total_prices)
    print()
    print("Wijk", wijk_type, ":", runs, "runs")
    print("Mean:", mean)
    print("Max:", max(total_prices))
    print("Max with move:", highest_price_move)
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
    # ax1.set_ylim(bottom, top)
    plt.show()

    # saving in csv file
    with open("wijk1.csv","w+") as my_csv:
        csvWriter = csv.writer(my_csv,delimiter=',')
        csvWriter.writerows(wijk_max)


if __name__ == '__main__':
    main()