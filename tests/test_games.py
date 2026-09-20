"""Tests for board game and rating functions."""

import pytest

from games import (
    add_rating,
    calculate_average_rating,
    find_games,
    get_rating_statistics,
    remove_last_rating,
)


def test_calculate_average_rating() -> None:
    """Average rating is calculated for filled and empty lists."""
    assert calculate_average_rating([5, 4, 3]) == 4.0
    assert calculate_average_rating([]) == 0.0


def test_find_games() -> None:
    """Games are found by a case-insensitive part of their names."""
    games = [
        {"name": "Палео"},
        {"name": "Пиксель Тактикс"},
        {"name": "Диксит"},
    ]

    result = find_games(games, "ПИКСЕЛЬ")

    assert [game["name"] for game in result] == ["Пиксель Тактикс"]


def test_rating_operations() -> None:
    """A rating can be added, summarized, and removed."""
    game = {"ratings": [5, 4]}

    add_rating(game, 3)
    assert get_rating_statistics(game) == {"count": 3, "average": 4.0}
    assert remove_last_rating(game)
    assert game["ratings"] == [5, 4]

    with pytest.raises(ValueError):
        add_rating(game, 6)
