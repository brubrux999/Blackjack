class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.num_hand = [] # Numeric representation of the hand
        self.score = 0
        self.blackjack = False # To know if the player has blackjack
        self.active = True # To know if the player is still in the game
        self.wins = 0 # Total wins of the player

    def reset_hand(self):
        self.hand = []
        self.num_hand = []
        self.blackjack = False
        self.active = True

    def hand_value(self, hand=None):
        As = 0 # Card counter "As"
        hand = [self.hand[0]] if hand is not None else self.hand
        self.num_hand.clear()

        for card in hand:
            if card == "As":
                As += 1
            elif card in ["J", "Q", "K"]:
                self.num_hand.append(10)
            else:
                self.num_hand.append(card)
        
        for x in range(As): # 11 or 1 value for "As" (if there is)
            if sum(self.num_hand) + 11 <= 21:
                self.num_hand.append(11)
            else:
                self.num_hand.append(1)

        self.score = sum(self.num_hand)
        return self.score
    
    def show_hand(self):
        print(f">> {self.name} hand: {self.hand}, the score is {self.score}")

    def take_cards(self, cards):
        if isinstance(cards, list):
            self.hand.extend(cards)
            self.hand_value()
        else:
            self.hand.append(cards) # Add a card to player hand
            self.hand_value() # Recompute the hand value

    def play_turn(self, deck):
        if self.blackjack == False:
            hit_stand = ""
            print(f"\n{self.name}'s turn:")
            while hit_stand != "s" and self.active:
                hit_stand = input(f"Hit or Stand (h/s)? ")
                if hit_stand == "h":
                    print(f"{self.name} hits")
                    self.take_cards(deck.draw(1))
                    self.show_hand()
                    if self.score > 21:
                        self.active = False
                        print(f"{self.name} busts")

class Dealer(Player):
    def __init__(self):
        super().__init__("Dealer")

    def play_turn(self, deck):
        print("Dealer reveals the hole card...")
        print(f"\n>> Dealer hand: {self.hand}, the score is {self.hand_value()}\n")
        while self.score < 17:
            print("The dealer draws a card")
            self.take_cards(deck.draw(1))
            print(f"\n>> Dealer hand: {self.hand}, the score is {self.hand_value()}\n")
            if self.score > 21:
                self.active = False
                return print("The dealer busts\n")