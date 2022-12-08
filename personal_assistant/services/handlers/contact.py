from typing import Optional

from personal_assistant.services.decorators import input_error, route
from personal_assistant.services.utils import AddressBook, address_book
from ..utils.representation import SimpleResultMyMessage, TableMyMessage
from ..utils.representation import REPRESENTOR


@route("add-contact")
@input_error
def add_contact(name: str) -> SimpleResultMyMessage:
    """
    On this command, the bot saves a new contact in memory.
    The user enters the "add-contact" command and the name, necessarily separated by a space.
    Command example: add-contact UserName
    """
    address_book.Name(name)

    phone = REPRESENTOR.request_user_input("Enter phone number: ")
    address_book.Phone(phone) if phone else None

    birthday = REPRESENTOR.request_user_input("Enter date of birth (YYYY.MM.DD or DD.MM.YYYY): ")
    address_book.Birthday(birthday) if birthday else None

    address = REPRESENTOR.request_user_input("Enter address: ")
    address_book.Address(address) if address else None

    email = REPRESENTOR.request_user_input("Enter email (example@domain.com): ")
    address_book.Email(email) if email else None

    contact = address_book.Record(**locals())

    return SimpleResultMyMessage(f"Successfully created a new contact '{contact.name.value}'")


@route("remove-contact")
@input_error
def remove_contact(name: str) -> SimpleResultMyMessage:
    """
    On this command, the bot deletes the contact.
    The user enters the "remove-contact" command and the name, necessarily separated by a space.
    Command example: remove-contact UserName
    """
    contact = AddressBook()[name]

    contact.remove_record()

    return SimpleResultMyMessage(f"Successfully deleted contact '{name}'")


@route("show-all")
@input_error
def show_all_users() -> SimpleResultMyMessage | TableMyMessage:
    """
    By this command, the bot displays all saved contacts with all the data to the console.
    """
    format_contacts = [{"name": "Name", "email": "Email", "birthday": "Birthday", "phone": "Phone", "address": "Address"}]

    for contacts in AddressBook().iterator(1):
        contact = contacts[0]

        format_contacts.append(contact.format_record())

    if len(format_contacts) > 1:
        return TableMyMessage(format_contacts)
    else:
        return SimpleResultMyMessage("No contact has been saved.")


@route("search-contacts")
def search_contacts(search_value: str) -> Optional[SimpleResultMyMessage | TableMyMessage]:
    """
    By this command, the bot displays in the console all contacts that have a match with the search string in the name or number.
    The user enters the "search-contacts" command and the name of the contact, separated by a space.
    Command example: search-contact any
    """
    contacts = AddressBook().search_contacts(search_value)

    if not contacts:
        return SimpleResultMyMessage("No contact found.")

    format_contacts = [{"name": "Name", "email": "Email", "birthday": "Birthday", "phone": "Phone", "address": "Address"}]

    for contact in contacts:
        format_contacts.append(contact.format_record())

    return TableMyMessage(format_contacts)
