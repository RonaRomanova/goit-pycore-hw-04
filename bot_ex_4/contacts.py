"""
Функції для роботи з контактами.
"""

from typing import Dict


def add_contact(args: list[str], contacts: Dict[str, str]) -> str:
    """Додає контакт до словника."""
    if len(args) != 2:
        return "Використовуйте: add <name> <phone>"

    name, phone = args
    contacts[name.lower()] = phone
    return "Контакт додано."


def change_contact(args: list[str], contacts: Dict[str, str]) -> str:
    """Оновлює номер телефону для наявного контакту."""
    if len(args) != 2:
        return "Використовуйте: change <name> <phone>"

    name, phone = args
    normalized_name = name.lower()

    if normalized_name not in contacts:
        return "Контакт не знайдено."

    contacts[normalized_name] = phone
    return "Контакт оновлено."


def show_phone(args: list[str], contacts: Dict[str, str]) -> str:
    """Повертає телефон контакту за ім'ям."""
    if len(args) != 1:
        return "Використовуйте: phone <name>"

    name = args[0].lower()
    return contacts.get(name, "Контакт не знайдено.")


def show_all(contacts: Dict[str, str]) -> str:
    """Повертає всі контакти у вигляді таблиці."""
    if not contacts:
        return "Контактів не збережено."

    name_header = "Ім'я"
    phone_header = "Телефон"
    formatted_contacts = [
        (name.capitalize(), phone) for name, phone in contacts.items()
    ]

    name_width = max(len(name_header), *(len(name) for name, _ in formatted_contacts))
    phone_width = max(
        len(phone_header),
        *(len(phone) for _, phone in formatted_contacts),
    )

    border = f"+-{'-' * name_width}-+-{'-' * phone_width}-+"
    header = (
        f"| {name_header.ljust(name_width)} | "
        f"{phone_header.ljust(phone_width)} |"
    )

    lines = [border, header, border]
    for name, phone in formatted_contacts:
        lines.append(f"| {name.ljust(name_width)} | {phone.ljust(phone_width)} |")

    lines.append(border)
    return "\n".join(lines)
