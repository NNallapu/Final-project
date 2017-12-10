import random

end = 100

#Dictionary to store the Chutes to jump up(ladder) or fall down(snake)
chutes = {1: 38, 4: 14, 9: 31, 16: 6, 21: 42, 28: 84, 36: 44,
          48: 26, 49: 11, 51: 67, 56: 53, 62: 19, 64: 60, 71: 91,
          80: 100, 87: 24, 93: 73, 95: 75, 98: 78}


def display_instruction():
    """ Display game instructions."""

    print(
    """
    Welcome to the Monte Carlo simulation of Snakes and Ladders game.
    Rules are simple. 
        1. Start at 0 (before rolling the die). 
        2. Roll the die. Move accordingly.
        3. If you reach a snake's head, you fall down to its tail.
        4. Likewise, if you reach the foot of the ladder, you can climb up. 
        5. No consequences of reaching snake's tail or ladder's top, by a throw of die.
        6. Goal is to reach the number 100 on the board.
        
      WINNER ---->      100 | 99 | 98 | 97| 96 | 95 | 94 | 93 | 92 | 91 | 
                        90 | 89 | 88 |87 | 86 | 85 | 84 | 83 | 82 | 81
                        .   .   .   .   .   .   .   .   .   .   .   .   .
                        .   .    .    .     .    .    .    .    .    .   .   
                        10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1              <----- START HERE                      
    """
    )

def roll_dice():
    """

    :return:
    random integer in the range of 1 to 6
    """
    return random.randint(1,6)

def no_of_moves():
    """
    Takes roll_dice integer as input d
    i is the counter starting at 0
    :return:
    Output n, an integer which gives no. of moves
    """
    i = 0
    n = 0

    while (i < 100):
        n = n + 1
        d = roll_dice()
        i = i + d
        if (100 < i):
            i = 100
        if i in chutes:
            i = chutes[i]
        else:
            i = i + d

    return n


def game_path():
    """

    :return:
    Calculates and returns the minimum rolls taken to reach each square
    """
    start = {0}
    path = {0: ()}

    while len(start) > 0:
        i = start.pop()
        p = path[i] + (i,)
        for j in range(i + 1, i + 7):
            if j > end: break
            if j in chutes: j = chutes[j]
            if j not in path or len(path[j]) > len(p):
                start.add(j)
                path[j] = p
    for i in path:
        if(i == 100):
            print("=====================================================================")
            print("SQUARE 100 CAN BE REACHED IN ", len(path[i]), "ROLLS VIA", path[i])
            print("=====================================================================")
        else:
            game_path = print("Square", i, "can be reached in ", len(path[i]), "rolls via", path[i])
    return game_path


def monte_carlo():
    games = 0
    total = 0
    while (games < 1000000):
        games = games + 1
        n = no_of_moves()
        total = total + n
        average = total / 1000000
    return str(average)

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

if __name__ == '__main__':
    display_instruction()
    print("\n")
    game_path()
    print("\n")
    a = no_of_moves()
    c = monte_carlo()
    print("===================================================")
    print("Current Game length is " + str(a) + " moves \n")
    print("===================================================")
    print("1000000 simulations of the game gives an average of " + str(c) + " moves\n")
    print("===================================================")
    print("Running the Snakes and Ladders game for two players \n")
    Player1 = no_of_moves()
    Player2 = no_of_moves()
    if Player1 < Player2:
        print("Winner of the game is Player1 with " +str(Player1)+ " moves. While Player2 had "+str(Player2)+ " moves")
    else:
        print("Winner of the game is Player2 with " +str(Player2)+ " moves. While Player1 had "+str(Player1)+ " moves")



