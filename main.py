############### Blackjack Project #####################

# Difficulty Normal 😎: Use all Hints below to complete the project.
# Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
# Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
# Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

# The deck is unlimited in size.
# There are no jokers.
# The Jack/Queen/King all count as 10.
# The the Ace can count as 11 or 1.
# Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# The cards in the list have equal probability of being drawn.
# Cards are not removed from the deck as they are drawn.
# The computer is the dealer.

##################### Hints #####################
import os
import random
from art import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


# Chooses card at random from "cards" list and returns it


def deal_cards(deck):
    dealt_card = random.choice(deck)
    return (dealt_card)


def card_hit(hand):
    hand.append(deal_cards(cards))

# Takes in a given score and checks if it's equal to 21; returns binary value


def check_blackjack(score, blackjack):
    if score == 21:
        blackjack = True
    else:
        blackjack = False
    return (blackjack)

# Adds value of cards in hand to score (ver1)


def count_score(score, hand):
    num_aces = 0
    score = 0
    for card in hand:
        if card == 11:
            num_aces += 1
        score += card
    if score > 21 and num_aces > 1:
        score -= ((num_aces-1)*10)
    # print(f"count_score - Number of aces: {num_aces}")
    # print(f"count_score - Hand: {hand} - Score: {score}")
    return (score)


# test_hand = [10, 10, 5]
# test_score = 0
# player_hand = [11, 10]
# dealer_hand = [10, 10]

# print(f"Testing - {count_score(test_score, test_hand)}")
start_new_game = True
while start_new_game == True:

    print(logo)

    player_hand = []
    dealer_hand = []

    player_score = 0
    dealer_score = 0

    player_blackjack = None
    dealer_blackjack = None

    # Initial deal

    for card in range(2):
        player_hand.append(deal_cards(cards))
        dealer_hand.append(deal_cards(cards))

    # gameplay loop
    keep_going = True
    while keep_going == True:
        player_score = count_score(player_score, player_hand)
        dealer_score = count_score(dealer_score, dealer_hand)

        player_blackjack = check_blackjack(player_score, player_blackjack)
        dealer_blackjack = check_blackjack(dealer_score, dealer_blackjack)

        print(
            f"Main loop - Your hand: {player_hand} - Your score: {player_score}\nDealer's first card: {dealer_hand[0]}")

        if player_blackjack == True or dealer_blackjack == True:
            print("Game over - blackjack")
            keep_going = False
        elif player_score > 21 or dealer_score > 21:
            print("Game over - bust")
            keep_going = False
        elif player_score < 21 or dealer_score < 16:
            hit_or_stay = input(
                "Would you like to take another card? (y/n): ").lower()
            if hit_or_stay == "y":
                os.system('clear')
                print(logo)
                player_hand.append(deal_cards(cards))
                player_score = count_score(player_score, player_hand)
            elif hit_or_stay == "n":
                player_score = count_score(player_score, player_hand)
                while dealer_score < 16:
                    dealer_hand.append(deal_cards(cards))
                    dealer_score = count_score(dealer_score, dealer_hand)
                    dealer_blackjack = check_blackjack(
                        dealer_score, dealer_blackjack)
                print("Dealer has score over 16")
                keep_going = False

    print("Final game state:")
    print(
        f"Your final hand: {player_hand} - your final score: {player_score} - blackjack: {player_blackjack}")
    print(
        f"Dealer's final hand: {dealer_hand} - dealer's final score: {dealer_score} - blackjack: {dealer_blackjack}")

    if dealer_blackjack == True:
        if player_blackjack == True:
            print("Blackjack - draw - dealer wins")
        elif player_blackjack == False:
            print("Blackjack - dealer wins")
    elif player_blackjack == True:
        print("Blackjack - player wins")
    elif player_blackjack == False:
        if player_score > 21:
            print("Player busts - dealer wins")
        elif player_score < 21:
            if dealer_score > 21:
                print("Dealer busts - player wins")
            elif dealer_score < 21:
                if player_score > dealer_score:
                    print("Higher score - player wins")
                else:
                    print("Higher score - dealer wins")

    new_game = input("Would you like to play again? (y/n): ").lower()

    if new_game == "n":
        os.system('clear')
        start_new_game = False
    else:
        os.system('clear')
# Hint 1: Go to this website and try out the Blackjack game:
#   https://games.washingtonpost.com/games/blackjack/
# Then try out the completed Blackjack project here:
#   http://blackjack-final.appbrewery.repl.run

# Hint 2: Read this breakdown of program requirements:
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
# Then try to create your own flowchart for the program.

# Hint 3: Download and read this flow chart I've created:
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

# Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
# 11 is the Ace.
#cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

# Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
#user_cards = []
#computer_cards = []

# Hint 6: Create a function called calculate_score() that takes a List of cards as input
# and returns the score.
# Look up the sum() function to help you do this.

# Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.

# Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().

# Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.

# Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.

# Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

# Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.

# Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

# Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.
