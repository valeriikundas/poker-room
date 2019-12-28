import random

from gameplay.card import Card


class Deck:
    def __init__(self):
        self.free_deck = [Card(r, s) for r in Card.ranks for s in Card.suits]

    def get_random_card(self):
        card = random.choice(self.free_deck)
        self.free_deck.remove(card)
        return str(card)

    def get_random_hand(self):
        first = self.get_random_card()
        second = self.get_random_card()
        return (str(first), str(second))

    def __str__(self):
        return ",".join(self.free_deck)
