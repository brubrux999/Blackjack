from random import shuffle
from player import Player
from deck import Deck

class BlackjackGame:
    def __init__(self):
        self.players = []
        self.dealer = Player("Dealer")
        self.deck = Deck()
    
    def dealing_cards(self):
        shuffle(self.deck.cards)

        self.dealer.hand.clear() # Clear hands before dealing new cards
        self.dealer.num_hand.clear()
        self.dealer.hand.extend(self.deck.cards[0:2]) # Take the first two cards
        del self.deck.cards[0:2] # Remove those cards taken from deck

        for player in self.players:
            player.hand.clear()
            player.num_hand.clear()
            player.hand.extend(self.deck.cards[0:2])
            del self.deck.cards[0:2]
            player.hand_value() # Compute the hand value
    
    def players_to_play(self):
        num_players = 0
        while num_players < 1 or num_players > 4:
            num_players = int(input("Enter number of players (1-4): "))
            if num_players < 1 or num_players > 4:
                print("Invalid number of players!\n")
        return num_players

    def players_class(self):
        self.players
        num_players = self.players_to_play()
        for i in range(num_players):
            name = input(f"Enter name for Player {i+1}: ")
            self.players.append(Player(name))
        return self.players

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

        # Player turns
        for player in self.players:
            if player.blackjack == False:
                hit_stand = ""
                print(f"\n{player.name}'s turn:")
                while hit_stand != "s" and player.active:
                    hit_stand = input(f"Hit or Stand (h/s)? ")
                    if hit_stand == "h":
                        print(f"{player.name} hits")
                        player.take_a_card(self.deck)
                        player.show_player_hand()
                        if player.score > 21:
                            player.active = False
                            print(f"{player.name} busts")
        
        if all(not player.active for player in self.players):
            return print("All players busted, dealer wins\n")
                    
        # Dealer turn
        if any(player.active for player in self.players):
            print("Dealer reveals the hole card...")
            print(f"\n>> Dealer hand: {self.dealer.hand}, the score is {self.dealer.hand_value()}\n")
            while self.dealer.score < 17:
                print("The dealer draws a card")
                self.dealer.take_a_card(self.deck)
                print(f"\n>> Dealer hand: {self.dealer.hand}, the score is {self.dealer.hand_value()}\n")
                if self.dealer.score > 21:
                    for player in self.players:
                        if player.active:
                            player.wins += 1
                    return print("The dealer busts\n")

        self.compare_scores() # Victory conditions (if there was no bust)

    def start(self):
        print(
            "\n============================\n"
            "Welcome to Blackjack!! (S17)\n"
            "============================\n"
            
            "\n1) Play\n"
            "2) View wins\n"
            "3) Quit\n"
        )
        option = 0
        while option != 1 or option != 2 or option != 3:
            option = int(input("Select an option: "))
            if option == 1:
                self.players = self.players_class()
                print("\nGood luck!")
                self.play()
                play_again = "y"
                while play_again != "n":
                    play_again = input("Do you wanna play again(y/n)? ")
                    if play_again == "y":
                        self.play()
                    elif play_again == "n":
                        print("Thanks for playing!!\n")
                        print(
                            "\n============================\n"
                            "Welcome to Blackjack!! (S17)\n"
                            "============================\n"
                            
                            "\n1) Play\n"
                            "2) View wins\n"
                            "3) Quit\n"
                        )
                    else:
                        print("Invalid input!\n")
            elif option == 2:
                for player in self.players:
                    print(f">> Total {player.name} wins: {player.wins}")
            elif option == 3:
                break
            else:
                print("Invalid input!\n")