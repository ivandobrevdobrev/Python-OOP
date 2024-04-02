from unittest import TestCase, main

from project.tennis_player import TennisPlayer


class TestTennisPlayer(TestCase):
    def setUp(self):
        self.player = TennisPlayer("Ivan", 37, 20)
        self.player2 = TennisPlayer("Nik", 39, 25)

    def test_correct_init(self):
        self.assertEqual("Ivan", self.player.name)
        self.assertEqual(37, self.player.age)
        self.assertEqual(20, self.player.points)
        self.assertEqual([], self.player.wins)

    def test_name_less_than_2_symbols_raises_error(self):
        with self.assertRaises(ValueError) as ve:
            self.player.name = "ib"
        self.assertEqual("Name should be more than 2 symbols!", str(ve.exception))

    def test_age_less_than_18_raises_error(self):
        with self.assertRaises(ValueError) as ve:
            self.player.age = 17
        self.assertEqual("Players must be at least 18 years of age!", str(ve.exception))

    def test_adding_new_win_successfully_if_tournament_not_in_the_list(self):
        tournament_name = "Miami open"
        self.player.add_new_win(tournament_name)
        self.assertEqual(["Miami open"], self.player.wins)

    def test_add_new_win_tournament_already_exists_returns_error(self):
        self.player.wins = ["Miami open"]
        tournament_name = "Miami open"
        expected = f"Miami open has been already added to the list of wins!"
        actual = self.player.add_new_win(tournament_name)

        self.assertEqual(expected, actual)

    def test_lt_if_points_less_than_other_player_points_return_msg(self):
        expected = f'Nik is a top seeded player and he/she is better than Ivan'
        actual = self.player.__lt__(self.player2)
        self.assertEqual(expected, actual)

    def test_lt_if_points_greater_than_other_player_points_return_msg(self):
        self.player2.points = 12.5
        expected = f'Ivan is a better player than Nik'
        actual = self.player.__lt__(self.player2)
        self.assertEqual(expected, actual)

    def test_str_returns_success(self):
        self.player.points = 50.29
        self.player.wins =["Miami","US Open","Paris"]
        expected= f"Tennis Player: Ivan\n" \
                  f"Age: 37\n" \
                  f"Points: 50.3\n" \
                  f"Tournaments won: Miami, US Open, Paris"
        actual = self.player.__str__()

        self.assertEqual(expected,actual)


if __name__ == "__main__":
    main()
