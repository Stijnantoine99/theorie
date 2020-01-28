# AmstelHaege
## Move Algorithm
Date: 28/01/2020
* Lars van der Water  - 11320532
* Rob Burger          - 11338059 
* Stijn van den Berg  - 11887648

After looking at the greedy and random algorithms it became clear that the houses were almost never placed in their ideal location. It is clear that if houses are placed on the edges of the grid the price will probably increase. If houses are close to each other it would be likely that when they would move away from each other the price would increase. To create this the move algorithm was created. Move will check the price after moving to 8 different directions. The best one of these moves will be the new location of the house. 

### How does it work
The move algorithm works the same as the random algorithm at first, the houses get placed and the price is calculated. After that every house will be checked for a possible move. The houses will be moved to 8 different positions (topleft, top, topright, right, bottomright, bottom, bottomleft and left). For all of these directions the price is calculated, the highest price is selected and the new coordinate is saved. This will take place for every house until there is no better direction than the current position. When this point is reached the algorithm will stop. After that the max and mean of all the runs will be shown and the best neigbourhood will be visualised.

### How do you use it
For the algorithm to work the house-variant(20/40/60), the neighbourhoodtype (1/2/3) and the amount of runs need to be selected in the main. With that the algorithm will move the houses until there is no better place for any of the houses. The houses will move until they find their balancepoint. 

### Results 
After running the algorithm, the following results are generated. First, the most valuable neighbourhood is visualized as 2D grid. Second, a boxplot of the prices of all neighbourhoods is shown, which demonstrates the mean and its variance. The input variables (defined in the main function) which were used are: neighbourhoodtype = 2, house-variant = 20 and runs = 100.

![Map Move](https://github.com/Stijnantoine99/theorie/blob/master/doc/move_map_100.png)

![Boxplot Move](https://github.com/Stijnantoine99/theorie/blob/master/doc/move_box_100.png)
