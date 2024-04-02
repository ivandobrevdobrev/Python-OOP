from unittest import TestCase, main

from project.trip import Trip


class TestTrip(TestCase):
    DESTINATION_PRICES_PER_PERSON = {'New Zealand': 7500, 'Australia': 5700, 'Brazil': 6200, 'Bulgaria': 500}

    def setUp(self):
        self.trip = Trip(1000.0, 4, True)

    def test_correct_init(self):
        self.assertEqual(1000.0, self.trip.budget)
        self.assertEqual(4, self.trip.travelers)
        self.assertTrue(self.trip.is_family)
        self.assertEqual({}, self.trip.booked_destinations_paid_amounts)

    def test_travelers_are_zero_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.trip.travelers = 0
        self.assertEqual('At least one traveler is required!', str(ve.exception))

    def test_is_family_true_and_person_less_than_2_set_is_family_toFalse(self):
        self.trip = Trip(1000.0, 1, True)

        self.assertEqual(False, self.trip.is_family)

    def test_book_a_trip_destination_not_valid_returns_message(self):
        destination = "Burgas"
        expected = "This destination is not in our offers, please choose a new one!"
        results = self.trip.book_a_trip(destination)

        self.assertEqual(expected, results)

    def test_book_a_trip_required_calculates_okay_for_family(self):
        new_trip = Trip(5000.0, 4, True)
        destination = "Bulgaria"
        expected_required_price = 500 * 4 * 0.9
        new_trip.book_a_trip(destination)
        self.assertEqual(expected_required_price, new_trip.booked_destinations_paid_amounts[destination])

    def test_book_trip_not_enough_budget_returns_message(self):
        new_trip = Trip(1000.0, 4, True)
        destination = "Bulgaria"
        result = new_trip.book_a_trip(destination)
        self.assertEqual("Your budget is not enough!", result)

    def test_book_trip_budget_calculated_ok_returns_success(self):
        self.trip.budget = 5000
        destination = "Bulgaria"
        self.trip.book_a_trip(destination)
        result_budget = self.trip.budget
        self.assertEqual(3200, result_budget)

    def test_book_trip_returns_correct_message(self):
        self.trip.budget = 5000
        destination = "Bulgaria"
        result = "Successfully booked destination Bulgaria! Your budget left is 3200.00"

        self.assertEqual(result, self.trip.book_a_trip(destination))

    def test_booking_status_no_bookings_made_returns_message(self):
        result = 'No bookings yet. Budget: 1000.00'
        self.assertEqual(result, self.trip.booking_status())

    def test_print_sorted_results(self):
        new_trip = Trip(30000.0, 1, False)
        destination1 = "Bulgaria"
        destination2 = "New Zealand"
        new_trip.book_a_trip(destination1)
        new_trip.book_a_trip(destination2)
        expected = f"""Booked Destination: Bulgaria
Paid Amount: 500.00
Booked Destination: New Zealand
Paid Amount: 7500.00
Number of Travelers: 1
Budget Left: 22000.00"""

        self.assertEqual(expected, new_trip.booking_status())


if __name__ == "__main__":
    main()
