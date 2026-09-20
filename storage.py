"""Functions for loading and saving project data."""

import json


def load_games(filename: str) -> list[dict]:
    """Load a list of board games from a JSON file."""
    try:
        with open(filename, encoding="utf-8") as file:
            games = json.load(file)
    except FileNotFoundError:
        print(f"Файл {filename} не найден.")
        return []
    except json.JSONDecodeError:
        print(f"Файл {filename} содержит некорректный JSON.")
        return []

    if not isinstance(games, list):
        print(f"Файл {filename} должен содержать список игр.")
        return []

    return games


def save_games(filename: str, games: list[dict]) -> bool:
    """Save a list of board games to a JSON file."""
    try:
        with open(filename, "w", encoding="utf-8") as file:
            json.dump(games, file, ensure_ascii=False, indent=4)
    except OSError:
        print(f"Не удалось сохранить данные в файл {filename}.")
        return False

    return True
