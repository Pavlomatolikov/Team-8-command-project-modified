from colorama import init, Fore

from .representation_interface import IRepresentor
from .message_base_class import MyMessage
from .simple_result_message import SimpleResultMyMessage
from .table_message import TableMyMessage

init(autoreset=True)


class ConsoleRepresentor(IRepresentor):

    def show(self, obj: MyMessage):
        self.METHODS.get(obj.type)(obj.value)

    @staticmethod
    def show_warn_message(value: str):
        print(Fore.RED + value)

    @staticmethod
    def show_help(value: dict):
        for command, func in value.items():
            print(Fore.CYAN + command + Fore.YELLOW + func + '\n')

    @staticmethod
    def show_simple_result(value: str):
        print(Fore.YELLOW + f"{value}")

    @staticmethod
    def show_table(value: list[dict]):
        for i in value:
            print(": {:^15} : {:^15} : {:^10} : {:^30} : {:^30} :".format(*i.values()))

    @staticmethod
    def show_notes(value: str):
        print(Fore.YELLOW + f"{value}")

    @staticmethod
    def show_prompt(value: SimpleResultMyMessage) -> None:
        print(value.value)

    @staticmethod
    def request_user_input(message: str) -> str:
        return input(f"{Fore.LIGHTBLUE_EX}{message}")

    METHODS = {
        'warn': show_warn_message,
        'help': show_help,
        'simple': show_simple_result,
        'table': show_table,
        'note': show_notes
    }

