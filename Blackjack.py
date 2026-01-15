from random import shuffle

deck = [
    "As", 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10,
    "As", 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10,
    "As", 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10,
    "As", 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10,
]

player_hand = []
dealer_hand = []

def dealing_cards():
    shuffle(deck)

    player_hand.extend(deck[0:2]) # Take the first two cards
    del deck[0:2] # Remove those cards taken from deck

    dealer_hand.extend(deck[0:2])
    del deck[0:2]

    player_score = hand_value(player_hand) # Compute the hand value
    dealer_score = hand_value(dealer_hand)

    return player_score, dealer_score

def take_a_card(hand, score):
    hand.append(deck[0]) # Add a card to (player/dealer) hand
    deck.pop(0) # Remove that card from deck
    score = hand_value(hand)

    return score

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

def play():
    blackjack = False
    print("\nThe dealer deals the cards...\n")
    player_score, dealer_score = dealing_cards()
    show_hands(player_hand, player_score, [dealer_hand[0], "?"], hand_value([dealer_hand[0]]))
    
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
            player_score = take_a_card(player_hand, player_score)
            show_hands(player_hand, player_score, [dealer_hand[0], "?"], hand_value([dealer_hand[0]]))
            if player_score > 21:
                return print("The player busts\n")
        # Dealer turn
        elif hit_stand == "s":
            print("Dealer reveals the hole card...")
            show_hands(player_hand, player_score, dealer_hand, dealer_score)
            while dealer_score < 17:
                print("The dealer draws a card")
                dealer_score = take_a_card(dealer_hand, dealer_score)
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
        play()
        play_again = "y"
        while play_again != "n":
            play_again = input("Do you wanna play again(y/n)? ")
            if play_again == "y":
                # Reset hands and deck
                player_hand.clear()
                dealer_hand.clear()
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