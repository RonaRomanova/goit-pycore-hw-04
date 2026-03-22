"""
Бот для керування контактами.

"""

from contacts import add_contact, change_contact, show_all, show_phone


def parse_input(user_input: str) -> tuple[str, list[str]]:
    """Розбиває введений рядок на команду та аргументи."""
    parts = user_input.strip().split()
    if not parts:
        return "", []

    command = parts[0].lower()
    args = parts[1:]
    return command, args


def handle_command(command: str, args: list[str], contacts: dict[str, str]) -> str:
    """Повертає результат виконання команди."""
    if command == "hello":
        return "\nЯк я можу допомогти?"

    if command == "add":
        return add_contact(args, contacts)

    if command == "change":
        return change_contact(args, contacts)

    if command == "phone":
        return show_phone(args, contacts)

    if command == "all":
        return show_all(contacts)

    return "\nНевідома команда."


def main() -> None:
    """Запускає бота в інтерактивному режимі."""
    contacts: dict[str, str] = {}

    print("\nПривіт, ласкаво просимо до персонального асистента!")

    while True:
        user_input = input("\nВведіть команду: ")
        command, args = parse_input(user_input)

        if command in {"close", "exit"}:
            print("\nДо побачення!")
            break

        print(handle_command(command, args, contacts))


if __name__ == "__main__":
    main()
