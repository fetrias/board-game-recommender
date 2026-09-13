from datetime import date


def get_game_info(
    name,
    category,
    minimum_players,
    maximum_players,
    ratings,
):
    return (
        f"Название: {name}\n"
        f"Категория: {category}\n"
        f"Количество игроков: от {minimum_players} до {maximum_players}\n"
        f"Оценки: {ratings}"
    )


def is_player_count_suitable(
    player_count,
    minimum_players,
    maximum_players,
):
    if minimum_players <= player_count <= maximum_players:
        return True
    return False


def calculate_average_rating(ratings):
    return sum(ratings) / len(ratings)


print("Выберите настольную игру:")
print("1 - Палео")
print("2 - Пиксель Тактикс")
print("3 - Диксит")

game_number = input("Введите номер игры: ")
game_found = True

if game_number == "1":
    game_name = "Палео"
    game_category = "Кооперативная приключенческая игра"
    minimum_players = 2
    maximum_players = 4
    ratings = [5, 4]
elif game_number == "2":
    game_name = "Пиксель Тактикс"
    game_category = "Тактическая карточная игра"
    minimum_players = 2
    maximum_players = 2
    ratings = [4, 5]
elif game_number == "3":
    game_name = "Диксит"
    game_category = "Ассоциативная игра"
    minimum_players = 3
    maximum_players = 8
    ratings = [4, 3]
else:
    game_found = False
    print("Игра с таким номером не найдена.")

if game_found:
    print("\nИнформация об игре")
    print(
        get_game_info(
            game_name,
            game_category,
            minimum_players,
            maximum_players,
            ratings,
        )
    )

    player_count = int(input("\nВведите количество участников: "))
    if is_player_count_suitable(
        player_count,
        minimum_players,
        maximum_players,
    ):
        print("Игра подходит для указанного количества участников.")
    else:
        print("Игра не подходит для указанного количества участников.")

    new_rating = int(input("Поставьте игре оценку от 1 до 5: "))
    if 1 <= new_rating <= 5:
        ratings.append(new_rating)
        average_rating = calculate_average_rating(ratings)
        print(f"Оценка учтена {date.today()}.")
        print(f"Все оценки игры: {ratings}")
        print(f"Средняя оценка игры: {average_rating:.2f}")
    else:
        print("Оценка должна быть целым числом от 1 до 5.")
