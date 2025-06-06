import time
from colorama import Style, Fore

def type_text(text, delay=0.03, end="\n"):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)

    if end == "\n":
        print()

def colored_text(text: str, color: str = Fore.WHITE, style: str = Style.NORMAL):
    return f"{style}{color}{text}{Style.RESET_ALL}"

def print_colored(text: str, color: str = Fore.WHITE, style: str = Style.NORMAL):
    print(colored_text(text, color, style))