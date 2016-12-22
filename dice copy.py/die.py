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
    print("------------------------------")
    print("A {} and a {} were rolled. The total of your dice roll is {}.".format(dice1,dice2,dice_sum))
    return dice_sum

# function name: get_bet
# purpose: prints how much
# bank money you have,
# asks for how much you will
# bet, returns it and only
# accept valid bets
# arguments: bank_account
# returns: the bet money
def get_bet(bank_account):
    print("------------------------------")
    print("You have ${} in your bank account.".format(bank_account))
    bet_money = float(input("How much will you bet from your bank money for this round? "))
    while int(bet_money) > bank_account or int(bet_money) != bet_money or int(bet_money) < 0:
        if int(bet_money) != bet_money and int(bet_money) < 0:
            print("Your bet must be an integer and you can not bet nonexistent money.")
            bet_money = float(input("I ask you again. How much will you bet for this round? "))
        elif int(bet_money) > bank_account and int(bet_money) != bet_money:
            print("Your bet must be an integer and you can not bet more than what you have in the bank.")
            bet_money = float(input("I ask you again. How much will you bet for this round? "))
        elif int(bet_money) > bank_account:
            print("Your bet money can not be more than what you have in the bank.")
            bet_money = float(input("I ask you again. How much will you bet for this round? "))
        elif int(bet_money) != bet_money:
            print("Your bet must be an integer.")
            bet_money = float(input("I ask you again. How much will you bet for this round? "))
        else:
            print("Your cannot bet nonexistent money.")
            bet_money = float(input("I ask you again. How much will you bet for this round? "))
    return int(bet_money)
    
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
        print("Rolling a {} in the first phase means you win. Here\'s your win money.".format(first_roll))
        return True
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
    print("------------------------------")
    prompt = input("Would you like to make another bet? [\'y\' or \'n\'] ")
    while prompt != 'y' and prompt != 'n':
        print("You can answer \"Yes\" or \"No\" by typing either \'y\' or \'n\'.")
        prompt = input("Now I will ask you again. Would you like to make another bet? [\'y\' or \'n\'] ")
    if prompt == 'y':
        print("Then we shall continue.")
        return True
    print("Then we shall not continue.")
    return False
        
# function name: check_phase_3_rolls
# purpose: it will keep checking each next roll
# if the first roll isn't a point number
# until a winning roll or a losing roll
# is rolled
# arguments: the result of the first roll
# returns: True, False, or does nothing
def check_phase_3_rolls(first_roll_result):
    if type(first_roll_result) == type(1):
        first_phase_3_roll = roll_dice()
        if first_phase_3_roll != 7 and first_phase_3_roll != first_roll_result:
            print("Rolling a {} in phase 3 means you have to roll again.".format(first_phase_3_roll))
            print("Remember. Your point number is {}.".format(first_roll_result))
            input("Press enter to continue")
            while first_phase_3_roll != 7 and first_phase_3_roll != first_roll_result:
                next_dice_roll = roll_dice()
                if next_dice_roll == 7:
                    print("Rolling a 7 in phase 3 means you lose. Give me your money!")
                    input("Press enter to continue")
                    return False
                elif next_dice_roll == first_roll_result:
                    print("Rolling a {} in phase 3 means you win. Here\'s your win money.".format(next_dice_roll))
                    input("Press enter to continue")
                    return True
                print("Rolling a {} in phase 3 gives you nothing. You have to roll again.".format(next_dice_roll))
                print("The point number you need to win is {}.".format(first_roll_result))
                input("Press enter to continue")
        elif
    return 0

# function name: give_ending_response
# purpose: prints some final remarks
# about the outcome of the game
# arguments: bank cash
# returns: nothing but print statements
def give_ending_response(final_money_count):
    if final_money_count == 0:
        print("------------------------------")
        print("You have lost all your money! You lose.")
    else:
        print("------------------------------")
        print("You ended our game of Craps with ${} in the bank.".format(final_money_count))
        if final_money_count < 100:
            print("Well, you\'ve just lost ${} from the $100 you had in the beginning.".format(100 - final_money_count))
            print("Well, you are giving up anyway so whatever. Nevertheless it\'s")
        elif final_money_count > 100:
            print("Hey! You have made ${} more than the $100 you had before! Good Job!".format(final_money_count - 100))
            print("Anyway, thanks for playing. Now it\'s")
        else:
            print("You didn\'t even make anything.")
    print("GAME OVER.")
    
