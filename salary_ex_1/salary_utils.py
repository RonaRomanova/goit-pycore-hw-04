from pathlib import Path
from typing import Tuple


def total_salary(path: str) -> Tuple[int, float]:
    """
    Повертає загальну та середню суму зарплат з файлу path.

    Формат рядка: 'Імʼя Фамілія,3000'
    """
    file_path = Path(path)

    if not file_path.is_absolute() and not file_path.exists():
        file_path = Path(__file__).resolve().parent / path

    if not file_path.exists():
        raise FileNotFoundError(f"Файл не знайдено: {path}")

    total = 0
    count = 0

    with file_path.open("r", encoding="utf-8") as fh:
        for line in fh:
            line = line.strip()
            if not line:
                continue

            try:
                _, salary_str = line.split(",", maxsplit=1)
                salary = int(salary_str)
            except ValueError:
                raise ValueError(f"Невірний формат рядка: {line}")

            total += salary
            count += 1

    if count == 0:
        return 0, 0.0

    return total, total / count
