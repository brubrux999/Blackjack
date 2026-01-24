from random import shuffle

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.num_hand = [] # Numeric representation of the hand
        self.score = 0
        self.blackjack = False # To know if the player has blackjack
        self.active = True # To know if the player is still in the game
        self.wins = 0 # Total wins of the player

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

    def show_player_hand(self):
        print(f">> {self.name} hand: {self.hand}, the score is {self.score}\n")

class Deck():

    def __init__(self):
        self.cards = [
            "As", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K",
            "As", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K",
            "As", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K",
            "As", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K",
        ]

    def dealing_cards(self):
        shuffle(self.cards)

        dealer.hand.clear() # Clear hands before dealing new cards
        dealer.num_hand.clear()
        dealer.hand.extend(self.cards[0:2]) # Take the first two cards
        del self.cards[0:2] # Remove those cards taken from deck

        for player in players:
            player.hand.clear()
            player.num_hand.clear()
            player.hand.extend(self.cards[0:2])
            del self.cards[0:2]
            player.hand_value() # Compute the hand value

def compare_scores():
    for player in players:
        if player.active and not player.blackjack:
            if player.score > dealer.score:
                player.wins += 1
                print(f"{player.name} wins\n")
            elif dealer.score > player.score:
                print(f"{player.name} loses\n")
            else:
                print(f"That's a push for {player.name}\n")
def play():

    print("\nThe dealer deals the cards...")
    deck.dealing_cards()
    print(f"\n>> Dealer hand: [{dealer.hand[0]}, ?], the score is {dealer.hand_value(dealer.hand[0:])}\n")
    for player in players:
        print(f">> {player.name} hand: {player.hand}, the score is {player.score}")

    # Evaluate if there is blackjack
    dealer.hand_value()
    if dealer.score == 21:
        return print(
            f"\nDealer hand: {dealer.hand}\n"
            "The dealer gets BLACKJACK!!\n"
        )

    elif any(player.score == 21 for player in players):
        for player in players:
            if player.score == 21:
                player.blackjack = True
                player.wins += 1
                print(f"\n{player.name} gets BLACKJACK!!\n")

    # Player turns
    for player in players:
        if player.blackjack == False:
            hit_stand = ""
            print(f"\n{player.name}'s turn:")
            while hit_stand != "s" and player.active:
                hit_stand = input(f"Hit or Stand (h/s)? ")
                if hit_stand == "h":
                    print(f"{player.name} hits")
                    player.take_a_card()
                    player.show_player_hand()
                    if player.score > 21:
                        player.active = False
                        print(f"{player.name} busts\n")
    
    if all(not player.active for player in players):
        return print("All players busted, dealer wins\n")
                
    # Dealer turn
    if any(player.active for player in players):
        print("Dealer reveals the hole card...")
        print(f"\n>> Dealer hand: {dealer.hand}, the score is {dealer.hand_value()}\n")
        while dealer.score < 17:
            print("The dealer draws a card")
            dealer.take_a_card()
            print(f"\n>> Dealer hand: {dealer.hand}, the score is {dealer.hand_value()}\n")
            if dealer.score > 21:
                for player in players:
                    if player.active:
                        player.wins += 1
                return print("The dealer busts\n")

    compare_scores() # Victory conditions (if there was no bust)

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

def players_to_play():
    num_players = 0
    while num_players < 1 or num_players > 4:
        num_players = int(input("Enter number of players (1-4): "))
        if num_players < 1 or num_players > 4:
            print("Invalid number of players!\n")
    return num_players

def players_class():
    players = []
    num_players = players_to_play()
    for i in range(num_players):
        name = input(f"Enter name for Player {i+1}: ")
        players.append(Player(name))
    return players

menu()

dealer = Player("Dealer")

option = 0
while option != 1 or option != 2 or option != 3:
    option = int(input("Select an option: "))
    if option == 1:
        players = players_class()
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
        for player in players:
            print(f"\n>> Total {player.name} wins: {player.wins}\n")
    elif option == 3:
        break
    else:
        print("Invalid input!\n")