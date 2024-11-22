all_films_path = "txtf/all_films.txt"
views_history_path = "txtf/views_history.txt"


class User:

    def __init__(self, username, watched_movies):
        """Инициальзация данных о конкретном пользователе."""
        self.username = username  # Имя пользователя
        self.watched_movies = set(watched_movies)  # Список фильмов, которые пользователь уже посмотрел

    def already_watched(self, movie_index):
        """Проверяет, смотрел ли пользователь указанный фильм."""
        return movie_index in self.watched_movies


class RecommendedMovies:

    def __init__(self, all_films_path, views_history_path):
        """Инициальзация данных из файлов ("all_films.txt", "views_history.txt")."""
        self.movies = self.get_movies(all_films_path)
        self.users_history = self.get_users_history(views_history_path)

    def get_movies(self, file_path):
        """Возвращает ID и название всех фильмов."""
        movies = {}
        with open(file_path, 'r') as file:
            for line in file:
                line = line.strip()
                parts = line.split(",", 1)
                if len(parts) == 2:
                    movie_index = int(parts[0].strip())
                    movie_name = parts[1].strip()
                    movies[movie_index] = movie_name
        return movies

    def get_users_history(self, file_path):
        """Возвращает история просмортров всех пользователей."""
        users_history = {}
        with (open(file_path, 'r') as file):
            for line in file:
                parts = line.strip().split(':')
                username = parts[0]
                if len(parts) > 1:
                    watched_movies = list(map(int, parts[1].split(',')))
                else:
                    watched_movies = []
                users_history[username] = User(username, watched_movies)
        return users_history

    def get_user_recommendation(self, username):
        """Возвращает рекомендацию для конкретного пользователя."""
        if username not in self.users_history:
            print(f"Пользователь {username} не найден.")
            return None

        current_user = self.users_history[username]
        current_watched = current_user.watched_movies

        # Поиск пользователей с похожей историей просмотров.
        similar_users = []
        for user in self.users_history.values():
            if user.username == username:
                continue
            all_movies = len(current_watched) + len(user.watched_movies)
            if all_movies >= len(current_watched) // 2:
                similar_users.append(user)

        # Сбор фильмов, которые смотрели похожие пользователи, но не смотрел текущий.
        recommended_movies = set()
        for user in similar_users:
            recommended_movies.update(user.watched_movies - current_watched)

        if not recommended_movies:
            print("Нет фильмов для рекомендации.")
            return None

        # Подсчёт количества просмотров для каждого фильма.
        movie_counts = {movie: 0 for movie in recommended_movies}
        for user in self.users_history.values():
            for movie in user.watched_movies:
                if movie in movie_counts:
                    movie_counts[movie] += 1

        # Поиск фильма с максимальным числом просмотров
        recommended_movie_index = max(movie_counts, key=movie_counts.get)
        return self.movies[recommended_movie_index]


if __name__ == "__main__":
    recomend_algorithm = RecommendedMovies(all_films_path, views_history_path)
    username = input("Введите имя пользователя для рекомендации: ")
    recommendation = recomend_algorithm.get_user_recommendation(username)
    if recommendation:
        print(f"Рекомендуемый фильм для {username}: {recommendation}")
