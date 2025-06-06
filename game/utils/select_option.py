from typing import Callable
from colorama import Fore, Style
import readchar

from game.utils.display import print_colored
from game.utils.system import clear_screen

def select_option(options: list[dict], render_header: Callable[[], None] = lambda: None, *args) -> int:
    selected = 0

    while True:
        clear_screen()
        render_header(*args)

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