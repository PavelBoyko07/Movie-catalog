import logic


def main():
    movies = logic.load_movies()
    print(f"Загружено фильмов: {len(movies)}")

    while True:
        print("\nМЕНЕДЖЕР ФИЛЬМОВ")
        print("1. Показать все фильмы")
        print("2. Показать непросмотренные фильмы")
        print("3. Добавить фильм")
        print("4. Отметить фильм как просмотренный (с оценкой или без)")
        print("5. Найти фильмы по году")
        print("0. Выход")

        choice = input("Ваш выбор: ").strip()

        if choice == "0":
            logic.save_movies(movies)
            print("Ваши данные сохранены. Выход")
            break

        elif choice == "1":
            print("\nПОКАЗАТЬ ВСЕ ФИЛЬМЫ")
            if not movies:
                print("Список фильмов пуст")
            else:
                for movie in movies:
                    watched = "" if movie['watched'] else ""
                    # Исправлено: правильная проверка на None
                    rating = movie['rating'] if movie['rating'] is not None else ""
                    print(f"{movie['id']}. {movie['title']} ({movie['year']}) [{watched}] {rating}")

        elif choice == "2":
            unwatched = logic.get_unwatched(movies)
            print(f"\nНЕПРОСМОТРЕННЫЕ ФИЛЬМЫ ({len(unwatched)})")
            if not unwatched:
                print("Все фильмы просмотрены!")
            else:
                for movie in unwatched:
                    print(f"{movie['id']}. {movie['title']} ({movie['year']})")

        elif choice == "3":
            print("\nДОБАВИТЬ ФИЛЬМ")
            title = input("Название: ").strip()
            if not title:
                print("Название не может быть пустым")
                continue

            try:
                year = int(input("Год: ").strip())
                if year < 1888 or year > 2100:
                    print("Некорректный год (должен быть между 1888 и 2100)")
                    continue

                movies = logic.add_movie(movies, title, year)
                logic.save_movies(movies)
                print("Фильм добавлен")
            except ValueError:
                print("Год должен быть числом")
            except Exception as e:
                print(f"Ошибка при добавлении: {e}")

        elif choice == "4":
            print("\nОТМЕТИТЬ ПРОСМОТРЕННЫМ")
            if not movies:
                print("Список фильмов пуст")
                continue

            try:
                movie_id = int(input("ID фильма: ").strip())
                rating_input = input("Рейтинг 1-10: ").strip()
                rating = None
                if rating_input:
                    rating = int(rating_input)
                    if rating < 1 or rating > 10:
                        print("Рейтинг должен быть от 1 до 10")
                        continue

                movies = logic.mark_watched(movies, movie_id, rating)
                logic.save_movies(movies)
                print("Фильм отмечен как просмотренный")
            except ValueError as e:
                print(f"Ошибка: {e}")
            except:
                print("Ошибка ввода")

        elif choice == "5":
            print("\nПОИСК ПО ГОДУ")
            try:
                year = int(input("Год: ").strip())
                found = logic.find_by_year(movies, year)
                print(f"Найдено фильмов: {len(found)}")
                if found:
                    for movie in found:
                        watched = "" if movie['watched'] else ""
                        rating = movie['rating'] if movie['rating'] is not None else ""
                        print(f"{movie['id']}. {movie['title']} [{watched}] {rating}")
                else:
                    print("Фильмы не найдены")
            except ValueError:
                print("Год должен быть числом")
            except Exception as e:
                print(f"Ошибка: {e}")

        else:
            print("Неверный выбор. Попробуйте снова.")

if __name__ == "__main__":  # ИСПРАВЛЕНО: двойное подчеркивание
    main()
