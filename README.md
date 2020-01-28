# AmstelHaege
Group: Utopia

Date: 28/01/2020

![Amstelhaege](https://github.com/Stijnantoine99/theorie/blob/master/doc/Amstelhaege.png)

* Lars van der Water  - 11320532
* Rob Burger          - 11338059 
* Stijn van den Berg  - 11887648

With current housing problem in the city of Amsterdam the local authorities decided to create a 3 new neighborhoods in the southern parts of Amsterdam. The local authorities still have to decide how many houses they want to build in three different neighborhoods. There are 3 different housevariants: 20 houses, 40 houses and 60 houses. The 3 neighborhoods are different in the distribution of the water. 

Every neighborhood is on an area of land with a depth of 180 meters and a width of 160 meters. In every one of the areas the water is distributed in a different way. In every neighborhood there are 3 different house types: single family homes, bungalows and maisons. The houses are always in the same proportions: 60% single family homes, 25% bungalows and 15% maisons. The houses have all different sizes: the single family homes 8x8 meter (width x depth),  bungalows 11x7 meter (width x depth) and maisons 12x10 meters (width x depth). 

All the houses have different prices and obligatory free space around. A single family house has a value of €285.000,- with that it needs 2 meters of obligatory free space. Every extra meter the price of the house increases with 3%. A bungalow has a value of €399.000,- it is obligated to have at least 3 meters of free space around it. Every extra meter the price increases with 4%. The maison has a price of €610.000,- with that it needs 6 meters of obligatory space. Every extra meter the price of the house increases with 6%. The obligatory space of the houses need to be within the neighborhoods area but can cross the water. 

### House table
| House type/features 	| Size (width x dept) 	| Obligatory space in meters 	| Price in euro's 	| Price increasement 	|
|---------------------	|---------------------	|----------------------------	|-----------------	|--------------------	|
| Single family home  	| 8 x 8               	| 2                          	| 285.000         	| 3%                 	|
| Bungalow            	| 11 x 7              	| 3                          	| 399.000         	| 4%                 	|
| Maison              	| 12 x 10             	| 6                          	| 610.000         	| 6%                 	|


# Our Job
It is our job to create the most profitable outcome possible. Here we need to create the neighborhood with the highest house prices and therefore the highest total price for the area. To reach this ultimate situation we wrote 4 different algorithms.

1. [Random algorithm](https://github.com/Stijnantoine99/theorie/tree/master/code/algoritmes/random_algorithm)

   * The random algorithm will place the houses randomly and will calculate the price

2. [Greedy algorithm](https://github.com/Stijnantoine99/theorie/tree/master/code/algoritmes/greedy_algorithm)

   * The greedy algorithm will place very house multiple times and will choose the one with the highest price outcome

3. [Move algorithm](https://github.com/Stijnantoine99/theorie/tree/master/code/algoritmes/move_algorithm)

   * The move algorithm will move the houses after placing and searches for the highest price possible. it will find an equilibrium._

4. [Main algorithm](https://github.com/Stijnantoine99/theorie/tree/master/code/algoritmes/main_algorithm)
 
   * The main algorithm is an combination between the greedy and move algorithm
 

Each of these algorithms are clarified in there own readme wich you can find in the repository or you can click on the links above. The readme files will explain some details of each algorithm:

* How does it work
* What are the results

### The algorithms

The algorithms are made to create the best possible way to place the houses in every neighborhood. Every algorithm is different and are therefore hard to compare. However every algorithm has a method to place the houses and a method to calculate the total price. In the table below we have tried to quantify the amount of steps every algorithm has to take in the place and price method.

__Variables__
* House-variant = 20/40/60
* Random_range = Amount of extra times every house will be placed and checked
* Amount of moves = How much time the move function will run until the balance is found (around 15)
* The 9 in the move function is the amount of possible moves (8) + the current place

#### Comparing algorithms
| Algorithms/Methods 	| Placing                                               	| Price           	|
|--------------------	|-------------------------------------------------------	|-----------------	|
| Random Algorithm   	| House-variant                                         	| 1               	|
| Greedy Algorithm   	| House-variant * random_range                          	| Same as placing 	|
| Move Algorithm     	| House-variant + (9*  House-variant * Amount of moves) 	| Same as placing 	|
| Main Algorithm     	| Greedy(placing) + Move(placing)                       	| Same as placing 	|

The price method will take a longer time to generate. Therefore when comparing it is important that the highest value is the same. This means that the value in the price column needs to have a similar value per algorithm. For example when comparing the random algorithm with the greedy algorithm you will need to run the random algorithm random_range amount of times to be able to compare both algorithms. 

### Requirements
For the code to work these requirements should be met. 

* _pip install numpy_
* _pip install matplotlib_





