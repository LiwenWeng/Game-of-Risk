import sys
from colorama import Fore, Style
import pyfiglet
import readchar

from game import EventManager, State
from game.entities.player import Player
from game.constants import GAME_NAME
from game.utils import clear_screen, select_option, type_text, colored_text, print_colored
from game.utils.display import section_break

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
        ][self.main_menu()]()
    
    def main_menu(self) -> int:
        clear_screen()

        def show_menu_header(shoud_type_text: bool = False):
            print(logo)
            (type_text if shoud_type_text else print)(colored_text("Survive the Cyber Storm.", Fore.YELLOW))
            section_break(24)

        options = [
            { "text": "Start New Game", "color": Fore.GREEN },
            { "text": "Instructions", "color": Fore.YELLOW },
            { "text": "Exit", "color": Fore.RED },
        ]
        logo = colored_text(pyfiglet.figlet_format(self.game_name, font="small"), Fore.CYAN, Style.BRIGHT)

        show_menu_header(True)
        return select_option(options, show_menu_header)
    
    def start_new_game(self):
        # self.show_welcome_message()
        self.set_name()
        while not self.state.is_over:
            [
                self.handle_action,
                self.view_inventory,
                self.view_logs,
                self.end_day
            ][self.select_day_option()]()
        
    def show_welcome_message(self):
        clear_screen()

        type_text(f"Welcome to {colored_text('NetShield Inc.', Fore.MAGENTA)}, Operative.")
        type_text("Your onboarding is now complete. You've officially joined the frontline defense of one of the world's fastest-growing tech firms.")
        
        type_text(colored_text('\nAbout Us:', Fore.CYAN))
        type_text(f"{colored_text('NetShield Inc.', Fore.MAGENTA)} builds secure digital infrastructure for {colored_text('global clients', Fore.GREEN)}.")
        type_text(f"We pride ourselves on staying one step ahead of cyber threats — because in our world, {colored_text('one breach', Fore.RED)} is all it takes to fall.")
        
        type_text(colored_text('\nYour Role:', Fore.GREEN))
        type_text(f"You're our newest cybersecurity analyst. Your mission: {colored_text('assess, defend, adapt', Fore.CYAN)}.\n")
        type_text(colored_text("Balance your resources. Mitigate risks. Survive the cyber storm.\n", Fore.YELLOW))
        
    def set_name(self):
        type_text(f"{colored_text('Now give us your code name', Fore.CYAN)}: ", end='')
        self.player.set_name(input())

    def show_day_info(self):
        print_colored(f"Day {self.state.current_day} / {self.state.max_days}", Fore.CYAN, Style.BRIGHT)
        print_colored(f"Analyst: {self.player.name}", Fore.MAGENTA)
        print_colored(f"Asset Value: ${self.state.asset_value:,}", Fore.GREEN if self.state.asset_value > 0 else Fore.RED)
        print_colored(f"Risk Level: {self.state.risk_level}", Fore.YELLOW)

        if self.state.risk_level > 70:
            print_colored("⚠️  Critical risk! Immediate action required.", Fore.RED, Style.BRIGHT)
        elif self.state.risk_level > 40:
            print_colored("⚠️  Elevated risk. Proceed with caution.", Fore.YELLOW)
        else:
            print_colored("✅ Risk under control. Stay vigilant.", Fore.GREEN)
        section_break(40)

    def select_day_option(self):
        clear_screen()

        options = [
            { "text": "Take Action", "color": Fore.GREEN },
            { "text": "View Inventory", "color": Fore.CYAN },
            { "text": "View Logs", "color": Fore.MAGENTA },
            { "text": "End Day", "color": Fore.YELLOW },
        ]

        return select_option(options, self.show_day_info)
        
    def handle_action(self):
        ...

    def view_inventory(self):
        ...

    def view_logs(self):
        clear_screen()

        day = self.state.current_day
        max_day = self.state.current_day

        while True:
            clear_screen()
            self.state.view_logs(day)

            print_colored("\nPress Q to return", Fore.CYAN)
            print_colored("← Previous Day - Next Day →", Fore.CYAN)
            key = readchar.readkey()

            if key == readchar.key.RIGHT:
                day = (day % max_day) + 1
            elif key == readchar.key.LEFT:
                day = ((day - 2) % max_day) + 1
            elif key.lower() == 'q':
                break

    def end_day(self):
        self.state.advance_day()

    def show_instructions(self):
        clear_screen()
        input("instructions\n")
        self.run()

    def exit_game(self):
        sys.exit()
