class Player:
    def __init__(self, name, bankroll):
        self.name = name
        self.bankroll = bankroll # Total chips amount
        self.insurance = 0
        self.hands = []
        self.blackjack = False # To know if the player has blackjack
        self.active = True # To know if the player is still in the game
        self.wins = 0 # Total wins of the player

    def reset_values(self):
        for hand in self.hands:
            hand.cards.clear()
            hand.bet = 0
            hand.finished = False
        self.insurance = 0
        self.blackjack = False
        self.active = True

    def place_bet(self):
        while True:
            if self.bankroll <= 0:
                buyin = input("Has no chips left. Buy-in (y/n)?: ")
                if buyin == "y":
                    amount = float(input("$"))
                    self.bankroll = amount
                elif buyin == "n":
                    self.active = False
                    return
                else:
                    print("Invalid input")
                    continue

            self.hands[0].bet = float(input("Hand bet: $"))
            if self.hands[0].bet <= 0:
                print("Bet must be a positive amount")
                continue

            if self.hands[0].bet > self.bankroll:
                print("You don't have enough chips")
                continue

            if self.bankroll - self.hands[0].bet == 0:
                print("ALL IN")

            self.bankroll -= self.hands[0].bet
            return
    
    def show_hand(self):
        print(f">> {self.name} hand: {self.hands[0]}")

    def play_turn(self, deck):
        if self.blackjack == False:
            hit_stand = ""
            print(f"\n{self.name}'s turn:")
            while hit_stand != "s" and self.active:
                hit_stand = input(f"Hit or Stand (h/s)? ")
                if hit_stand == "h":
                    print(f"{self.name} hits\n")
                    self.hands[0].take_cards(deck.draw(1))
                    self.hands[0].value()
                    self.show_hand()
                    if self.hands[0].score > 21:
                        self.active = False
                        print(f"{self.name} busts")

class Dealer(Player):
    def __init__(self, hand):
        super().__init__("Dealer", 0)
        self.hand = hand

    def play_turn(self, deck):
        print("Dealer reveals the hole card...")
        print(self.hand(1))
        self.hand.value(1)
        while self.hand.score < 17:
            print("The dealer draws a card")
            self.hand.take_cards(deck.draw(1))
            self.hand.value(1)
            print(self.hand(1))
            if self.hand.score > 21:
                self.active = False
                return print("The dealer busts\n")
            
    def show_hand(self, option):
        if option == 0:
            print(self.hand(0))
        if option == 1:
            print(self.hand(1))