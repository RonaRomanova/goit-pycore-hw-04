from pathlib import Path
from typing import List, Dict, Any


def get_cats_info(path: str) -> List[Dict[str, str]]:
    """
    Читає файл котів, повертає список словників.

    Формат рядка: id,name,age
    """
    file_path = Path(path)

    if not file_path.is_absolute() and not file_path.exists():
        file_path = Path(__file__).resolve().parent / path

    if not file_path.exists():
        raise FileNotFoundError(f"Файл не знайдено: {path}")

    cats: List[Dict[str, str]] = []

    try:
        with file_path.open("r", encoding="utf-8") as fh:
            for line_num, line in enumerate(fh, start=1):
                line = line.strip()
                if not line:
                    continue  # пропускаємо порожні рядки

                try:
                    parts = list(filter(None, line.split(",", maxsplit=2)))  # видаляємо порожні частини
                    if len(parts) != 3:
                        raise ValueError(f"Очікується 3 поля (id,name,age), отримано {len(parts)}")

                    cat_id, name, age = parts
                    # Перевіряємо вік на число
                    try:
                        int(age)  # кидає ValueError, якщо не число
                    except ValueError:
                        raise ValueError(f"Вік має бути числом: {age}")

                    cat = {
                        "id": cat_id,
                        "name": name,
                        "age": age
                    }
                    cats.append(cat)

                except ValueError as err:
                    raise ValueError(f"Рядок {line_num}: {err}. Рядок: '{line}'")

    except OSError as err:
        raise OSError(f"Помилка читання файлу: {err}") from err

    return cats