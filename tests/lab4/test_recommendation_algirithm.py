import unittest
from src.lab4.task1.recommendation_algorithm import RecommendedMovies


class RecommendationAlgorithmTestCase(unittest.TestCase):
    all_films_path = "/Users/6ogdanmezentsev/PycharmProjects/Mezentsev-programming/src/lab4/task1/txtf/all_films.txt"
    views_history_path = "/Users/6ogdanmezentsev/PycharmProjects/Mezentsev-programming/src/lab4/task1/txtf/views_history.txt"

    def test_1(self):
        recomend_algorithm = RecommendedMovies(self.all_films_path, self.views_history_path)
        expected_result = "Хатико"

        result = recomend_algorithm.get_user_recommendation("alice")

        self.assertEqual(result, expected_result)

    def test_2(self):
        recomend_algorithm = RecommendedMovies(self.all_films_path, self.views_history_path)
        expected_result = "Мстители: Финал"

        result = recomend_algorithm.get_user_recommendation("bob")

        self.assertEqual(result, expected_result)

    def test_3(self):
        recomend_algorithm = RecommendedMovies(self.all_films_path, self.views_history_path)
        expected_result = "Дюна"

        result = recomend_algorithm.get_user_recommendation("charlie")

        self.assertEqual(result, expected_result)

    def test_4(self):
        recomend_algorithm = RecommendedMovies(self.all_films_path, self.views_history_path)
        expected_result = "Унесенные призраками"

        result = recomend_algorithm.get_user_recommendation("pit")

        self.assertEqual(result, expected_result)

    def test_5(self):
        recomend_algorithm = RecommendedMovies(self.all_films_path, self.views_history_path)
        expected_result = "Иллюзия обмана"

        result = recomend_algorithm.get_user_recommendation("kate")

        self.assertEqual(result, expected_result)