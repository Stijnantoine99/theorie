def housing_costs(self, eengezins, bungalow, maison):

"""Prijs bepalen code"""

    # make default prices of houses
    self.eengezins = 285000
    self.bungalow = 399000
    self.maison = 610000

    # make default total prices
    self.total_eengezins = eengezins * self.eengezins
    self.total_bungalow = bungalow * self.bungalow
    self.total_maison = maison * self.maison

    # Iterate over the array
    for i in range(len(array)):
        for j in range(len(array[i])):

            # scan if there is extra space around the house
            if spot is E:
                if array[E - 3] is G or W and array[E + 11] is G or W: