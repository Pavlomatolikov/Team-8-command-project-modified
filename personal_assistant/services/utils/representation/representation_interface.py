from abc import abstractmethod, ABCMeta
from .message_base_class import MyMessage


class IRepresentor(metaclass=ABCMeta):
    """Abstract singleton class with interface to represent input/output of the application"""

    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    @abstractmethod
    def show(self, obj: MyMessage):
        pass

    @staticmethod
    @abstractmethod
    def show_warn_message(value: str):
        pass

    @staticmethod
    @abstractmethod
    def show_help(value: dict):
        pass

    @staticmethod
    @abstractmethod
    def show_simple_result(value: str):
        pass

    @staticmethod
    @abstractmethod
    def show_table(value: list):
        pass

    @staticmethod
    @abstractmethod
    def show_notes(value: str):
        pass

    @staticmethod
    @abstractmethod
    def show_prompt(value: str) -> None:
        pass

    @staticmethod
    @abstractmethod
    def request_user_input(message: str) -> str:
        pass
