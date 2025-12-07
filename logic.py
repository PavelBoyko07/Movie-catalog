import json
import os


def load_movies(path: str = "movies.json") -> list[dict]:
    try:
        if not os.path.exists(path):
            return []

        with open(path, 'r', encoding='utf-8') as f:
            data = json.load(f)

        return data if isinstance(data, list) else []

    except (json.JSONDecodeError, OSError):
        return []

def save_movies(movies: list[dict], path: str = "movies.json") -> None:
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(movies, f, ensure_ascii=False, indent=2)

def add_movie(movies: list[dict], title: str, year: int) -> list[dict]:
    max_id = 0
    for movie in movies:
        if 'id' in movie and movie['id'] > max_id:
            max_id = movie['id']

    new_movie = {
        'id': max_id + 1,
        'title': title,
        'year': year,
        'watched': False,
        'rating': None
    }

    movies.append(new_movie)
    return movies

def mark_watched(movies: list[dict], movie_id: int, rating: int | None = None) -> list[dict]:
    if rating is not None:
        if not 1 <= rating <= 10:
            raise ValueError(f"Рейтинг должен быть от 1 до 10, получено: {rating}")

        # Создаём новый список с обновлённым фильмом
    updated_movies = []
    movie_found = False

    for movie in movies:
        if movie.get('id') == movie_id:
            # Обновляем найденный фильм
            updated_movie = movie.copy()  # Копируем чтобы не менять исходный
            updated_movie['watched'] = True
            if rating is not None:
                updated_movie['rating'] = rating
            updated_movies.append(updated_movie)
            movie_found = True
        else:
            updated_movies.append(movie.copy())

    if not movie_found:
        raise ValueError(f"Фильм с ID {movie_id} не найден")

    return updated_movies

def find_by_year(movies: list[dict], year: int) -> list[dict]:
    result = []
    for movie in movies:
        if movie.get('year') == year:
            result.append(movie)
    return result

def get_unwatched(movies: list[dict]) -> list[dict]:
    return [movie for movie in movies if not movie.get('watched', False)]