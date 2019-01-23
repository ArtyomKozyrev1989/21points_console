from card_desk import CardDesk
from Player import Player
import Game
import time
import os


def main():
    global play_round
    while play_round:
        cards = CardDesk()
        cards.shuffle_desk()
        taken_card = cards.take_card()
        player1.take_card(taken_card)
        while True:
            if not Game.do_want_another_card():
                break
            taken_card = cards.take_card()
            player1.take_card(taken_card)
            if not Game.check_if_less_21(player1):
                print(f"\n{player1.name} has more than 21 points. You lost the round! \n")
                player1.show_cards()
                player2.add_victory()
                break
        if Game.check_if_less_21(player1):
            Game.pc_game_part(player1, player2, cards)
        if Game.do_want_another_game():
            player1.start_new_round()
            player2.start_new_round()
            os.system("cls")
            print("New round started!")
        else:
            Game.check_who_win_series(player1, player2)
            Game.goodbye()
            play_round = False


if __name__ == "__main__":
    Game.welcome()
    player1_name = Game.choose_player_name()
    player1 = Player(player1_name)
    player2 = Player("PC")
    play_round = True
    try:
        main()
    except Exception as ex:
        print(f"The following problem happened in the program:  {ex}")
        print("The program will be terminated in 10 seconds")
        time.sleep(10)
