"""Functions for working with board games and ratings."""


def calculate_average_rating(ratings: list[int]) -> float:
    """Calculate the average value of the provided ratings."""
    if not ratings:
        return 0.0
    return sum(ratings) / len(ratings)


def get_game_info(game: dict) -> str:
    """Return formatted information about a board game."""
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
    """Find games whose names contain the provided text."""
    normalized_query = query.strip().casefold()
    return [
        game
        for game in games
        if normalized_query in game["name"].casefold()
    ]


def sort_games_by_rating(games: list[dict]) -> list[dict]:
    """Return games sorted by average rating in descending order."""
    return sorted(
        games,
        key=lambda game: calculate_average_rating(game["ratings"]),
        reverse=True,
    )


def add_rating(game: dict, rating: int) -> None:
    """Add a rating from 1 to 5 to a board game."""
    if not 1 <= rating <= 5:
        raise ValueError("Оценка должна быть целым числом от 1 до 5.")
    game["ratings"].append(rating)


def remove_last_rating(game: dict) -> bool:
    """Remove the last rating if the game has any ratings."""
    if not game["ratings"]:
        return False
    game["ratings"].pop()
    return True


def get_rating_statistics(game: dict) -> dict[str, int | float]:
    """Return the number of ratings and their average value."""
    ratings = game["ratings"]
    return {
        "count": len(ratings),
        "average": calculate_average_rating(ratings),
    }
