class Price:

    def __init__(self):

        pass
    
    def housing_costs(self, eengezins, bungalow, maison):

        """Prijs bepalen code"""

        # # create a test array
        # test_array = [
        #     ["G", "G", "G", "G", "G", "G", "G", "G", "H", "G", "G", "G", "G", "G"],
        #     ["G", "G", "G", "G", "G", "G", "G", "G", "G", "G", "G", "G", "G", "G"],
        #     ["G", "G", "G", "G", "G", "G", "G", "G", "G", "G", "G", "G", "G", "G"],
        #     ["G", "G", "G", "G", "G", "G", "G", "G", "G", "G", "G", "G", "G", "G"],
        #     ["G", "G", "G", "G", "G", "H", "H", "H", "H", "G", "G", "G", "G", "G"],
        #     ["G", "G", "G", "G", "G", "H", "H", "H", "H", "G", "G", "G", "G", "G"],
        #     ["G", "G", "G", "G", "G", "H", "H", "H", "H", "G", "G", "G", "G", "G"],
        #     ["G", "G", "G", "G", "G", "H", "H", "H", "H", "G", "G", "G", "G", "G"],
        #     ["G", "G", "G", "G", "G", "G", "G", "G", "G", "G", "G", "G", "G", "G"],
        #     ["G", "G", "G", "G", "G", "G", "G", "G", "G", "G", "G", "G", "G", "G"],
        #     ["G", "G", "G", "G", "G", "G", "G", "G", "G", "G", "G", "G", "G", "G"],
        #     ["G", "G", "G", "G", "G", "G", "G", "G", "G", "G", "G", "G", "G", "G"],
        #     ["G", "G", "G", "G", "G", "G", "G", "G", "G", "G", "G", "G", "G", "G"],
        #     ["G", "G", "G", "G", "G", "G", "G", "G", "G", "G", "G", "G", "G", "G"],
        #     ["G", "G", "G", "G", "G", "G", "G", "G", "G", "G", "G", "G", "G", "G"],
        # ]
        
        # make default prices of houses
        self.eengezins = 285000
        self.bungalow = 399000
        self.maison = 610000

        # calcualte percentage of extra housing worth per extra sqaure meter space
        self.percentage_eengezins = self.eengezins * 0.03
        self.percentage_bungalow = self.bungalow * 0.04
        self.percentage_maison = self.percentage_maison * 0.06

        # make default total prices
        self.total_eengezins = eengezins * self.eengezins
        self.total_bungalow = bungalow * self.bungalow
        self.total_maison = maison * self.maison

        # Search for places where house stands
        
        # counter = 0
        # for i in range(len(test_array)):
        #     for j in range(len(test_array[i])):
        #         if test_array[i][j] == "H":


                    # # create coordinates of place where part of house is located
                    # x = 
                    # y =

                    
                    # for j in wijk1
                    # # check whether there is any extra ground
                    # if wijk1[x - 3][y] == "G" or "W" or None:
                
                    # counter += 1

        # locate 8 base points on the outside for every eengezinswoning
        for coordinates in eensgezins_coordinatenlijst:

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

                # check whether there is free ground around the house
                while vrij = True:
                
                    meter_counter = 3

                    # if there are any houses in the area of the search command then stop searching
                    if wijk1[top_left[0]][top_left[1] - meter_counter] or wijk1[top_left[0] - meter_counter][top_left[1]] or wijk1[top_right[0]][top_left[1] + meter_counter] or wijk1[top_right[0] - meter_counter][top_right[1]] or wijk1[bottom_left[0]][bottom_left[1] - meter_counter] or wijk1[bottom_left[0] + meter_counter][bottom_left[1]] or wijk1[bottom_right[0]][bottom_right[1] + meter_counter] or wijk1[bottom_right[0] + meter_counter][bottom_right[1]] or wijk1[top_middle[0] - meter_counter][top_middle[1]] or wijk1[left_middle[0]][left_middle[1] - meter_counter] or wijk1[right_middle[0]][right_middle[1] + meter_counter] or wijk1[bottom_middle[0] + meter_counter][bottom_middle[1] - meter_counter] != 0:
                        vrij = False
                        print(meter_counter)
                    
                    # if there are no houses found in the area of the search command an extra amount of money to the total worth of the eengezinswoningen
                    else:
                        self.total_eengezins = self.total_eengezins + self.percentage_eengezins
                        meter_counter += 1 



                    # if (
                    #     top_left[0][[1] - meter_counter] is not 0 and top_left[y_coordinate - meter_counter][x_coordinate]
                    #     and top_right[y_coordinate][x_coordinate + meter_counter] is not 0 and top_right[y_coordinate - meter_counter][x_coordinate]
                    #     and bottom_left[y_coordinate][x_coordinate - meter_counter] is not 0 and bottom_left[y_coordinate + meter_counter][x_coordinate]
                    #     and bottom_right[y_coordinate][x_coordinate + meter_counter] is not 0 and bottom_right[y_coordinate + meter_counter][x_coordinate]
                    #     and top_middle[y_coordinate - meter_counter][x_coordinate] is not 0
                    #     and left_middle[y_coordinate][x_coordinate - meter_counter] is not 0
                    #     and right_middle[y_coordinate][x_coordinate + meter_counter] is not 0
                    #     and bottom_middle[y_coordinate + meter_counter][x_coordinate - meter_counter] is not 0
                    # ):

                    #     self.total_eengezins = self.total_eengezins + self.percentage_eengezins

        pass

