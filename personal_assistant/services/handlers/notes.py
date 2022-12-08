from personal_assistant.services.decorators import input_error, route
from personal_assistant.services.utils import notes, Notes
from ..utils.representation import SimpleResultMyMessage, NoteMyMessage, WarnMyMessage
from ..utils.representation import REPRESENTOR


@route('add-note')
@input_error
def add_note(text: str) -> SimpleResultMyMessage:
    """
    On this command, the bot stores a new note in memory.
    The user enters the "add-note" command and text, necessarily separated by a space.
    Command example: add-note
    """
    note = notes.Record(text)

    tag_input = REPRESENTOR.request_user_input("Enter tags separated by space: ")

    if tag_input:
        tags = tag_input.split(" ")
        note.add_tags(tags)

    return SimpleResultMyMessage("Note was successfully added")


@route('search-note')
@input_error
def search_notes_by_text(text: str) -> SimpleResultMyMessage | NoteMyMessage:
    """
    By this command, the bot searches the memory for a note by text.
    The user enters the "search-text" command separated by a space and the text that will be searched.
    Command example: search-text lorem ipsum dolor sit amet
    """
    results = notes.Notes().search_notes_by_text(text)

    if not results:
        return SimpleResultMyMessage("Note was not found.")

    format_results = ""

    for result in results:
        format_results += result.format_record() + '\n'

    return NoteMyMessage(format_results)


@route('search-tags')
@input_error
def search_notes_by_tags(tags: str) -> SimpleResultMyMessage | NoteMyMessage:
    """
    By this command, the bot searches the memory for a note by tags.
    The user enters a space-separated "search-tags" command and a space-separated tag/tags that will be searched.
    Command example: search-tags tag1 tag2
    """

    tags = tags.split()
    tags.sort()

    results: dict[str, list[notes.Record]] = {tag: notes.Notes().search_notes_by_tags([tag]) for tag in tags if notes.Notes().search_notes_by_tags([tag])}

    if not results:
        return SimpleResultMyMessage("Note was not found.")

    format_results = ""

    for key, value in results.items():
        note = '\n\tNote: '.join([str(x.text.value) for x in value])
        format_results += f"{key}\n\tNote: {note}\n"

    return NoteMyMessage(format_results)


def find_note_by_index() -> notes.Record | str:
    dict_indexes = {}

    num = 1

    for note in Notes().get_all_records():
        dict_indexes[num] = note.note_id

        print(f"{num}. \t{note.format_record()}")

        num += 1

    if num == 1:
        return "No notes"

    while True:
        try:
            index = int(
                REPRESENTOR.request_user_input("Enter the index of the note from the list: "))
        except ValueError:
            REPRESENTOR.show(WarnMyMessage("\nChoose a number from the list!"))
            REPRESENTOR.show(SimpleResultMyMessage("\n(Enter 0 to cancel)"))
            continue

        if index == 0:
            return "Cancel"

        try:
            return Notes().search_notes_by_id(dict_indexes[index])
        except KeyError:
            REPRESENTOR.show(WarnMyMessage("\nChoose a number from the list!"))
            REPRESENTOR.show(SimpleResultMyMessage("\n(Enter 0 to cancel)"))


@route('add-tags')
def add_tags_to_notes() -> SimpleResultMyMessage:
    """
    With this command, the bot adds tags to an existing post.
    The user enters the "add-tags" command.
    Next, the user will be prompted to enter tags separated by a space.
    Command example: add-tags
    """
    note = find_note_by_index()

    if isinstance(note, str):
        return SimpleResultMyMessage(note)

    tag_input = None

    while not tag_input:
        tag_input = REPRESENTOR.request_user_input("Enter tags separated by space: ")

    note.add_tags(tag_input.split(" "))

    return SimpleResultMyMessage('The tags have been added successfully')


@route('change-note')
def change_note() -> SimpleResultMyMessage:
    """
    With this command, the bot changes previously saved notes.
    The user enters the "change-note" command.
    Next, the user will be prompted to enter a new note text.
    Command example: change-note
    """
    note = find_note_by_index()

    if isinstance(note, str):
        return SimpleResultMyMessage(note)

    new_text = None

    while not new_text:
        new_text = input("Enter new note: ")

    note.replace_text(new_text)

    return SimpleResultMyMessage('Note was successfully change')


@route('delete-note')
def delete_note() -> SimpleResultMyMessage:
    """
    By this command, the bot deletes the previously saved note.
    The user enters the "delete-note" command.
    Next, the user will be prompted to select a note to delete from the list.
    Command example: delete-note
    """
    note = find_note_by_index()

    if isinstance(note, str):
        return SimpleResultMyMessage(note)

    note.remove_record()
    
    return SimpleResultMyMessage('Note was successfully deleted')
