# AmstelHaege
Group: Utopia

Date: 28/01/2020

* Lars van der Water  - 11320532
* Rob Burger          - 11338059 
* Stijn van den Berg  - 11887648

![Amstelhaege](https://github.com/Stijnantoine99/theorie/blob/master/doc/Amstelhaege.png)

## Problem Statement
With current housing problem in the city of Amsterdam the local authorities decided to create 3 new neighbourhoods in the southern parts of Amsterdam. The local authorities still have to decide how many houses they want to build in three different neighbourhoods. There are 3 different housing variants: 20 houses, 40 houses and 60 houses. The 3 neighbourhoods are different in the distribution of the water. 

Every neighbourhood is on an area of land with a depth of 180 meters and a width of 160 meters. In every one of the areas the water is distributed in a different way. In every neighborhood there are 3 different house types: single family houses, bungalows and maisons. The houses are always in the same proportions: 60% single family houses, 25% bungalows and 15% maisons. The houses all have different sizes: the single family houses 8x8 meter (width x depth),  bungalows 11x7 meter (width x depth) and maisons 12x10 meters (width x depth). 

All the houses have different prices and obligatory free space around. A single family house has a value of €285.000,- and needs 2 meters of obligatory free space. For every extra meter, the value of the house increases with 3%. A bungalow has a value of €399.000,- it is obligated to have at least 3 meters of free space around it. For every extra meter, the value increases with 4%. The maison has a value of €610.000,- and needs 6 meters of obligatory space. For every extra meter, the value of the house increases with 6%. The obligatory free space of the houses need to be within the neighbourhoods area but it is able to 'cross' the water.

### House table
| House type/features 	| Size (width x dept) 	| Obligatory space in meters 	| Price in euro's 	| Price increasement 	|
|---------------------	|---------------------	|----------------------------	|-----------------	|--------------------	|
| Single family home  	| 8 x 8               	| 2                          	| 285.000         	| 3%                 	|
| Bungalow            	| 11 x 7              	| 3                          	| 399.000         	| 4%                 	|
| Maison              	| 12 x 10             	| 6                          	| 610.000         	| 6%                 	|


## Solution
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

### State space

Regarding the case of Amstelhaege, the placement and moving of the houses using the algorithms can be seen as a dynamic system over time. The houses have certain coordinates, but are moved over time in order to get a higher total price. The increase in total price hereby depicts the system getting to a higher energy level state.

This dynamic system can be represented in a state space model. This model consists out a set of input values, output values and state variables. Furthermore this dynamic system also has certain constant values.
  
#### The constant values in the dynamic system:
  - Water: The water in the models is a constant as it is placed in a predetermined area and does not change over time
  - Default price for houses: The default price does not get higher or lower in the system over time.
  - Number of houses: There is always a predetermined number of houses in the models.

#### Input values into the dynamic system ( u(t) ):
  - Moving of the houses: The moving of the houses portrays an input into the system which alters the overall state of the system, because the moving of a house changes so does the price of specific houses.

#### State variables ( x(t) ):
  - Coordinates of individual houses: The coordinates of the individual houses are the only state variables in the system of this case, because this is the minimum set of variables which enables to fully describe the system. Other values like individual housing price and total housing price can be determined from the housing coordinates. These values are therefore not first order variables. The coordinates can not be determined from pricing. Therefore coordinates are first order state variables.

#### Output ( y(t) ):
  - Total housing price: The output of the dynamic system which changes over time is the total housing price.

#### Initial conditions of the model for the variable part of the system:
Understanding the initial conditions will help to show why the movement of the houses are the state variables. This is because it should be possible to predict what state the system will be in over time if you know the constant values, the input values and the initial conditions. 
Example: the condition is a change in total price. This change can be determined from the difference in coordinates before and after moving.
    
#### Change in energy of the system over time
A dynamic system stores energy. In this particular system the only storage element for energy are the houses and store their indivual prices. The price is the form of energy in this system. The energy of every house is known from the coordinates of the house and the other houses.

### Upper and Lower bound of the system

In order to determine the limits of accuracy for this problem the upper and lower bound has to be determined.

#### Lower bound

The lower bound of the problem for this case can be easily defined. On account if all houses do not have any extra free space they will have their default value prices. The lower bounds have different values between the model variants with a difference in number of houses as the sum of all housing prices accounts for the total housing price:

  - 20 houses:
    - (285,000 * 12 + 399,000 * 5 + 610,000 * 3) = 7,245,000
  - 40 houses:
    - (285,000 * 24 + 399,000 * 10 + 610,000 * 6) = 14,490,000
  - 60 houses:
    - (285,000 * 36 + 399,000 * 15 + 610,000 * 9) = 21,735,000
    
#### Upper bound

Our theory for determining the upper bound is based on maximizing the increase in price for one house, while minimizing the increase for the other houses. Both the single family household and the bungalow receive a lower added value when given extra free surrounding compared to the maison:

  - Single family household = 285,000 * 0.03 = 8,550 added for every meter
  - Bungalow                = 399,000 * 0.04 = 15,960 added for every meter
  - Maison                  = 610,000 * 0.06 = 36,600 added for every meter

The upper bound could be determined by eliminating the increase in value for the lower earning houses. Furthermore the total price should be higher if only one of the highest earning houses is isolated. The increase in individual housing price will be terminated once another house is met. Isolating more than one house should therefore eliminate the increase in housing price prematurely.
By placing all other houses at the furthest distance possible from this single isolated house, the upper bound could therefore be determined:

##### Example upper bound: 1st neighbourhood with 20 houses

  - First the gridmap area is determined without the water:
    - Normal area    = 160x180
    - Water area     = 32x180
    - Grassland area = 132x180 -> the total area to place houses therefore is: 23,040
  - Secondly subtract the total area of all houses AND 
  calculate the mandatory free space for every house type:
    - Total area houses            = Single(8 * 8 * 12 = 768) + Bungalow(11 * 7 * 5 = 385) + Maison(12 * 10 * 3 = 360) = 1,513
    - Free space for one single    = 4 * 12 + 4 * 8 = 80 -> for 12 households = 12 * 80 = 960
    - Free space for one bungalow  = 4 * 10 + 4 * 11 = 84 -> for 5 households = 5 * 84 = 420
    - Free space for one maison    = 4 * 16 + 4 * 12 = 336 -> for 3 households = 3 * 336 = 1,008
    - Grassland area - total housing area - mandatory free space = 23,040 - 1,513 - 2,388 = 19,139 area left
  - Thirdly calculate with the area left what the isolated maison could earn maximally:
    - square root area left √(19,139) ~ 138
    - 138 * 36,600 = 5,050,800 euro's extra added to the maison's value
  
However there is still some area which could increase the total price of the neighbourhood. The pricing of the houses is calculated from the outline of the mandatory free space till the outline of another house's wall. Therefore if placed in a right way the houses with a lower mandatory free space can benefit from the houses with a higher mandatory free space. A single family household has 2 meter mandatory free surrounding, while a maison should have 6 meter. The difference in 4 meter can be accounted as extra free space for the single family household, which means that is two/third from the mandatory free space of the maison:

  - Beneficial extra area for bungalow = 1,008(maison) * 0.5 = 504 extra area:
    - √(504) ~ 22 -> 22 * 15,960 = 351,120 euro's extra added to the bungalow value
    - 351,120 * 5 = 1,755,600 euro's extra added for all bungalows
  - Beneficial extra area for single = 1,008(maison) * 0.333 + 420(bungalow) * 0.667 ~ 615 extra area
    - √(615) ~ 24 -> 24 * 8,550 = 205,200 euro's extra added to the single value
    - 205,200 * 12 = 2,462,400 euro's extra added for all single households
    
Taken from this hypothetical state of the model the upper bound could be calculated by adding the default values of the houses to the increase in value for all the houses:

  * 7,245,000 + 5,050,800 + 1,755,600 + 2,462,400 = 16,513,800 euro's as a total price
  > This value could probably never be met as the placement of the houses could not be achieved this ideally without wasting the regular area for the isolated maison

### Requirements
For the code to work these requirements should be met. 

* _pip install numpy_
* _pip install matplotlib_





