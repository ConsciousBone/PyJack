# ░█▀█░█░█░▀▀█░█▀█░█▀▀░█░█░
# ░█▀▀░░█░░░░█░█▀█░█░░░█▀▄░
# ░▀░░░░▀░░▀▀░░▀░▀░▀▀▀░▀░▀░
# PyJack - Blackjack but in a single Python file!
# Created by @consciousbone for Hack Club Stardance
# ASCII art from https://www.asciiart.eu/text-to-ascii-art

# Imports
import os

# Consts
PYJACK_VERSION = 0

# General subroutines
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

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
    os.system('cls' if os.name == 'nt' else 'clear')
    print_ascii_logo(page_name)


def main_menu():
    menu_header("Main menu")


# Run the damn thing
if __name__ == "__main__":
    main_menu()