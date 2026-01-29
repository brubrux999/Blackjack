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
            bankroll = float(input("Buy-in amount: $"))
            self.players.append(Player(name, bankroll))
    
    def dealing_cards(self):
        print("\nGood luck, the dealer deals the cards...")
        self.dealer.take_cards(self.deck.draw(2)) # Take the first two cards

        for player in self.players:
            player.take_cards(self.deck.draw(2)) # Each player take two cards
            player.hand_value() # Compute the value of the hand

    def check_blackjack(self):
        # Evaluate if any player have blackjack
        for player in self.players:
            if player.score == 21:
                player.blackjack = True
                print(f"{player.name} gets BLACKJACK!!")
    
        # Evaluate if dealer has blackjack
        self.dealer.hand_value(1)
        if any(card in ["A", "J", "Q", "K"] for card in self.dealer.hand):
            
            # Peak rule
            if self.dealer.hand[0] in ["J", "Q", "K"] and self.dealer.hand[1] == "A":
                print(
                    f"\nDealer hand: {self.dealer.hand}\n"
                    "The dealer gets BLACKJACK!!\n"
                )
                for player in self.players:
                    if player.blackjack == False:
                        print(f"{player.name} lose the bet")
                    else:
                        player.bankroll += player.bet
                        print(f"It's a push for {player.name}")
                return True
            
            # Insurance
            if self.dealer.hand[0] == "A":
                print("\nDealer shows Ace. Insurance (y/n)?")
                for player in self.players:
                    insurance = input(f">> {player.name}: ")
                    if insurance == "y":
                        player.insurance = float(input(f"(max amount: ${player.bet / 2}) $"))
                        player.bankroll -= player.insurance
                    elif insurance == "n":
                        pass
                if self.dealer.hand[1] in ["J", "Q", "K"]:
                    print(
                        f"\nDealer hand: {self.dealer.hand}\n"
                        "BLACKJACK!! - Insurance pays 2:1\n"
                    )
                    for player in self.players:
                        player.bankroll += player.insurance * 2 # Insurance payout 2:1
                    return True
                
            return False
                
        # Player wins if has blackjack and dealer doesn't
        else:
            for player in self.players:
                if player.blackjack == True:
                    player.wins += 1
                    player.bankroll += player.bet + (player.bet * 1.5) # Payout 3:2
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

        self.dealing_cards()

        self.dealer.show_hand(0)
        for player in self.players:
            player.show_hand()

        if self.check_blackjack():
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
                        player.bankroll += player.bet * 2
                        player.wins += 1
            else:
                self.compare_scores() # Victory conditions (if there was no bust)

    def start(self):
        print(self.menu.show)
        option = 0
        while option != 1 or option != 2 or option != 3:
            option = int(input("Select an option: "))
            # Play option
            if option == 1:
                self.add_player()
                self.new_round()
                self.play()

                # Play again
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

            # View wins (future leaderboard csv)
            elif option == 2:
                for player in self.players:
                    print(f">> Total {player.name} wins: {player.wins}")
            # Quit
            elif option == 3:
                break
            else:
                print("Invalid input!\n")