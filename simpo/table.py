import json
from player import Player
from deck import Deck


class Table:

    def __init__(self):
        self.__read_config__()
        self.__init__seats()
        self.button = self.conf["button"]
        self.big_blind_amount = self.conf["big_blind_amount"]
        self.small_blind_amount = self.conf["small_blind_amount"]
        self.rake = self.conf["rake"]
        self.deck = Deck()
        self.pot = 0


    def __init__seats(self):
        self.seats = []
        for player in range(1, 11):
            try:
                conf = self.conf["seats"][str(player)]
                if not conf:
                    self.seats.append(None)
                else:
                    self.seats.append(Player(conf, table=self))
            except:
                self.seats.append(None)


    def __read_config__(self):
        self.conf = json.loads(open("table_config.json").read())        

    def take_blinds(self):
        button = int(self.button)
        current_seat = button
        small_blind_taken = False
        big_blind_taken = False
        while not big_blind_taken:
            current_seat = current_seat + 1 
            if current_seat == 11:
                current_seat = 1
            if self.seats[current_seat]:
                if small_blind_taken:
                    self.pot = self.pot + self.seats[current_seat].take_money(self.big_blind_amount)
                    big_blind_taken = True
                else:
                    self.pot = self.pot + self.seats[current_seat].take_money(self.small_blind_amount)
                    small_blind_taken = True
            

    def deal(self):
        self.take_blinds()
        self.deck.new_deck()
        for card in range(0, 2):
            for player in self.seats:
                if player:
                    player.accept_card(self.deck.get_card())
    

        

    
    


if __name__ == "__main__":
    t = Table()
    t.take_blinds()
    #print t.pot
    t.deal()
    #print t.seats
    
