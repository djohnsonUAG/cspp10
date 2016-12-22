import random
# function name: roll_dice
# purpose: rolls two random dice rolls,
# prints it out, and returns the sum
# arguments: None
# returns: the sum of the two dice
def roll_dice():
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    dice_sum = dice1 + dice2
    print("A {} and a {} were rolled. The total of your dice roll is {}.".format(dice1,dice2,dice_sum))
    return dice_sum

# function name: get_bet
# purpose: prints how much
# bank money you have,
# asks for how much you will
# bet, returns it and only
# accept valid bets-00p,ghgg
# arguments: bank_account
# returns: the bet money
def get_bet(bank_account):
    print("How much{}")
    #bank money
    print("how much are you will bet{}")
    return get_bet(bank_account)
    
    
    
# function name: check_first_roll
# purpose: returns whether the first roll
# was a winning roll, a losing roll, or it was neither
# and we need to need to use it as a point number
# in the next phase
# arguments: the first phase dice roll
# returns: it returns a win or lose(True or False)
# or the point number you rolled
def check_first_roll(first_roll):
    if first_roll == 2 or first_roll == 3 or first_roll == 12:
        print("Rolling a {} in the first phase means you lose. Give me your money!".format(first_roll))
        return False
    elif first_roll == 7 or first_roll == 11:
        print("Rolling a {} in the first phase means you win. Here's your win money.".format(first_roll))
        return True
    else:
        print("Rolling a {} in the first phase means you have to move to phase 3. {} is your point number then.".format(first_roll,first_roll))
        return first_roll
        
# function name: ask_to_end_game
# purpose: it will ask the user
# if they want to end the game
# and returns true or false based
# on that
# arguments: None
# returns: True or False
def ask_to_end_game():
    prompt = input("Would you like to make another bet? [\'y\' or \'n\'] ")
    while prompt != 'y' and prompt != 'n':
        print("You just have to answer \"Yes\" or \"No\" by typing either \'y\' or \'n\'.")
        prompt = input("Now I will ask you again. Would you like to make another bet? [\'y\' or \'n\'] ")
    if prompt == 'y':
        return True
    else:
        return False
        
# function name: check_phase_3_rolls
# purpose: it will keep checking each next roll
# if the first roll is a point number
# until a winning roll or a losing roll
# is rolled
# arguments: the result of the first roll
# and the first phase 3 dice roll
# returns: True, False, or does nothing
def check_phase_3_rolls(first_roll_result,first_phase_3_roll):
    if type(first_roll_result) == type(1):
        while first_phase_3_roll != 7 and first_phase_3_roll != first_roll_result:
            next_dice_roll = roll_dice()
            if next_dice_roll == 7:
                print("Rolling a {} in the . ".format(next_dice_roll))
                return False
            elif next_dice_roll == first_roll_result:
                print("Rolling a {} in the . ".format(next_dice_roll))
                return True
    else:
        return 0
            