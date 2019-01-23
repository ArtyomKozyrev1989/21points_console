import string
import time


def welcome():
    print(
        '''
        ***************************************

             WELCOME TO THE GAME 21 POINTS
                 FOR ONE PLAYER VS PC

        ***************************************
        ''')


def _normalize_name(name):
    name = name.split()
    normalized_name = ""
    for i in range(len(name)):
        if i != len(name) - 1:
            normalized_name += name[i] + " "
        else:
            normalized_name += name[i]
    return normalized_name

def _check_name_symbols(name):
    allowed_symbols = string.ascii_letters + string.digits
    for symbol in allowed_symbols:
        if symbol in name:
            return True
    return False

def choose_player_name():
    while True:
        name = input("Please choose player name: ")
        if len(name) > 40:
            print("Player's name should be less than 40 symbols, please try again!")
        else:
            if _check_name_symbols(name):
                return _normalize_name(name)
            else:
                print("Player's name should contain digits or letters, please try again!")

def do_want_another_card():
    while True:
        print("Do you want to take another card?")
        take = _normalize_name(input("Press Enter if yes, otherwise print NO and press Enter: "))
        if take == "":
            return True
        elif take.upper() == "NO":
            return False
        else:
            print("Incorrect input, please try again!")

def do_want_another_game():
    while True:
        print("Do you want to play another game?")
        play = _normalize_name(input("Press Enter if yes, otherwise print NO and press Enter: "))
        if play == "":
            return True
        elif play.upper() == "NO":
            return False
        else:
            print("Incorrect input, please try again!")

def check_if_less_21(player):
    if player.points_have() <= 21:
        return True
    else:
        return False

def check_who_win_series(player1, player2):
    print(f"{player1.name} has {player1.victory_number} victories")
    print(f"{player2.name} has {player2.victory_number} victories")
    if player1.victory_number > player2.victory_number:
        print(f"{player1.name} won the series")
    elif player1.victory_number == player2.victory_number:
        print(f"We have DRAW in the series")
    else:
        print(f"{player2.name} won the series")

def goodbye():
    print("Thank you for the game, the program will be terminated in 10 seconds")
    seconds_left = 10
    for i in range(2, 10, 2):
          time.sleep(2)
          print(f"{seconds_left - i} seconds left")
    print("See you!")
    time.sleep(2)

def pc_game_part(player1, player2, card_desk):
    print(f"{player2.name} started game!")
    while True:
        taken_card = card_desk.take_card()
        player2.take_card(taken_card)
        if player2.points_have() > 21:
            print(f"\n{player2.name} has more than 21 points. It lost the round!\n")
            player2.show_cards()
            player1.add_victory()
            return
        else:
            if player2.points_have() >= player1.points_have():
                print("\nRound results:\n")
                print(f"{player1.name} has {player1.points_have()} points")
                player1.show_cards()
                print(f"\n{player2.name} has {player2.points_have()} points")
                player2.show_cards()
                print(f"\n{player2.name} won the round!")
                player2.add_victory()
                return
