from player import Player , Dealer
from deck import Deck
from menu import Menu

class BlackjackGame:
    def __init__(self):
        self.players = []
        self.dealer = Dealer()
        self.deck = Deck()
        self.menu = Menu()
    
    def new_round(self):
        self.deck = Deck()

        for player in self.players:
            player.reset_hand()

        self.dealer.active = True
        self.dealer.reset_hand()

    def add_player(self):
        self.players = []
        num_players = 0
        while num_players < 1 or num_players > 4:
            num_players = int(input("Enter number of players (1-4): "))
            if num_players < 1 or num_players > 4:
                print("Invalid number of players!\n")
        for i in range(num_players):
            name = input(f"Enter name for Player {i+1}: ")
            self.players.append(Player(name))
    
    def dealing_cards(self):
        self.dealer.take_cards(self.deck.draw(2)) # Take the first two cards

        for player in self.players:
            player.take_cards(self.deck.draw(2)) # Each player take two cards

    def check_blackjak(self):
        # Evaluate if dealer has blackjack
        self.dealer.hand_value()
        if self.dealer.score == 21:
            print(
                f"\nDealer hand: {self.dealer.hand}\n"
                "The dealer gets BLACKJACK!!\n"
            )
            for player in self.players:
                player.bankroll -= player.bet
                print(f"{player.name} lose the bet")
            return True
        
        # Evaluate if any player have blackjack
        else:
            for player in self.players:
                if player.score == 21:
                    player.blackjack = True
                    player.wins += 1
                    player.bankroll += player.bet + (player.bet * 1.5) # Payout 3:2
                    print(f"{player.name} gets BLACKJACK!! - pays 3:2\n")
            return False

    def compare_scores(self):
        for player in self.players:
            # for those players who are still playing
            if player.active and not player.blackjack:
                if player.score > self.dealer.score:
                    player.bankroll += player.bet * 2 # Payout 1:1
                    player.wins += 1
                    print(f"{player.name} wins even money\n")
                elif self.dealer.score > player.score:
                    print(f"{player.name} loses")
                else:
                    player.bankroll += player.bet
                    print(f"That's a push for {player.name}\n")
            player.active = False
    
    def play(self):
        print("Place your bets:\n")
        for player in self.players:
            print(f">> {player.name} bankroll: ${player.bankroll}")
            player.place_bet()
        print("\nGood luck, the dealer deals the cards...")
        self.dealing_cards()

        print(f"\n>> Dealer hand: [{self.dealer.hand[0]}, ?], the score is {self.dealer.hand_value(self.dealer.hand[0:])}\n")
        for player in self.players:
            player.show_hand()

        if self.check_blackjak():
            return # Ends the game just if dealer has blackjack

        # Players turn
        for player in self.players:
            player.play_turn(self.deck)
        
        if all(not player.active for player in self.players):
            return print("All players busted, dealer wins\n")
                    
        # Dealer turn
        if any(player.active for player in self.players):
            self.dealer.play_turn(self.deck)
            if self.dealer.active == False:
                for player in self.players:
                    if player.active == True:
                        player.wins += 1
            else:
                self.compare_scores() # Victory conditions (if there was no bust)

    def start(self):
        print(self.menu.show)
        option = 0
        while option != 1 or option != 2 or option != 3:
            option = int(input("Select an option: "))
            if option == 1:
                self.add_player()
                self.new_round()
                self.play()

                play_again = "y"
                while play_again != "n":
                    play_again = input("Do you wanna play again(y/n)? ")
                    if play_again == "y":
                        self.new_round()
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