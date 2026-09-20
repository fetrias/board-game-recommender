"""Tests for board game recommendation functions."""

from recommendations import (
    filter_games_by_player_count,
    recommend_games,
)


GAMES = [
    {
        "name": "Палео",
        "categories": ["Кооперативная", "Приключенческая"],
        "min_players": 2,
        "max_players": 4,
        "ratings": [5, 4],
    },
    {
        "name": "Каркассон",
        "categories": ["Стратегическая", "Семейная"],
        "min_players": 2,
        "max_players": 5,
        "ratings": [4, 3],
    },
    {
        "name": "Азул",
        "categories": ["Абстрактная", "Стратегическая", "Семейная"],
        "min_players": 2,
        "max_players": 4,
        "ratings": [5, 4],
    },
]


def test_filter_games_by_player_count() -> None:
    """Only games supporting the player count are returned."""
    result = filter_games_by_player_count(GAMES, 5)

    assert [game["name"] for game in result] == ["Каркассон"]


def test_recommend_games_by_category() -> None:
    """Recommendations match the category and are sorted by rating."""
    result = recommend_games(GAMES, 4, "СЕМЕЙНАЯ")

    assert [game["name"] for game in result] == ["Азул", "Каркассон"]
