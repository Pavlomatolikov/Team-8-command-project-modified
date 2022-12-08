from .message_base_class import MyMessage


class SimpleResultMyMessage(MyMessage):
    def __init__(self, value: str):
        super().__init__(value)
        self.type = 'simple'
