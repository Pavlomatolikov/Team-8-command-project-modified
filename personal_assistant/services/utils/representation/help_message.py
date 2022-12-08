from .message_base_class import MyMessage


class HelpMyMessage(MyMessage):
    def __init__(self, value: dict):
        super().__init__(value)
        self.type = 'help'
