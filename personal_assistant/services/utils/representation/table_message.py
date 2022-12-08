from .message_base_class import MyMessage


class TableMyMessage(MyMessage):
    def __init__(self, value: list):
        super().__init__(value)
        self.type = 'table'
