from colorama import init, Fore

from .services.db import create_all_tables
from .services.utils.input_parser import text_parsing
from .services.utils.representation import SimpleResultMyMessage
from .services.utils.representation import REPRESENTOR

init(autoreset=True)


def main() -> None:
    create_all_tables()
    REPRESENTOR.show_prompt(SimpleResultMyMessage(f"{Fore.GREEN}"
                                                  f"Developed by GoIt Team 8\n\n"
                                                  f"Your personal assistant welcomes you.\n\n"
                                                  f"Type {Fore.MAGENTA}«help»{Fore.GREEN} to see all available "
                                                  f"commands\n "
                                                  ))

    while True:
        text = REPRESENTOR.request_user_input("\nEnter command: ")

        result = text_parsing(text)

        if not result:
            continue

        func, args = result

        result = func(*args) if args else func()

        if result:
            REPRESENTOR.show(result)

            if result.value == "Good bye!":
                break


if __name__ == '__main__':
    main()
