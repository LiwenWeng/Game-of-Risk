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
        clear_screen()
        

    def show_instructions(self):
        clear_screen()
        print("instructions")
        input()
        self.run()

    def exit_game(self):
        sys.exit()

