"""
Завдання 2. Читання даних про котів з файлу
У вас є текстовий файл, який містить інформацію про котів. 
Кожен рядок файлу містить унікальний ідентифікатор кота, 
його ім'я та вік, розділені комою. Наприклад:

Ваше завдання - розробити функцію get_cats_info(path), 
яка читає цей файл та повертає список словників з інформацією про кожного кота.
"""

from cats_utils import get_cats_info


def main() -> None:
    try:
        cats = get_cats_info("cats.txt")
        print(cats)
    except (FileNotFoundError, ValueError, OSError) as e:
        print(f"Помилка: {e}")


if __name__ == "__main__":
    main()