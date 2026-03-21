"""
Логіка роботи з контактами для Завдання 4.
У цьому файлі реалізовано клас ContactsBook, який містить методи для
додавання, зміни, отримання та показу контактів.
"""

from typing import Dict

from prettytable import PrettyTable


class ContactsBook:
    def __init__(self) -> None:
        self.data: Dict[str, str] = {}

    def add(self, name: str, phone: str) -> str:
        """Додає/перезаписує контакт."""
        self.data[name.lower()] = phone
        return "Контакт додано."

    def change(self, name: str, phone: str) -> str:
        """Змінює телефон для контакту."""
        if name.lower() in self.data:
            self.data[name.lower()] = phone
            return "Контакт оновлено."
        return "Контакт не знайдено."

    def phone(self, name: str) -> str:
        """Повертає телефон за ім'ям."""
        return self.data.get(name.lower(), "Контакт не знайдено.")

    def show_all(self) -> str:
        """Повертає всі контакти у вигляді таблиці."""
        if not self.data:
            return "Контактів не збережено."

        table = PrettyTable()
        table.field_names = ["Ім'я", "Телефон"]

        for name, phone in self.data.items():
            table.add_row([name.capitalize(), phone])

        return table.get_string()
