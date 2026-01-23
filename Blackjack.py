from random import shuffle

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.num_hand = []
        self.score = 0
        self.wins = 0

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

    def take_a_card(self, deck):
        self.hand.append(deck.cards[0]) # Add a card to player hand
        deck.cards.pop(0) # Remove that card from deck
        self.hand_value() # Recompute the hand value

class Deck():

    def __init__(self):
        self.cards = [
            "As", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K",
            "As", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K",
            "As", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K",
            "As", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K",
        ]

    def dealing_cards(self):
        shuffle(self.cards) # Shuffle the deck

        # Hands starts empty
        player1.hand.clear()
        dealer.hand.clear()
        player1.num_hand.clear()
        dealer.num_hand.clear()

        player1.hand.extend(self.cards[0:2]) # Take the first two cards
        del self.cards[0:2]      # Remove them from the deck

        dealer.hand.extend(self.cards[0:2])
        del self.cards[0:2]

        player1.hand_value() # Compute the player hand value

def show_some_cards():
        return f"\n>> Dealer hand: [{dealer.hand[0]}, ?], the score is {dealer.hand_value(dealer.hand[0:])}\n" \
                f">> {player1.name} hand: {player1.hand}, the score is {player1.score}\n"

def show_hole_cards():
        return f"\n>> Dealer hand: {dealer.hand}, the score is {dealer.hand_value()}\n" \
                f">> {player1.name} hand: {player1.hand}, the score is {player1.score}\n"

def compare_scores():
    if player1.score > dealer.score:
        player1.wins += 1
        return "The player wins\n"
    elif dealer.score > player1.score:
        return "The dealer wins\n"
    else:
        return "It's a push\n"

def play():
    blackjack = False

    print("\nThe dealer deals the cards...")
    deck.dealing_cards()
    print(show_some_cards())

    # Evaluate if there is blackjack
    dealer.score = dealer.hand_value()
    if dealer.score == 21:
        blackjack = True
        return print(
            f"Dealer hand: {dealer.hand}\n"
            "The dealer gets BLACKJACK!!\n"
        )
    elif player1.score == 21:
        blackjack = True
        player1.wins += 1
        return print("The player gets BLACKJACK!!\n")
    
    # Player turn
    hit_stand = ""
    while hit_stand != "s" and blackjack == False:
        hit_stand = input("Hit or Stand (h/s)? ")

        if hit_stand == "h":
            print("The player hits")
            player1.take_a_card(deck)
            print(show_some_cards())
            if player1.score > 21:
                return print("The player busts\n")
        # Dealer turn
        elif hit_stand == "s":
            print("Dealer reveals the hole card...")
            print(show_hole_cards())
            while dealer.score < 17:
                print("The dealer draws a card")
                dealer.take_a_card(deck)
                print(show_hole_cards())
                if dealer.score > 21:
                    player1.wins += 1
                    return print("The dealer busts\n")
        else:
            print("Invalid input!\n")

    return print(compare_scores()) # Victory conditions (if there was no bust)

# Menu game
def menu():
    return print(
        "\n============================\n"
        "Welcome to Blackjack!! (S17)\n"
        "============================\n"

        "\n1) Play\n"
        "2) View wins\n" # Future leaderboard feature
        "3) Quit\n"
    )

menu()

player1 = Player("Bruno")
dealer = Player("Dealer")

option = 0
while option != 1 or option != 2 or option != 3:
    option = int(input("Select an option: "))
    if option == 1:
        print("\nGood luck!")
        deck = Deck()
        play()
        play_again = "y"
        while play_again != "n":
            play_again = input("Do you wanna play again(y/n)? ")
            if play_again == "y":
                deck = Deck()
                play()
            elif play_again == "n":
                print("Thanks for playing!!\n")
                menu()
                break
            else:
                print("Invalid input!\n")
    elif option == 2:
        print(f"\n>> Total player wins: {player1.wins}\n")
    elif option == 3:
        break
    else:
        print("Invalid input!\n")