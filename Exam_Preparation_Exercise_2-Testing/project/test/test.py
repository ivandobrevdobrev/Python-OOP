from collections import deque
from unittest import TestCase,main

from project.railway_station import RailwayStation


class TestRailwayStation(TestCase):
    def setUp(self):
        self.station = RailwayStation("Burgas")

    def test_correct_init(self):
        self.assertEqual("Burgas", self.station.name)
        self.assertEqual(deque(),self.station.arrival_trains)
        self.assertEqual(deque(),self.station.departure_trains)

    def test_name_if_lenght_less_than_3_symbols_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.station.name = "ghs"
        self.assertEqual("Name should be more than 3 symbols!", str(ve.exception))

    def test_new_arrival_on_board_adds_trains(self):
        self.assertEqual(deque(), self.station.arrival_trains)
        self.assertEqual(0,len(self.station.arrival_trains))

        self.station.new_arrival_on_board("Train1")

        self.assertEqual(deque(["Train1"]), self.station.arrival_trains)
        self.assertEqual(1,len(self.station.arrival_trains))

    def test_train_has_arrived_info_different_from_info_in_the_deque(self):
        self.station.new_arrival_on_board("Train1")
        train_info = "Train2"

        result = self.station.train_has_arrived(train_info)
        expected = "There are other trains to arrive before Train2."
        self.assertEqual(expected,result)

    def test_train_has_arrived_pick_up_the_info_of_the_arrived_train(self):
        self.station.new_arrival_on_board("Train1")
        train_info = "Train1"

        result = self.station.train_has_arrived(train_info)
        expected = "Train1 is on the platform and will leave in 5 minutes."
        self.assertEqual(expected, result)
        self.assertEqual(0,len(self.station.arrival_trains))
        self.assertEqual(1,len(self.station.departure_trains))

    def test_train_has_left_returns_true(self):
        self.station.new_arrival_on_board("Train1")
        self.station.train_has_arrived("Train1")
        train_info = "Train1"

        result = self.station.train_has_left(train_info)
        self.assertEqual(0,len(self.station.departure_trains))
        self.assertEqual(0, len(self.station.arrival_trains))
        self.assertTrue(result)

    def test_train_has_left_returns_false(self):
        self.station.new_arrival_on_board("Train1")
        self.station.train_has_arrived("Train1")
        train_info = "Train2"

        result = self.station.train_has_left(train_info)
        self.assertEqual(1,len(self.station.departure_trains))
        self.assertFalse(result)

if __name__ == "__main__":
    main()