# function name: ask_for_tutorial
# purpose: asks if you want a tutorial
# and will print out a tutorial
# if you say yes
# arguments: None
# returns: None
def ask_for_tutorial():
    print("------------------------------")
    tutorial_prompt = input("Would you like a tutorial on Craps? [\'y\' or \'n\'] ")
    while tutorial_prompt != 'y' and tutorial_prompt != 'n':
        print("You can answer \"Yes\" or \"No\" by typing either \'y\' or \'n\'.")
        tutorial_prompt = input("Now I will ask you again. Would you like a tutorial on Craps? [\'y\' or \'n\'] ")
    if tutorial_prompt == 'y':
        give_tutorial()
    else:
        print("Then we shall begin the game.")

# function name: give_tutorial
# purpose: prints lengthy tutorial
# arguments: None
# returns: None
def give_tutorial():
    input("Okay. Press enter to continue to the tutorial.")
    print("------------------------------")
    print("Craps is a gambling game where the player bets money")
    print("and then dice is rolled. Based on the sum of their")
    print("roll, they will either win their bet, lose their")
    print("bet, or roll again for a winning or losing roll.")
    print("Now let me explain what are the rules that determine")
    print("this.")
    input("Press enter to continue.")
    print("")
    print("The first roll you make can result in a couple of")
    print("things. If you roll a 2, 3, or a 12, you lose. If")
    print("you roll a 7 or an 11, you win. But if you roll")
    print("anything else, you have roll again and the rules")
    print("change. If you roll only a 7, you lose. If you")
    print("roll the number you rolled in the first round, you")
    print("win. This number is also called the point number.")
    print("If you roll something else, nothing happens and")
    print("you simply roll again and again until you roll a")
    print("7 or your point number. Now let me explain a few")
    print("other things.")
    input("Press enter to continue.")
    print("")
    print("When you start the game, you will have $100. You")
    print("can only bet a positive whole number that is not")
    print("more than the $100 you have. Another thing to")
    print("mention is that the game will only end when you")
    print("run out of money or if you decide to answer \'No\'")
    print("to a prompt asking if you want to continue the")
    print("game at the end of each round.")
    input("Press enter to continue.")
    print("")
    print("Now that\'s all for the tutorial! Let\'s play Craps!")
  
# function name: craps
# purpose: the main game function, uses all of
# the functions to perform game
# arguments: None
# returns: None
def craps():
    print("Let\'s play Craps!")
    ask_for_tutorial()
    bank_cash = 100
    round_counter = 0
    run_game = True
    while run_game == True and bank_cash > 0:
        bet = get_bet(bank_cash)
        round_counter = round_counter + 1
        print("------------------------------")
        print("Round {}!".format(round_counter))
        first_dice_roll = roll_dice()
        phase2 = check_first_roll(first_dice_roll)
        input("Press enter to continue.")
        phase3_rolls = check_phase_3_rolls(phase2)
        if phase3_rolls == 0:
            if phase2 == True:
                print("------------------------------")
                print("${} is added to the bank.".format(bet))
                bank_cash = bank_cash + bet
                run_game = ask_to_end_game()
            else:
                print("------------------------------")
                print("${} is taken from the bank.".format(bet))
                bank_cash = bank_cash - bet
                if bank_cash > 0:
                    run_game = ask_to_end_game()
        elif phase3_rolls == True:
            print("------------------------------")
            print("${} is added to the bank.".format(bet))
            bank_cash = bank_cash + bet
            run_game = ask_to_end_game()
        else:
            print("------------------------------")
            print("${} is taken from the bank.".format(bet))
            bank_cash = bank_cash - bet
            if bank_cash > 0:
                run_game = ask_to_end_game()
    give_ending_response(bank_cash)
        
craps()