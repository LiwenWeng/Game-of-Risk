import sys
from colorama import Fore, Style
import pyfiglet
import readchar

from game import EventManager, State
from game.entities.player import Player
from game.constants import GAME_NAME
from game.utils import clear_screen, type_text, colored_text, print_colored

class Engine:
    def __init__(self):
        self.game_name = GAME_NAME
        self.state = State()
        self.player = Player()
        self.event_manager = EventManager()

    def run(self):
        [ 
            self.start_new_game, 
            self.show_instructions, 
            self.exit_game 
        ][self.menu()]()
    
    def menu(self) -> int:
        options = [
            { "text": "Start New Game", "color": Fore.GREEN },
            { "text": "Instructions", "color": Fore.YELLOW },
            { "text": "Exit", "color": Fore.RED },
        ]
        logo = colored_text(pyfiglet.figlet_format(self.game_name, font="small"), Fore.CYAN, Style.BRIGHT)
        selected = 0

        clear_screen()
        print(logo)
        type_text(colored_text("Survive the Cyber Storm.", Fore.YELLOW))

        while True:
            clear_screen()

            print(logo)
            print_colored("Survive the Cyber Storm.", Fore.YELLOW)
            print("------------------------\n")
            print_colored("Use ↑/↓ arrows and Enter to select:\n", style=Style.BRIGHT)

            for i, option in enumerate(options):
                prefix = "> " if i == selected else "   "
                color = option["color"] if i == selected else Fore.WHITE
                style = Style.BRIGHT if i == selected else Style.NORMAL
                print_colored(prefix + option["text"], color, style)

            key = readchar.readkey()
            if key == readchar.key.UP:
                selected = (selected - 1) % len(options)
            elif key == readchar.key.DOWN:
                selected = (selected + 1) % len(options)
            elif key == readchar.key.ENTER:
                return selected
    
    def start_new_game(self):
        self.show_welcome_message_and_set_name()
        

    def show_instructions(self):
        clear_screen()
        print("instructions")
        input()
        self.run()

    def exit_game(self):
        sys.exit()

    def show_welcome_message_and_set_name(self):
        clear_screen()
        type_text(f"Welcome to {colored_text('NetShield Inc.', Fore.MAGENTA)}, Operative.")
        type_text("Your onboarding is now complete. You've officially joined the frontline defense of one of the world's fastest-growing tech firms.")
        type_text(colored_text('\nAbout Us:', Fore.CYAN))
        type_text(f"{colored_text('NetShield Inc.', Fore.MAGENTA)} builds secure digital infrastructure for {colored_text('global clients', Fore.GREEN)}.")
        type_text(f"We pride ourselves on staying one step ahead of cyber threats — because in our world, {colored_text('one breach', Fore.RED)} is all it takes to fall.")
        type_text(colored_text('\nYour Role:', Fore.GREEN))
        type_text(f"You're our newest cybersecurity analyst. Your mission: {colored_text('assess, defend, adapt', Fore.CYAN)}.\n")
        type_text(colored_text("Balance your resources. Mitigate risks. Survive the cyber storm.\n", Fore.YELLOW))
        type_text(f"{colored_text('Now give us your code name', Fore.CYAN)}: ", end='')
        self.player.set_name(input())

    
