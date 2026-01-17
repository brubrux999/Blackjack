from random import shuffle

# Hands to display
player_hand = []
dealer_hand = []
# Hands to compute values (without str values)
phand = []
dhand = []
# Scores
player_score = []
dealer_score = []

def dealing_cards():
    shuffle(deck)

    # Hands starts empty
    player_hand.clear()
    dealer_hand.clear()
    phand.clear()
    dhand.clear()

    player_hand.extend(deck[0:2]) # Take the first two cards
    del deck[0:2] # Remove those cards taken from deck

    dealer_hand.extend(deck[0:2])
    del deck[0:2]

    player_score.append(hand_value(player_hand, phand, player_score)) # Compute the hand value
    dealer_score.append(hand_value([dealer_hand[0]], dhand, dealer_score))

    return

def take_a_card(hand, pd_hand, score):
    hand.append(deck[0]) # Add a card to (player/dealer) hand
    deck.pop(0) # Remove that card from deck
    hand_value(hand, pd_hand, score) # Recompute the hand value

    return 

def hand_value(hand, pd_hand, score):
    As = 0 # Card counter "As"
    pd_hand.clear()
    score.clear()

    for card in hand:
        if card == "As":
            As += 1
        else:
            pd_hand.append(card)
    
    for x in range(As): # 11 or 1 value for "As" (if there is)
        if sum(pd_hand) + 11 <= 21:
            pd_hand.append(11)
        else:
            pd_hand.append(1)

    return score.append(sum(pd_hand))

def show_hands(dealer_hand, dealer_score):
        return f"\n>> Dealer hand: {dealer_hand}, the score is {dealer_score[0]}\n" \
                f">> Your hand: {player_hand}, the score is {player_score[0]}\n"

def compare_scores(player_score, dealer_score):
    if player_score[0] > dealer_score[0]:
        return "The player wins\n"
    elif dealer_score[0] > player_score[0]:
        return "The dealer wins\n"
    else:
        return "It's a push\n"

def play():
    blackjack = False
    print("\nThe dealer deals the cards...")
    dealing_cards()
    print(show_hands([dealer_hand[0], "?"], dealer_score))
    
    # Evaluate if there is blackjack
    hand_value(dealer_hand, dhand, dealer_score)
    if dealer_score[0] == 21:
        blackjack = True
        return print(
            f"Dealer hand: {dealer_hand}\n"
            "The dealer gets BLACKJACK!!\n"
        )
    elif player_score[0] == 21:
        blackjack = True
        return print("The player gets BLACKJACK!!\n")
    
    # Player turn
    hit_stand = ""
    while hit_stand != "s" and blackjack == False:
        hit_stand = input("Hit or Stand (h/s)? ")

        if hit_stand == "h":
            print("The player hits")
            take_a_card(player_hand, phand, player_score)
            hand_value([dealer_hand[0]], dhand, dealer_score)
            print(show_hands([dealer_hand[0], "?"], dealer_score))
            if player_score[0] > 21:
                return print("The player busts\n")
        # Dealer turn
        elif hit_stand == "s":
            print("Dealer reveals the hole card...")
            hand_value(dealer_hand, dhand, dealer_score)
            print(show_hands(dealer_hand, dealer_score))
            while dealer_score[0] < 17:
                print("The dealer draws a card")
                take_a_card(dealer_hand, dhand, dealer_score)
                print(show_hands(dealer_hand, dealer_score))
                if dealer_score[0] > 21:
                    return print("The dealer busts\n")
        else:
            print("Invalid input!\n")

    return print(compare_scores(player_score, dealer_score)) # Victory conditions (if there was no bust)

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
        deck = [
            "As", 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10,
            "As", 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10,
            "As", 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10,
            "As", 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10,
        ] # Deck of cards
        play()
        play_again = "y"
        while play_again != "n":
            play_again = input("Do you wanna play again(y/n)? ")
            if play_again == "y":
                deck = [
                    "As", 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10,
                    "As", 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10,
                    "As", 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10,
                    "As", 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10,
                ] # Reset the deck
                play()
            elif play_again == "n":
                print("Thanks for playing!!\n")
                menu()
                break
            else:
                print("Invalid input!\n")
    elif option == 2:
        break
    elif option == 3:
        print("Seccion de prueba")
    else:
        print("Invalid input!\n")