from random import shuffle

class Deck():
    def __init__(self):
        self.cards = self.create_suffle_deck()

    def create_suffle_deck(self):
        deck = [
            "As", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K",
            "As", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K",
            "As", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K",
            "As", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K",
        ]
        shuffle(deck)
        return deck

    def draw(self, n=int):
        draw = self.cards[:n] # Draw n-cards
        del self.cards[:n] # Remove them from deck
        return draw if n > 1 else draw[0]
