from random import shuffle
from player import Player , Dealer
from deck import Deck
from menu import Menu

class BlackjackGame:
    def __init__(self):
        self.players = []
        self.dealer = Dealer()
        self.deck = Deck()
        self.menu = Menu()

    def add_player(self):
        num_players = 0
        while num_players < 1 or num_players > 4:
            num_players = int(input("Enter number of players (1-4): "))
            if num_players < 1 or num_players > 4:
                print("Invalid number of players!\n")
        for i in range(num_players):
            name = input(f"Enter name for Player {i+1}: ")
            self.players.append(Player(name))
    
    def dealing_cards(self):
        self.deck.create_suffle_deck # Reset the deck

        self.dealer.hand.clear() # Clear hands before dealing first cards
        self.dealer.num_hand.clear()
        self.dealer.take_cards(self.deck.draw(2)) # Take the first two cards

        for player in self.players:
            # Reset player properties
            player.active = True
            player.blackjack = False
            player.hand.clear()
            player.num_hand.clear()
            # Take two cards
            player.take_cards(self.deck.draw(2))

    def compare_scores(self):
        for player in self.players:
            if player.active and not player.blackjack:
                if player.score > self.dealer.score:
                    player.wins += 1
                    print(f"{player.name} wins\n")
                elif self.dealer.score > player.score:
                    print(f"{player.name} loses\n")
                else:
                    print(f"That's a push for {player.name}\n")
    
    def play(self):
        print("\nThe dealer deals the cards...")
        self.dealing_cards()
        print(f"\n>> Dealer hand: [{self.dealer.hand[0]}, ?], the score is {self.dealer.hand_value(self.dealer.hand[0:])}\n")
        for player in self.players:
            print(f">> {player.name} hand: {player.hand}, the score is {player.score}")

        # Evaluate if there is blackjack
        self.dealer.hand_value()
        if self.dealer.score == 21:
            return print(
                f"\nDealer hand: {self.dealer.hand}\n"
                "The dealer gets BLACKJACK!!\n"
            )

        elif any(player.score == 21 for player in self.players):
            for player in self.players:
                if player.score == 21:
                    player.blackjack = True
                    player.wins += 1
                    print(f"\n{player.name} gets BLACKJACK!!\n")

        # Players turn
        for player in self.players:
            player.play_turn(self.deck)
        
        if all(not player.active for player in self.players):
            return print("All players busted, dealer wins\n")
                    
        # Dealer turn
        if any(player.active for player in self.players):
            self.dealer.play_turn(self.deck)

        self.compare_scores() # Victory conditions (if there was no bust)

    def start(self):
        print(self.menu.show)
        option = 0
        while option != 1 or option != 2 or option != 3:
            option = int(input("Select an option: "))
            if option == 1:
                self.add_player()
                print("\nGood luck!")
                self.play()
                play_again = "y"
                while play_again != "n":
                    play_again = input("Do you wanna play again(y/n)? ")
                    if play_again == "y":
                        self.play()
                    elif play_again == "n":
                        print("Thanks for playing!!\n")
                        print(self.menu.show)
                    else:
                        print("Invalid input!\n")
            elif option == 2:
                for player in self.players:
                    print(f">> Total {player.name} wins: {player.wins}")
            elif option == 3:
                break
            else:
                print("Invalid input!\n")