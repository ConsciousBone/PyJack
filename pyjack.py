# ░░░░░░░░░░░░░░░░░░░░░░░░░
# ░█▀█░█░█░▀▀█░█▀█░█▀▀░█░█░
# ░█▀▀░░█░░░░█░█▀█░█░░░█▀▄░
# ░▀░░░░▀░░▀▀░░▀░▀░▀▀▀░▀░▀░
# ░░░░░░░░░░░░░░░░░░░░░░░░░
# PyJack - Blackjack but in a single Python file!
# Created by @consciousbone for Hack Club Stardance
# ASCII art from https://www.asciiart.eu/text-to-ascii-art

# Imports
import os

# Consts
PYJACK_VERSION = 0

# General subroutines
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
''')

def menu_header(page_name):
    clear()
    print_ascii_logo(page_name)


def main_menu():
    menu_header("Main menu")
    print('''\
1) Play Blackjack
2) Stats
3) Config
4) Quit
    ''')

    selected_menu_option = input("Select an option.\n> ") # get input
    if selected_menu_option == "1":
        print("play")
    elif selected_menu_option == "2":
        print("stats")
    elif selected_menu_option == "3":
        print("config")
    elif selected_menu_option == "4":
        print("quit")
    else:
        print("invalid")


# Run the damn thing
if __name__ == "__main__":
    main_menu()