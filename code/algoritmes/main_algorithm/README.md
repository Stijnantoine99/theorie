# AmstelHaege
## Main Algorithm
Date: 28/01/2020
* Lars van der Water  - 11320532
* Rob Burger          - 11338059 
* Stijn van den Berg  - 11887648

To acieve the best possible outcome the algorithms from before where combined to one main algorithm. Here the greedy algorithm and the move algorithm will be combined. The houses will be placed with the help of the greedy algorithm and after that the houses will be moved. This creates the highest possible outcome with the writen algorithms. 

### How does it work
Every house will be placed random_range amount of times. From these the location with the highest price will be saved and selected. After that all the houses are placed and the move function will look for every house if there is a better option surrounding it. If there is the house will move to this direction. This will happen for every house and if there is not a better option for a house the house will remain on it's position. The houses will move untill all the houses don't have a better option. The better option doesn't have to be better for the houseprice of the selected house. The best option is where the total price of the field is the highest. 

#### How can you use it
To use the algorithm it is necessary to choose the house-variant(20/40/60), the neighborhoodtype(1/2/3), the random_range and the amount of runs. This will create a gridmap with all the placed houses. After the placing every house will move with the move function. When the houses cannot increase the price with moving the algorithm will end. Based on the amount of runs the algorithm will start over. After all the runs the max and mean price will be shown. The neighborhood with the highest price will be visualised and a boxplot will appear. 

### Results 
After running the algorithm with neighbourhood_type = 2, house_variant = 20, runs = 100 and random_range = 10.

![Map Main](https://github.com/Stijnantoine99/theorie/blob/master/doc/main_map_100.png)

![Boxplot Main](https://github.com/Stijnantoine99/theorie/blob/master/doc/main_box_100.png)
