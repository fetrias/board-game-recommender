"""Helper functions for safe user input."""


def input_int(
    prompt: str,
    minimum: int | None = None,
    maximum: int | None = None,
) -> int:
    """Request an integer until the user enters an allowed value."""
    while True:
        try:
            value = int(input(prompt))
        except ValueError:
            print("Введите целое число.")
            continue

        if minimum is not None and value < minimum:
            print(f"Введите число не меньше {minimum}.")
            continue
        if maximum is not None and value > maximum:
            print(f"Введите число не больше {maximum}.")
            continue

        return value


def input_rating() -> int:
    """Request a board game rating from 1 to 5."""
    return input_int("Введите оценку от 1 до 5: ", minimum=1, maximum=5)


def select_game(games: list[dict]) -> dict | None:
    """Request a game identifier and return the selected game."""
    if not games:
        print("Список игр пуст.")
        return None

    for game in games:
        print(f"{game['id']} - {game['name']}")

    while True:
        game_id = input_int("Введите id игры или 0 для отмены: ", minimum=0)
        if game_id == 0:
            return None

        for game in games:
            if game["id"] == game_id:
                return game

        print("Игра с таким id не найдена.")
