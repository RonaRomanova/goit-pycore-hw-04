
"""
Завдання 3: Візуалізація структури директорії з кольорами.
python dir_tree.py /path/to/directory
"""

import sys
import os
from pathlib import Path
from colorama import init, Fore, Style

# Ініціалізація colorama для кросплатформенності
init(autoreset=True)


def print_tree(path: Path, prefix: str = "", is_last: bool = True):
    """
    Рекурсивно виводить дерево директорії з кольорами.
    
    Args:
        path: шлях до файлу/папки
        prefix: відступ для візуалізації
        is_last: чи останній елемент у списку
    """
    # Символи для дерева
    connector = "└── " if is_last else "├── "
    extender = "    " if is_last else "│   "
    
    # Кольори
    if path.is_dir():
        color = Fore.CYAN  # Директорії — блакитні
        item_type = "dir"
    else:
        color = Fore.GREEN  # Файли — зелені
        item_type = "file"
    
    # Виводимо поточний елемент
    print(f"{prefix}{connector}{color} {path.name}{Style.RESET_ALL}")
    
    # Якщо це директорія — рекурсивно обходимо вміст
    if path.is_dir():
        items = sorted(path.iterdir(), key=lambda p: (p.is_file(), p.name.lower()))
        
        for i, item in enumerate(items):
            is_last_item = (i == len(items) - 1)
            new_prefix = prefix + extender if not is_last else prefix + "    "
            print_tree(item, new_prefix, is_last_item)


def main():
    """Головна функція скрипта."""
    if len(sys.argv) != 2:
        print("Usage: python dir_tree.py <directory_path>")
        print("Приклад: python dir_tree.py /Users/nadya/Desktop")
        sys.exit(1)
    
    directory_path = Path(sys.argv[1])
    
    # Перевірка існування
    if not directory_path.exists():
        print(f"Шлях не існує: {directory_path}")
        sys.exit(1)
    
    # Перевірка, що це директорія
    if not directory_path.is_dir():
        print(f"'{directory_path}' не є директорією.")
        sys.exit(1)
    
    # Заголовок
    print(f"{directory_path}")
    print("-" * 50)
    
    # Рекурсивно виводимо вміст
    try:
        items = sorted(directory_path.iterdir(), key=lambda p: (p.is_file(), p.name.lower()))
        for i, item in enumerate(items):
            is_last = (i == len(items) - 1)
            print_tree(item, "", is_last)
    except PermissionError as e:
        print(f"Помилка доступу: {e}")
        sys.exit(1)
    except OSError as e:
        print(f"Помилка: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
