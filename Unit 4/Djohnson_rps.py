import random

def get_p1_move():
    while True:
        p_choice = input("rock, paper or scissors?: ")
        if p_choice == "rock":
            return "r"
        elif p_choice == "paper":
            return "p"
        elif p_choice == "scissors":
            return "s"
        else:
            print(" I couldn't understand, please try Again")

def get_comp_move():
    c_choice = random.randint(1,3)
    if c_choice == 1:
        return "r"
    elif c_choice == 2:
        return "p"
    elif c_choice == 3:
        return "s"

def get_rounds():
    rounds = int(input("How many rounds would you like to play? (between 1 and 9): "))
    return rounds

def get_round_winner(p_choice, c_choice):
    if p_choice == c_choice:
        return "tie"
    elif p_choice == "r" and c_choice == "s":
        return "player"
    elif p_choice == "r" and c_choice == "p":
        return "comp"
    elif p_choice == "p" and c_choice == "r":
        return "player"
    elif p_choice == "p" and c_choice == "s":
        return "comp"
    elif p_choice == "s" and c_choice == "p":
        return "player"
    elif p_choice == "s" and c_choice == "r":
        return "comp"

def get_full_move(shortmove):
    if shortmove == "r":
        return "Rock"
    elif shortmove == "p":
        return "Paper"
    elif shortmove == "s":
        return "Scissors"

def print_score(pscore, cscore, ties):
    return "The score is Player 1: {}, Player 2: {}, and {} ties.".format(pscore,cscore,ties)

def rps():
    print("Welcome to the game Rock, Paper, Scissors!")
    print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _")
    print("")
    rounds = get_rounds()
    pscore = 0
    cscore = 0
    ties = 0
    for x in range(rounds):
        print ("Round {}!".format(x + 1))
        p_choice = get_p1_move()
        c_choice = get_comp_move()
    
        print("Player chose: {}".format(get_full_move(p_choice)))
        print("Computer chose: {}".format(get_full_move(c_choice)))
    
        winner = get_round_winner(p_choice,c_choice)
        if winner == "player":
            print("The Player won....So that would be you!!!")
            pscore = pscore + 1
        elif winner == "comp":
            print("The Computer won...maybe next time you will win:(")
            cscore = cscore + 1
        else:
            print("It's a tie")
            ties = ties + 1
        print(print_score(pscore,cscore,ties))
        print("")
        print(" _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ ")
    print(print_score(pscore,cscore,ties))



rps()