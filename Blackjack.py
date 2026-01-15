from random import shuffle

deck = [
    "As", 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10,
    "As", 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10,
    "As", 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10,
    "As", 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10,
]

def dealing_cards(deck):
    shuffle(deck)

    player_hand = deck[:2] # Take the first two cards
    deck = deck[2:] # Remove those cards taken from deck

    dealer_hand = deck[:2]
    deck = deck[2:]

    player_score = hand_value(player_hand) # Compute the hand value
    dealer_score = hand_value(dealer_hand)

    return player_hand, player_score, dealer_hand, dealer_score, deck

def take_a_card(hand, score, deck):
    hand.append(deck[0]) # Add a card to (player/dealer) hand
    deck.pop(0) # Remove that card from deck
    score = hand_value(hand)

    return hand, score, deck

def hand_value(hand):
    As = 0 # Card counter "As"
    score = 0

    for card in hand:
        if card == "As":
            As += 1
        else:
            score += card
    
    for x in range(As): # 11 or 1 value for "As" (if there is)
        if score + 11 <= 21:
            score += 11
        else:
            score += 1

    return score

def show_hands(player_hand, player_score, dealer_hand, dealer_score):
        return print(
            f"\n>> Dealer hand: {dealer_hand}, the score is {dealer_score}\n"
            f">> Your hand: {player_hand}, the score is {player_score}\n"
            )
        
def compare_scores(player_score, dealer_score):
    if player_score > dealer_score:
        return print("The player wins")
    elif dealer_score > player_score:
        return print("The dealer wins")
    else:
        return print("It's a push")

def play(deck):
    blackjack = False
    print("\nThe dealer deals the cards...\n")
    player_hand, player_score, dealer_hand, dealer_score, deck = dealing_cards(deck)
    print(
        f">> Dealer hand: [{dealer_hand[0]}, ?], the score is {hand_value([dealer_hand[0]])}\n"
        f">> Your hand: {player_hand}, the score is {player_score}\n"
    )
    
    # Evaluate if there is blackjack
    if dealer_score == 21:
        blackjack = True
        print(
            f"Dealer hand: {dealer_hand}\n"
            "The dealer gets BLACKJACK!!\n"
        )
        return
    elif player_score == 21:
        blackjack = True
        return print("The player gets BLACKJACK!!\n")
    
    # Player turn
    hit_stand = ""
    while hit_stand != "s" and blackjack == False:
        hit_stand = input("Hit or Stand (h/s)? ")

        if hit_stand == "h":
            print("The player hits")
            player_hand, player_score, deck = take_a_card(player_hand, player_score, deck)
            show_hands(player_hand, player_score, [dealer_hand[0], "?"], dealer_score)
            if player_score > 21:
                return print("The player busts\n")
        elif hit_stand == "s": # Dealer turn
            print("Dealer reveals the hole card...")
            show_hands(player_hand, player_score, dealer_hand, dealer_score)
            while dealer_score < 17:
                print("The dealer draws a card")
                dealer_hand, dealer_score, deck = take_a_card(dealer_hand, dealer_score, deck)
                show_hands(player_hand, player_score, dealer_hand, dealer_score)
                if dealer_score > 21:
                    return print("The dealer busts\n")
        else:
            print("Invalid input!\n")

    return compare_scores(player_score, dealer_score) # Victory conditions (if there was no bust)

# Menu game
def menu():
    return print(
        "\n============================\n"
        "Welcome to Blackjack!! (S17)\n"
        "============================\n"

        "\n1) Play\n"
        "2) Quit\n"
    )

menu()

option = 0
while option != 1 or option != 2 or option != 3:
    option = int(input("Select an option: "))
    if option == 1:
        print("\nGood luck!")
        play(deck)
        play_again = "y"
        while play_again != "n":
            play_again = input("Do you wanna play again(y/n)? ")
            if play_again == "y":
                play(deck)
            elif play_again == "n":
                menu()
                break
            else:
                print("Invalid input!\n")
    elif option == 2:
        break
    else:
        print("Invalid input!\n")