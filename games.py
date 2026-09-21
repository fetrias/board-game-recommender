"""Функции для работы с настольными играми и оценками."""


def calculate_average_rating(ratings: list[int]) -> float:
    """Вычислить среднее значение переданных оценок."""
    if not ratings:
        return 0.0
    return sum(ratings) / len(ratings)


def get_game_info(game: dict) -> str:
    """Вернуть отформатированную информацию о настольной игре."""
    categories = ", ".join(game["categories"])
    average_rating = calculate_average_rating(game["ratings"])

    return (
        f"Название: {game['name']}\n"
        f"Категории: {categories}\n"
        f"Количество игроков: от {game['min_players']} "
        f"до {game['max_players']}\n"
        f"Средняя оценка: {average_rating:.2f}"
    )


def find_games(games: list[dict], query: str) -> list[dict]:
    """Найти игры, названия которых содержат переданный текст."""
    normalized_query = query.strip().casefold()
    return [
        game
        for game in games
        if normalized_query in game["name"].casefold()
    ]


def sort_games_by_rating(games: list[dict]) -> list[dict]:
    """Вернуть игры по убыванию средней оценки."""
    return sorted(
        games,
        key=lambda game: calculate_average_rating(game["ratings"]),
        reverse=True,
    )


def add_rating(game: dict, rating: int) -> None:
    """Добавить настольной игре оценку от 1 до 5."""
    if not 1 <= rating <= 5:
        raise ValueError("Оценка должна быть целым числом от 1 до 5.")
    game["ratings"].append(rating)


def remove_last_rating(game: dict) -> bool:
    """Удалить последнюю оценку игры при наличии оценок."""
    if not game["ratings"]:
        return False
    game["ratings"].pop()
    return True


def get_rating_statistics(game: dict) -> dict[str, int | float]:
    """Вернуть количество оценок и их среднее значение."""
    ratings = game["ratings"]
    return {
        "count": len(ratings),
        "average": calculate_average_rating(ratings),
    }
