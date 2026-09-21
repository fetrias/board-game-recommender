"""Функции для отбора и рекомендации настольных игр."""

from games import sort_games_by_rating


def is_player_count_suitable(game: dict, player_count: int) -> bool:
    """Проверить, подходит ли игра для указанного числа участников."""
    return game["min_players"] <= player_count <= game["max_players"]


def filter_games_by_player_count(
    games: list[dict],
    player_count: int,
) -> list[dict]:
    """Вернуть игры для указанного числа участников."""
    return [
        game
        for game in games
        if is_player_count_suitable(game, player_count)
    ]


def filter_games_by_category(
    games: list[dict],
    category: str,
) -> list[dict]:
    """Вернуть игры указанной категории."""
    normalized_category = category.strip().casefold()
    if not normalized_category:
        return list(games)

    return [
        game
        for game in games
        if any(
            normalized_category == game_category.casefold()
            for game_category in game["categories"]
        )
    ]


def recommend_games(
    games: list[dict],
    player_count: int,
    category: str = "",
) -> list[dict]:
    """Рекомендовать подходящие игры по убыванию средней оценки."""
    suitable_games = filter_games_by_player_count(games, player_count)
    suitable_games = filter_games_by_category(suitable_games, category)
    return sort_games_by_rating(suitable_games)
