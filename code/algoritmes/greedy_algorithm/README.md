# AmstelHaege
## Greedy algorithm
Date: 28/01/2020
* Lars van der Water  - 11320532
* Rob Burger          - 11338059 
* Stijn van den Berg  - 11887648

After the random algorithm it was clear that the ideal situation was not met. When placing randomly it was clear that many houses would be placed next or very close to each other. This means that the freespace is not ideally used. It became clear that these houses only created a negative effect on the total price. We understood that these houses needed to be prevented. To achieve this the greedy algorithm was created, an algorithm that will calculate the price after each time of placing a house. With this functionallity we can place houses multiple times and choose the one with the highest price. 

### How does it work
The algorithm is almost the same as the random algorithm. The price calculation and the way of placing is still the same. However, in the main a new variable is added, the random_range variable. This variable shows the amount of times you want to place a single family house. For example, if you want to do this 10 times. Every house will be 10 times randomly placed with each an unique price. The one with the highest price of these 10 will be saved and added in the grid. 

### How can you use it 
To use the algorithm you need to choose the house-variant (20/40/60), the neighbourhoodtype (1/2/3) and the random_range (amount of times you want to place a house). Also, you need to choose the amount of runs you want the whole algorithm to run. From these runs the mean and max will be shown in the terminal. The neigbourhood with the highest price will be visualised and a boxplot of all the runs will be shown.

### Results
After running the algorithm, the following results are generated. First, the most valuable neighbourhood is visualized as 2D grid. Second, a boxplot of the prices of all neighbourhoods is shown, which demonstrates the mean and variance. The input variables (defined in the main function) which were used are: neighbourhoodtype = 2, house-variant = 20, runs = 100 and random_range = 10.

![Map Greedy](https://github.com/Stijnantoine99/theorie/blob/master/doc/Greedy_map_100.png)

![Boxplot Greedy](https://github.com/Stijnantoine99/theorie/blob/master/doc/Greedy_box_100.png)
