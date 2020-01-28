# AmstelHaege
## Simulated Annealing Algorithm
Date: 28/01/2020
* Lars van der Water  - 11320532
* Rob Burger          - 11338059 
* Stijn van den Berg  - 11887648

One of the big shortcomings for an algorithm which uses a hill climbing technique like our move algorithm is the possibility to get stuck in a local maximum. The reason for that in this particular case is that the algorithm searches for the direction resulting in the highest price. If there is no movement which increases the price the algorithm will not move the houses anmymore. However this does not have to mean the maximum price has been found for the neighbourhood. It could also mean the houses are stuck as they are only able to move one step in the eight directions. The simulated annealing technique helps in overcoming this problem by taking bigger steps accross the dimensions of the model. In our case the simulated annealing would check if a bigger step could be taken if there are no single step movements possible. The algorithm tests whether movements which result in a lower price have a certain chance to increase after the annealing step again by checking the acceptance propabilties of the annealing steps. This way houses which are stuck in their movement could still be moved to different directions on the map in order to increase their price.

### Hypothesis
Even though the simulated annealing technique works very well to escape local maxima/minima, there is no certainty the algorithm will increase the total price more than the move algorithm. This is because of the fact that the houses are able to move in 8 different directions and if one house gets stuck this does not mean a permanent local maximum. Due to the possibility one of the other houses is able to move this could enable the house which was stuck to move again. For this reason simulated annealing could only be helpful by minimizing running time as the houses move in bigger steps than the move algorithm.

### How does it work
The simulated annealing algorithm works the same as the move algorithm. The houses are placed at random afterwhich every house will be checked if the a move will increase its price. The houses will be moved in 8 different directions. For all of these directions the price is calculated, the highest price is selected and the new coordinate is saved. Every time one of the houses has been tried to move, the algorithm checks whether the house has moved from its current position. 
If the house has not moved the algorithm checks if simulated annealing is possible. Simulated annealing starts by selecting a random integer in the range between the temperature and a few numbers below the temperature. If a range between 1 and the temperature will be used a constant average could be the annealing steps. The randomly selected integer will be the amount of steps for every 8 directions the house can move to (just like the move algorithm). If the annealing step is possible, the acceptance probability is calculated **(2^(score_old – score_new )/temperature)**. If the acceptance probability is below a certain threshold (determined beforehand) one of the probablties below this threshold will be randomly selected. The step which belongs to this selected probabilty will be initiated. 
This will take place for every house untill all houses have been tried to move once. Normally when this point is reached the idea would be to decrease the temperatuer by one (if simulated annealing has been performed) and start to try and move the houses again. This would continue untill the temperature itself is one. However we have not been able to create a working 'temperature cooling down' method for the algorithm. Therefore the temperature stays the same while running the algorithm. 

#### How do you use it 
For the algorithm to work the house-variant(20/40/60), the neighborhoodtype (1/2/3) and the amount of runs need to be selected in the main. With that the algorithm will move the houses until there is no better place for any of the houses. The houses will move until they find their balancepoint. Moreover the temperature and threshold for the acceptance probability have to be inserted. This can be done in the move method.

### Results 
Since the algorithm is not finished yet, no results can be shown for this algorithm.

### Improvements
Due to time shortage we had at the end the algorithm is not fully functional yet. Therefore there are some points which should be improved on. The important improvements are:

  - Create a cooling down method for the temperature. As mentioned the temperature is supposed to decrease after every house has been tried to move. However currently there is no method to enable this.
  - Divide the "Move" class into a "Move" and "Simulated annealing" class. The "Move" class was purposed for the hill climbing method and the simulated annealing was supposed to be a different class. However due to time shortage we were not able to this before the deadline.
  - Enable the user of the algorithm to insert the values for temperature and acceptance probabilty threshold in the main function. This makes use of the algorithm more comfortable for the user.
