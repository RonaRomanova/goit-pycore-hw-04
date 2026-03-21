"""
Бот для керування контактами.

"""

from contacts import ContactsBook


def parse_input(user_input: str) -> tuple[str, list[str]]:
    """Розбиває введений рядок на команду та аргументи."""
    parts = user_input.strip().split()
    if not parts:
        return "", []

    command = parts[0].lower()
    args = parts[1:]
    return command, args


def main() -> None:
    """Запускає бота в інтерактивному режимі."""
    book = ContactsBook()

    print("\nПривіт, ласкаво просимо до персонального асистента!")

    while True:
        user_input = input("\nВведіть команду: ")
        command, args = parse_input(user_input)

        if command in {"close", "exit"}:
            print("До побачення!")
            break

        if command == "hello":
            print("Як я можу допомогти?")
            continue

        if command == "add":
            if len(args) != 2:
                print("Використовуйте: add <name> <phone>")
                continue
            name, phone = args
            print(book.add(name, phone))
            continue

        if command == "change":
            if len(args) != 2:
                print("Використовуйте: change <name> <phone>")
                continue
            name, phone = args
            print(book.change(name, phone))
            continue

        if command == "phone":
            if len(args) != 1:
                print("Використовуйте: phone <name>")
                continue
            print(book.phone(args[0]))
            continue

        if command == "all":
            print(book.show_all())
            continue

        print("Невідома команда.")


if __name__ == "__main__":
    main()
