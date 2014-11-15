import json
from player import Player
from deck import Deck


class Table:

    def __init__(self):
        self.__read_config__()
        self.__init__seats()
        self.button = self.conf["button"]
        self.big_blind = self.conf["big_blind"]
        self.small_blind = self.conf["small_blind"]
        self.rake = self.conf["rake"]
        self.deck = Deck()


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

    def deal(self):
        self.deck.new_deck()
        for card in range(0, 2):
            for player in self.seats:
                if player:
                    player.accept_card(self.deck.get_card())
    

        

    
    


if __name__ == "__main__":
    t = Table()
    t.deal()
    print t.seats
    
