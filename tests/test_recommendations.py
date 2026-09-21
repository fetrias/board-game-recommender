"""Тесты функций рекомендации настольных игр."""

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
    """Возвращаются только игры для указанного числа участников."""
    result = filter_games_by_player_count(GAMES, 5)

    assert [game["name"] for game in result] == ["Каркассон"]


def test_recommend_games_by_category() -> None:
    """Рекомендации соответствуют категории и отсортированы по оценке."""
    result = recommend_games(GAMES, 4, "СЕМЕЙНАЯ")

    assert [game["name"] for game in result] == ["Азул", "Каркассон"]
