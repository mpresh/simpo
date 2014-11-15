import itertools, random


class Deck:
    
    def __init__(self):
        self.new_deck()

    def new_deck(self):
        self.deck = list(itertools.product(range(2,15),['Spade','Heart','Diamond','Club']))
        random.shuffle(self.deck)

    def get_card(self):
        card = self.deck.pop()
        return card

    def flop(self):
        burn_card = self.get_card()
        cards = []
        cards.append(self.get_card)
        cards.append(self.get_card)
        cards.append(self.get_card)
        return cards

    def turn(self):
        burn_card = self.get_card()
        cards = []
        cards.append(self.get_card)
        return cards

    def river(self):
        burn_card = self.get_card()
        cards = []
        cards.append(self.get_card)
        return cards

if __name__ == "__main__":
    deck = Deck()
    while len(deck.deck):
        print deck.get_card(), len(deck.deck)
