class Player:
    def __init__(self, conf, table=None):
        self.name = conf["name"]
        self.table = table
        self.stack = conf["stack"]
        self.cards = []

    def accept_card(self, card):
        self.cards.append(card)

    def take_money(self, amount):
        if amount > self.stack:
            return_amount = self.stack
            self.stack = 0
            return return_amount
        else:
            self.stack = self.stack - amount
            return amount
        


    def __repr__(self):
        return "Player({},  {},  {})".format(self.name, self.stack, self.cards)
