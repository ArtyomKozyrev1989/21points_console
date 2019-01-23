class Card:

    suits = ("Club", "Diamond", "Heart", "Spade")
    ranks = ("Ace", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King")
    points_dict = {"Ace": 11, "Six": 6, "Seven": 7, "Eight": 8, "Nine": 9,
                   "Ten": 10, "Queen": 3, "Jack": 2, "King": 4}

    def __init__(self, suit, rank):
        if suit not in Card.suits:
            raise ValueError("You put incorrect suit type!")
        else:
            self.suit = suit

        if rank not in Card.ranks:
            raise ValueError("You put incorrect suit type!")
        else:
            self.rank = rank

        self.points = Card.points_dict[self.rank]

    def __str__(self):
        return f"{self.rank} {self.suit} gives {self.points} points"
