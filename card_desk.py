import random
from Card import Card


class CardDesk:

    def __init__(self):
        self.cards = CardDesk.create_card_desk()

    def create_card_desk():
        desk_card = []
        for s in Card.suits:
            for r in Card.ranks:
                desk_card.append(Card(s, r))
        return desk_card

    def shuffle_desk(self):
        random.shuffle(self.cards, random.random)

    def take_card(self):
        return self.cards.pop()

    def show_left_cards(self):
        return self.cards

    def __len__(self):
        return len(self.cards)
