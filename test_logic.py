import json
import os
import tempfile
from logic import *

def test_1_empty_file():
    print("Тест 1: Загрузка несуществующего файла")
    result = load_movies("файл_которого_нет.json")
    assert result == [], "Должен вернуть пустой список"
    print("OK")

def test_2_add_movie():
    print("Тест 2: Добавление фильма")
    movies = []
    movies = add_movie(movies, "Матрица", 1999)

    assert len(movies) == 1, "Должен быть 1 фильм"
    assert movies[0]['title'] == "Матрица"
    assert movies[0]['year'] == 1999
    assert movies[0]['id'] == 1
    assert movies[0]['watched'] == False
    assert movies[0]['rating'] == None
    print("OK")

def test_3_add_second_movie():
    print("Тест 3: Добавление второго фильма")
    movies = [
        {'id': 1, 'title': 'Фильм 1', 'year': 2020, 'watched': False, 'rating': None}
    ]
    movies = add_movie(movies, "Фильм 2", 2021)

    assert len(movies) == 2
    assert movies[1]['id'] == 2, "ID должен быть 2"
    print("OK")

def test_4_mark_watched():
    print("Тест 4: Отметить как просмотренный")
    movies = [
        {'id': 1, 'title': 'Тест', 'year': 2020, 'watched': False, 'rating': None}
    ]
    movies = mark_watched(movies, movie_id=1, rating=9)

    assert movies[0]['watched'] == True
    assert movies[0]['rating'] == 9
    print("OK")

def test_5_find_by_year():
    print("Тест 5: Поиск по году")
    movies = [
        {'id': 1, 'title': 'Фильм 2020', 'year': 2020, 'watched': False, 'rating': None},
        {'id': 2, 'title': 'Фильм 2021', 'year': 2021, 'watched': False, 'rating': None},
        {'id': 3, 'title': 'Еще 2020', 'year': 2020, 'watched': False, 'rating': None}
    ]

    result = find_by_year(movies, 2020)
    assert len(result) == 2, "Должно найти 2 фильма 2020 года"
    print("OK")

def test_6_get_unwatched():
    print("Тест 6: Непросмотренные фильмы")
    movies = [
        {'id': 1, 'title': 'Не смотрел', 'year': 2020, 'watched': False, 'rating': None},
        {'id': 2, 'title': 'Посмотрел', 'year': 2021, 'watched': True, 'rating': 8},
        {'id': 3, 'title': 'Тоже не смотрел', 'year': 2022, 'watched': False, 'rating': None}
    ]

    unwatched = get_unwatched(movies)
    assert len(unwatched) == 2, "Должно быть 2 непросмотренных"

    titles = [m['title'] for m in unwatched]
    assert 'Не смотрел' in titles
    assert 'Тоже не смотрел' in titles
    print("OK")


def run_all_tests():
    print("=" * 50)
    print("ЗАПУСК 6 ТЕСТОВ ДЛЯ МЕНЕДЖЕРА ФИЛЬМОВ")
    print("=" * 50)

    tests = [
        test_1_empty_file,
        test_2_add_movie,
        test_3_add_second_movie,
        test_4_mark_watched,
        test_5_find_by_year,
        test_6_get_unwatched
    ]

    passed = 0
    total = len(tests)

    for test in tests:
        try:
            test()
            passed += 1
        except AssertionError as e:
            print(f"Ошибка: {e}")
        except Exception as e:
            print(f"Неожиданная ошибка: {e}")

    print("=" * 50)
    print(f"ИТОГ: {passed}/{total} тестов пройдено")
    print("=" * 50)

    if passed == total:
        print("Все тесты пройдены успешно!")
    else:
        print("Некоторые тесты не пройдены")

if __name__ == "main":
    run_all_tests()