"""Console interface for the board game recommendation service."""

from datetime import date
from pathlib import Path

from games import (
    add_rating,
    find_games,
    get_game_info,
    get_rating_statistics,
    remove_last_rating,
    sort_games_by_rating,
)
from recommendations import recommend_games
from storage import load_games, save_games
from utils import input_int, input_rating, select_game


DATA_FILE = str(Path(__file__).parent / "data" / "games.json")


def show_games(games: list[dict]) -> None:
    """Display a short list of board games."""
    if not games:
        print("Игры не найдены.")
        return

    for game in games:
        statistics = get_rating_statistics(game)
        print(
            f"{game['id']}. {game['name']} | "
            f"игроков: {game['min_players']}-{game['max_players']} | "
            f"средняя оценка: {statistics['average']:.2f}"
        )


def show_menu() -> None:
    """Display the application menu."""
    print("\n=== Сервис рекомендаций настольных игр ===")
    print("1. Показать все игры")
    print("2. Показать информацию об игре")
    print("3. Найти игру по названию")
    print("4. Получить рекомендацию")
    print("5. Отсортировать игры по рейтингу")
    print("6. Добавить оценку")
    print("7. Отменить последнюю оценку")
    print("8. Показать статистику оценок")
    print("0. Выход")


def show_game_details(games: list[dict]) -> None:
    """Request a game and display detailed information about it."""
    game = select_game(games)
    if game is not None:
        print("\n" + get_game_info(game))


def search_and_show_games(games: list[dict]) -> None:
    """Find games by name and display the results."""
    query = input("Введите название или его часть: ")
    found_games = find_games(games, query)
    show_games(found_games)


def show_recommendations(games: list[dict]) -> None:
    """Request recommendation parameters and display suitable games."""
    player_count = input_int(
        "Введите количество участников: ",
        minimum=1,
    )
    categories = sorted(
        {
            category
            for game in games
            for category in game["categories"]
        }
    )
    print("Доступные категории: " + ", ".join(categories))
    category = input("Введите категорию или оставьте поле пустым: ")
    suitable_games = recommend_games(games, player_count, category)
    show_games(suitable_games)


def add_game_rating(games: list[dict]) -> None:
    """Add and save a rating for the selected game."""
    game = select_game(games)
    if game is None:
        return

    rating = input_rating()
    try:
        add_rating(game, rating)
    except ValueError as error:
        print(error)
        return

    if save_games(DATA_FILE, games):
        print(f"Оценка добавлена {date.today()}.")


def cancel_last_rating(games: list[dict]) -> None:
    """Remove and save the last rating of the selected game."""
    game = select_game(games)
    if game is None:
        return

    if not remove_last_rating(game):
        print("У игры нет оценок для удаления.")
        return

    if save_games(DATA_FILE, games):
        print("Последняя оценка удалена.")


def show_rating_statistics(games: list[dict]) -> None:
    """Display rating count and average for the selected game."""
    game = select_game(games)
    if game is None:
        return

    statistics = get_rating_statistics(game)
    print(f"Количество оценок: {statistics['count']}")
    print(f"Средняя оценка: {statistics['average']:.2f}")


def main() -> None:
    """Load project data and run the application menu."""
    games = load_games(DATA_FILE)
    if not games:
        print("Нет данных для работы программы.")
        return

    while True:
        show_menu()
        choice = input_int("Выберите действие: ", minimum=0, maximum=8)

        if choice == 0:
            print("Работа программы завершена.")
            break
        if choice == 1:
            show_games(games)
        elif choice == 2:
            show_game_details(games)
        elif choice == 3:
            search_and_show_games(games)
        elif choice == 4:
            show_recommendations(games)
        elif choice == 5:
            show_games(sort_games_by_rating(games))
        elif choice == 6:
            add_game_rating(games)
        elif choice == 7:
            cancel_last_rating(games)
        elif choice == 8:
            show_rating_statistics(games)


if __name__ == "__main__":
    main()
