"""Functions for selecting and recommending board games."""

from games import sort_games_by_rating


def is_player_count_suitable(game: dict, player_count: int) -> bool:
    """Check whether a game supports the provided number of players."""
    return game["min_players"] <= player_count <= game["max_players"]


def filter_games_by_player_count(
    games: list[dict],
    player_count: int,
) -> list[dict]:
    """Return games suitable for the provided number of players."""
    return [
        game
        for game in games
        if is_player_count_suitable(game, player_count)
    ]


def filter_games_by_category(
    games: list[dict],
    category: str,
) -> list[dict]:
    """Return games belonging to the provided category."""
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
    """Recommend suitable games sorted by average rating."""
    suitable_games = filter_games_by_player_count(games, player_count)
    suitable_games = filter_games_by_category(suitable_games, category)
    return sort_games_by_rating(suitable_games)
