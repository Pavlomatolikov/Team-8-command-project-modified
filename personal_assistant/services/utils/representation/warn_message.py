from .message_base_class import MyMessage


class WarnMyMessage(MyMessage):
    def __init__(self, value: str):
        super().__init__(value)
        self.type = 'warn'
