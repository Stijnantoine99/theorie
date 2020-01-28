# AmstelHaege
## Random Algorithm
Date: 28/01/2020
* Lars van der Water  - 11320532
* Rob Burger          - 11338059 
* Stijn van den Berg  - 11887648

At the start of the project we wanted to generate a random solution. It would be our basepoint from where we wanted to expand. The houses needed to be placed random but were obligated to the restrictions. While the houses were placed between the right restrictions the price could be calculated. We expected that the price wouldn't be that high. 

### How does it work
For the algorithm to work the user should enter in the main the house-variant(20/40/60) and the neighbourhoodtype (1/2/3). With that the water will be placed with the correct coordinates. After that the single family houses will be placed randomly, followed by the maisons and bungalows. Than every houseprice will be calculated with the price method. 

### How can you use it
In het main method the house-variant & the neigbourhoodtype need to be selected. After that you can enter the amount of runs i.e. how many times do you want generate a neigbourhood. After that the max value and the mean value will be shown in the terminal. The neigbourhood with the highest price will be visualised and a boxplot will be generated with all the data collected.

#### Detailed
The datastructure of the algorithm is a numpy array.
In the placing method a random coordinate is generated within the borders of the grid (160x180). After this the house will be drawn in the grid. If the drawing crosses with an older drawing or with water an error will occur. The coordinate will be deleted and a new coordinate will be generated. This will continue until all the houses are placed.
When the placing is done the price will be calculated. Every meter extra around the house will cause an increasement of the houseprice. To calculate the price the house is removed from the grid. Then the total area of the field is checked for the number 1 (one family house), 2 (bungalow) or 3 (maison). If there is one of these numbers in the total area the price increasment is stopped and the price of the house is calculated. All of these houses together will result in the total price of the area. 

### Results
After running the algorithm, the following results are generated. First, the most valuable neighbourhood is visualized as a 2D grid. Second, a boxplot of the prices of all neighbourhoods is shown, which demonstrates the mean and variance. The input variables (defined in the main function) which were used are: neighbourhoodtype = 2, house-variant = 20 and runs = 1000.

![Map Random](https://github.com/Stijnantoine99/theorie/blob/master/doc/random_map_1000.png)

![Boxplot Random](https://github.com/Stijnantoine99/theorie/blob/master/doc/random_box_1000.png)
