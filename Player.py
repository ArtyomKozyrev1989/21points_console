class Player:


    def __init__(self, name):
        self.name = name
        self.cards_have = []
        self.victory_number = 0

    def points_have(self):
        sum_of_points = 0
        for i in self.cards_have:
            sum_of_points += i.points
        return sum_of_points

    def take_card(self, card):
        self.cards_have.append(card)
        print(f"{self.name} took card")
        print(card)
        print(f"{self.name} has {self.points_have()} points")

    def show_cards(self):
        print(f"{self.name} has the following cards: ")
        for i in self.cards_have:
            print(i)

    def add_victory(self):
        self.victory_number += 1

    def start_new_round(self):
        self.cards_have = []
