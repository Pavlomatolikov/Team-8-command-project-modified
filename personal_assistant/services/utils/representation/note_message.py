from .message_base_class import MyMessage


class NoteMyMessage(MyMessage):
    def __init__(self, value: str):
        super().__init__(value)
        self.type = 'note'
