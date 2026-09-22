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
            print("play")
            break
        elif selected_menu_option == "2":
            stats_menu()
            break
        elif selected_menu_option == "3":
            print("config")
            break
        elif selected_menu_option == "4":
            print("quit")
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


# MARK: Blackjack constants
SUITS = ["♠", "♥", "♦", "♣"] # ooh fancy unicode thanks to https://en.wikipedia.org/wiki/Playing_cards_in_Unicode
RANKS = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

# MARK: Blackjack variables
deck = []

# MARK: Blackjack subroutines
def build_deck():
    print("uhhhhhh")

# Run the damn thing
if __name__ == "__main__":
    main_menu()