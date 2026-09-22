# ░░░░░░░░░░░░░░░░░░░░░░░░░
# ░█▀█░█░█░▀▀█░█▀█░█▀▀░█░█░
# ░█▀▀░░█░░░░█░█▀█░█░░░█▀▄░
# ░▀░░░░▀░░▀▀░░▀░▀░▀▀▀░▀░▀░
# ░░░░░░░░░░░░░░░░░░░░░░░░░
# PyJack - Blackjack but in a single Python file!
# Created by @consciousbone for Hack Club Stardance
# ASCII art from https://www.asciiart.eu/text-to-ascii-art

# MARK: Imports
import os
import random

# MARK: General constants
PYJACK_VERSION = 0

# MARK: General variables
menu_error_header = ""

# MARK: General subroutines
def clear():
    os.system('cls' if os.name == 'nt' else 'clear') # clear terminal

def print_ascii_logo(page_name):
    print(f'''
░░░░░░░░░░░░░░░░░░░░░░░░░
░█▀█░█░█░▀▀█░█▀█░█▀▀░█░█░
░█▀▀░░█░░░░█░█▀█░█░░░█▀▄░
░▀░░░░▀░░▀▀░░▀░▀░▀▀▀░▀░▀░
░░░░░░░░░░░░░░░░░░░░░░░░░
PyJack (v{PYJACK_VERSION})
{page_name}

─────────────────────────
''')

# MARK: Menu subroutines
def menu_header(page_name):
    global menu_error_header # let this subroutine use that var

    clear() # very clean very fancy very wow
    print_ascii_logo(page_name)

    if menu_error_header != "": # theres an error which needs showing, do it!
        print(f"{menu_error_header}\n")
        menu_error_header = "" # clear it to ensure it doesn't keep showing


def main_menu():
    while True:
        global menu_error_header # let this subroutine use that var
        menu_header("Main menu")
        print('''\
1) Play
2) Stats
3) Config
4) Quit
        ''')

        selected_menu_option = input("Select an option.\n> ") # get input
        if selected_menu_option == "1":
            play_blackjack()
            break
        elif selected_menu_option == "2":
            stats_menu()
            break
        elif selected_menu_option == "3":
            config_menu()
            break
        elif selected_menu_option == "4":
            print("Thanks for playing!")
            break
        else:
            menu_error_header = "Invalid option."

def stats_menu():
    while True:
        global menu_error_header
        menu_header("Stats")

        print("Coming soon!\n")

        print('''\
1) Back
            ''')

        selected_menu_option = input("Select an option.\n> ")
        if selected_menu_option == "1":
            main_menu()
            break
        else:
            menu_error_header = "Invalid option."

def config_menu():
    while True:
        global menu_error_header
        menu_header("Config")

        print("Coming soon!\n")

        print('''\
1) Back
            ''')

        selected_menu_option = input("Select an option.\n> ")
        if selected_menu_option == "1":
            main_menu()
            break
        else:
            menu_error_header = "Invalid option."


# MARK: Blackjack constants
SUITS = ["♠", "♥", "♦", "♣"] # ooh fancy unicode thanks to https://en.wikipedia.org/wiki/Playing_cards_in_Unicode
RANKS = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

# MARK: Blackjack variables
deck = []
player = []
dealer = []

# MARK: Blackjack subroutines/functions
def build_deck():
    deck.clear() # make sure deck doesn't end up massive
    for suit in SUITS:
        for rank in RANKS:
            deck.append((rank, suit))
    random.shuffle(deck)

def hand_value(hand):
    value = 0
    aces = 0

    for rank, suit in hand:
        if rank in ["J", "Q", "K"]: # handle the cards that aren't numbers, aces come later
            value += 10
        elif rank == "A": # now handle aces part 1; default to 11, but will move to 1 later if it would cause a bust
            value += 11
            aces += 1 # keep track of number of aces for later
        else:
            value += int(rank) # ez

    while value > 21 and aces > 0: # handle aces part 2; turn aces one by one from 11 to 1
        value -= 10
        aces -= 1

    return value # finished counting!

def show_hand(name, hand, hide_first_card=False):
    if hide_first_card: # hide the first card, used with dealer
        cards = ["??"] + [f"{rank}{suit}" for rank, suit in hand[1:]] # skip first card since it's hidden
        print(f"{name}: {' '.join(cards)}") # make sure cards are formatted nicely
    else:
        cards = [f"{rank}{suit}" for rank, suit in hand]
        print(f"{name}: {' '.join(cards)} ({hand_value(hand)})") # also show hand value for player


def play_blackjack(): # the main event 0.0
    build_deck() # get a deck
    menu_header("Play")

    player = [deck.pop(), deck.pop()] # give player 2 cards
    dealer = [deck.pop(), deck.pop()] # give dealer 2 cards

    show_hand("Dealer", dealer, hide_first_card=True) # show dealer's hand, hiding first card
    show_hand("Player", player) # show player's hand, ofc not hiding your own cards :/

# Run the damn thing
if __name__ == "__main__":
    main_menu()