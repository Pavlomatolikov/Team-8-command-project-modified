from functools import wraps

from colorama import Fore
from ..utils.representation import WarnMyMessage
from ..utils.representation import REPRESENTOR


def input_error(func):
    @wraps(func)
    def inner(*args, **kwargs) -> None:
        try:
            return func(*args, **kwargs)
        except ValueError as e:
            REPRESENTOR.show(WarnMyMessage(f"{e}\n"))
        except KeyError as e:
            REPRESENTOR.show(WarnMyMessage(f"User {e} not found\n"))
        except IndexError as e:
            REPRESENTOR.show(WarnMyMessage(f"{e}\n"))

    return inner
