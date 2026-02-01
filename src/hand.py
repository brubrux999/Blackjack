class PlayerHand():
    def __init__(self):
        self.cards = []
        self.num_cards = [] # Numeric representation of the hand
        self.score = 0
        self.bet = 0 # Bet for each round
        self.finished = False
    
    def __str__(self):
        return f"{self.cards} the score is {self.score}"
    
    def take_cards(self, cards):
        if isinstance(cards, list):
            self.cards.extend(cards)
        else:
            self.cards.append(cards) # Add a card to player hand

    def value(self):
        Ace = 0 # Card counter "Ace"
        self.num_cards.clear()

        for card in self.cards:
            if card == "A":
                Ace += 1
            elif card in ["J", "Q", "K"]:
                self.num_cards.append(10)
            else:
                self.num_cards.append(card)
        
        for x in range(Ace): # 11 or 1 value for "As" (if there is)
            if sum(self.num_cards) + 11 <= 21:
                self.num_cards.append(11)
            else:
                self.num_cards.append(1)

        self.score = sum(self.num_cards)

class DealerHand(PlayerHand):
    def __init__(self):
        super().__init__()

    def __call__(self, option=None):
        if option == 0:
            return f"\n>> Dealer hand: [{self.cards[0]}, ?] the score is {self.value(0)}\n"
        elif option == 1:
            return f"\n>> Dealer hand: {self.cards} the score is {self.score}\n"

    def value(self, option):
        Ace = 0 # Card counter "As"
        self.num_cards.clear()

        # Value of the first (visible) card
        if option == 0:
            if self.cards[0] == "A":
                return 11
            elif self.cards[0] in ["J", "Q", "K"]:
                return 10
            else:
                return self.cards[0]
            
        # Value of all cards
        if option == 1:
            for card in self.cards:
                if card == "A":
                    As += 1
                elif card in ["J", "Q", "K"]:
                    self.num_cards.append(10)
                else:
                    self.num_cards.append(card)
        
            for _ in range(Ace): # 11 or 1 value for "As" (if there is)
                if sum(self.num_cards) + 11 <= 21:
                    self.num_cards.append(11)
                else:
                    self.num_cards.append(1)

            self.score = sum(self.num_cards)