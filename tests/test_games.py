"""Тесты функций для работы с настольными играми и оценками."""

import pytest

from games import (
    add_rating,
    calculate_average_rating,
    find_games,
    get_rating_statistics,
    remove_last_rating,
)


def test_calculate_average_rating() -> None:
    """Средняя оценка вычисляется для заполненного и пустого списков."""
    assert calculate_average_rating([5, 4, 3]) == 4.0
    assert calculate_average_rating([]) == 0.0


def test_find_games() -> None:
    """Игры находятся по части названия без учёта регистра."""
    games = [
        {"name": "Палео"},
        {"name": "Пиксель Тактикс"},
        {"name": "Диксит"},
    ]

    result = find_games(games, "ПИКСЕЛЬ")

    assert [game["name"] for game in result] == ["Пиксель Тактикс"]


def test_rating_operations() -> None:
    """Оценка добавляется, учитывается в статистике и удаляется."""
    game = {"ratings": [5, 4]}

    add_rating(game, 3)
    assert get_rating_statistics(game) == {"count": 3, "average": 4.0}
    assert remove_last_rating(game)
    assert game["ratings"] == [5, 4]

    with pytest.raises(ValueError):
        add_rating(game, 6)