if __name__ == "__main__":

    price = Price()
    price.housing_costs(12, 5, 3)




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

            range_bungalow_x = 17
            range_bungalow_y = 13
            locatie_outline_boven_x_as =  -4
            locatie_outline_boven_y_as = -4
            locatie_outline_onder_x_as = 14
            locatie_outline_onder_y_as = 10
            constante_x_links = -4
            constante_x_rechts = 14

            check = True
            counter_x = 0
            counter_y = 0 
            counter_x_onder = 0
            counter_y_onder = 0


            while check == True:

                for i in range(range_bungalow_x):

                    if wijk1[coordinates[1] + locatie_outline_boven_x_as][coordinates[0] + locatie_outline_boven_y_as] != 0:
                        check = False
                        print("House found in the area (x-as, boven)")
                        break
                    
                    else:
                        locatie_outline_boven_x_as += 1
                        counter_x += 1 
                        print("x boven")
                        print(wijk1[coordinates[1] + locatie_outline_boven_x_as][coordinates[0]+ locatie_outline_boven_y_as])

                
                for i in range(range_bungalow_y):

                    if wijk1[coordinates[1] + constante_x_links][coordinates[0] + locatie_outline_boven_y_as] != 0:
                        check = False
                        print("House found in the area (y-as, links)")
                        break
                    else:
                        # update by incrementing variable to search area
                        locatie_outline_boven_y_as += 1
                        counter_y += 1 
                        print("y links")
                        print(wijk1[coordinates[1] + constante_x_links][coordinates[0] + locatie_outline_boven_y_as])

                for i in range(range_bungalow_x):
                    # if a house has been found in the area
                    if wijk1[coordinates[1] + locatie_outline_onder_x_as][coordinates[0] + locatie_outline_onder_y_as] != 0:
                        check = False
                        print("House found in the area (x-as, onder)")
                        break

                    else:
                        # update by incrementing variable to search area
                        locatie_outline_onder_x_as -= 1
                        counter_x_onder -= 1 
                        print("x onder")
                        print(wijk1[coordinates[1] + locatie_outline_onder_x_as][coordinates[0] + locatie_outline_onder_y_as])

                for i in range(range_bungalow_y):
                    # if a house has been found in the area
                    if wijk1[coordinates[1] + constante_x_rechts][coordinates[0] + locatie_outline_onder_y_as] != 0:
                        check = False
                        print("House found in the area (y-as, rechts)")
                        break 

                    else:
                        # update by incrementing variable to search area
                        locatie_outline_onder_y_as -= 1
                        counter_y_onder -= 1 
                        print("y rechts")
                        print(wijk1[coordinates[1] + constante_x_rechts][coordinates[0] + locatie_outline_onder_y_as])

                
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

                self.total_eengezins = self.total_eengezins + self.percentage_eengezins
                print(self.total_eengezins)



        def maison(self, coordinaten, maison_aantal):
        
        # make default prices of houses
        self.maison = 610000
        self.maison_aantal = maison_aantal

        # calcualte percentage of extra housing worth per extra sqaure meter space
        self.percentage_maison = self.percentage_maison * 0.06

        # make default total prices
        self.total_maison = maison * self.maison

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
                        print("House found in the area (x-as, boven)")
                        break
                    
                    else:
                        locatie_outline_boven_x_as += 1
                        counter_x += 1 
                        print("x boven")
                        print(wijk1[coordinates[1] + locatie_outline_boven_x_as][coordinates[0]+ locatie_outline_boven_y_as])

                
                for i in range(range_maison_y):

                    if wijk1[coordinates[1] + constante_x_links][coordinates[0] + locatie_outline_boven_y_as] != 0:
                        check = False
                        print("House found in the area (y-as, links)")
                        break
                    else:
                        # update by incrementing variable to search area
                        locatie_outline_boven_y_as += 1
                        counter_y += 1 
                        print("y links")
                        print(wijk1[coordinates[1] + constante_x_links][coordinates[0] + locatie_outline_boven_y_as])

                for i in range(range_maison_x):
                    # if a house has been found in the area
                    if wijk1[coordinates[1] + locatie_outline_onder_x_as][coordinates[0] + locatie_outline_onder_y_as] != 0:
                        check = False
                        print("House found in the area (x-as, onder)")
                        break

                    else:
                        # update by incrementing variable to search area
                        locatie_outline_onder_x_as -= 1
                        counter_x_onder -= 1 
                        print("x onder")
                        print(wijk1[coordinates[1] + locatie_outline_onder_x_as][coordinates[0] + locatie_outline_onder_y_as])

                for i in range(range_maison_y):
                    # if a house has been found in the area
                    if wijk1[coordinates[1] + constante_x_rechts][coordinates[0] + locatie_outline_onder_y_as] != 0:
                        check = False
                        print("House found in the area (y-as, rechts)")
                        break 

                    else:
                        # update by incrementing variable to search area
                        locatie_outline_onder_y_as -= 1
                        counter_y_onder -= 1 
                        print("y rechts")
                        print(wijk1[coordinates[1] + constante_x_rechts][coordinates[0] + locatie_outline_onder_y_as])

                
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
                print(self.total_maison)