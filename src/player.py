class Player:
    def __init__(self, name, bankroll):
        self.name = name
        self.bankroll = bankroll # Total chips amount
        self.bet = 0 # Bet in each round
        self.insurance = 0
        self.hand = []
        self.num_hand = [] # Numeric representation of the hand
        self.score = 0
        self.blackjack = False # To know if the player has blackjack
        self.active = True # To know if the player is still in the game
        self.wins = 0 # Total wins of the player

    def reset_hand(self):
        self.bet = 0
        self.insurance = 0
        self.hand = []
        self.num_hand = []
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
            
            self.bet = float(input(f"Bet: $"))
            if self.bet <= 0:
                print("Bet must be a positive amount")
                continue

            if self.bet > self.bankroll:
                print("You don't have enough chips")
                continue

            if self.bankroll - self.bet == 0:
                print("ALL IN")

            self.bankroll -= self.bet
            return

    def hand_value(self):
        Ace = 0 # Card counter "As"
        self.num_hand.clear()

        for card in self.hand:
            if card == "A":
                As += 1
            elif card in ["J", "Q", "K"]:
                self.num_hand.append(10)
            else:
                self.num_hand.append(card)
        
        for x in range(Ace): # 11 or 1 value for "As" (if there is)
            if sum(self.num_hand) + 11 <= 21:
                self.num_hand.append(11)
            else:
                self.num_hand.append(1)

        self.score = sum(self.num_hand)
    
    def show_hand(self):
        print(f">> {self.name} hand: {self.hand}, the score is {self.score}")

    def take_cards(self, cards):
        if isinstance(cards, list):
            self.hand.extend(cards)
        else:
            self.hand.append(cards) # Add a card to player hand

    def play_turn(self, deck):
        if self.blackjack == False:
            hit_stand = ""
            print(f"\n{self.name}'s turn:")
            while hit_stand != "s" and self.active:
                hit_stand = input(f"Hit or Stand (h/s)? ")
                if hit_stand == "h":
                    print(f"{self.name} hits\n")
                    self.take_cards(deck.draw(1))
                    self.hand_value()
                    self.show_hand()
                    if self.score > 21:
                        self.active = False
                        print(f"{self.name} busts")

class Dealer(Player):
    def __init__(self):
        super().__init__("Dealer", 0)

    def play_turn(self, deck):
        print("Dealer reveals the hole card...")
        self.show_hand(1)
        self.hand_value(1)
        while self.score < 17:
            print("The dealer draws a card")
            self.take_cards(deck.draw(1))
            self.hand_value(1)
            self.show_hand(1)
            if self.score > 21:
                self.active = False
                return print("The dealer busts\n")
            
    def hand_value(self, option):
        As = 0 # Card counter "As"
        self.num_hand.clear()

        # Value of the first (visible) card
        if option == 0:
            if self.hand[0] == "A":
                return 11
            elif self.hand[0] in ["J", "Q", "K"]:
                return 10
            else:
                return self.hand[0]
            
        # Value of all cards
        if option == 1:
            for card in self.hand:
                if card == "A":
                    As += 1
                elif card in ["J", "Q", "K"]:
                    self.num_hand.append(10)
                else:
                    self.num_hand.append(card)
        
            for _ in range(As): # 11 or 1 value for "As" (if there is)
                if sum(self.num_hand) + 11 <= 21:
                    self.num_hand.append(11)
                else:
                    self.num_hand.append(1)

            self.score = sum(self.num_hand)

    def show_hand(self, option):
        if option == 0:
            print(f"\n>> Dealer hand: [{self.hand[0]}, ?], the score is {self.hand_value(0)}\n")
        if option == 1:
            print(f"\n>> Dealer hand: {self.hand}, the score is {self.score}\n")