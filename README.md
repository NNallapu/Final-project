


# Title: MCS Simulation of Snakes and Ladders game 

## Team Member: Nandana Nallapu


# Monte Carlo Simulation Scenario & Purpose:
What was interesting to me about this game is that it is purely based on chance and probability and there's no skill involved. So it makes for a perfect candidate to apply Monte Carlo simulation. 

Understanding the workings of a Finite State Machine like Snakes and Ladders, and implementing the rules regarding when and how the system moves from one state to another, and what factors affect this state change. The purpose is to look at the questions like what is the minimum number of moves made in the game to finish it, given two players, and to see what is the shortest time to win the game, given two players - how many moves are typically required to win, which ladder helps the winner most.

### Hypothesis before running the simulation:

The hypothesis is that there is an average running time for the game and chances of the game going on forever are slim, even if certain folks are unlucky enough to keep going down the Snakes. From the experiment, the 

### Simulation's variables of uncertainty

All players start with a single roll die to reach one of the 100 squares. On each trial, there are equal chances of getting a ladder,snake or just a number/snake's tail/ladder's top. After running the simulation a number of time, by dividing the total number of moves by the number of games, we get an estimate for the average number of moves. 

According to Nick Berry, the Markov chain analysis of Snakes and Ladders would have better possibility of giving an exact answer for Snakes and Ladders, as it takes into account stochastic probabilities of each die roll depending on the square the user is at, instead of a random generator for a die roll. For example,for reaching the square 53 from 50 square - a 3 on the die will take the user to 53 and a roll die of 6 would also take user to 53 as 56 has the head of snake taking user down to 53. So, the probability of moving from square 50 to square 53 is 2/6 and not 1/6. Such conditions can be better represented in Markov Model.

## Instructions on how to use the program:

Part 1 consists of Instructions function which just displays the instructions. It also consists of a calculation for number of moves of a typical game, with die roll randomly generated, a function to calculate the path moved from square 1 to square 100 and the Monte caro simulation for a million games. 


## Sources Used:
Snakes and Ladders Wiki: https://en.wikipedia.org/wiki/Snakes_and_Ladders
Mathematical Analysis of Snakes and Ladders by Nick Berry: http://ksuweb.kennesaw.edu/~jprest20/cgdd2002/CC_Mag_Winter_2012.pdf
Implementation of board games: https://www.ijircce.com/upload/2016/april/197_Implementation.pdf
Data Genetics blog :  http://datagenetics.com/blog/november12011/index.html

