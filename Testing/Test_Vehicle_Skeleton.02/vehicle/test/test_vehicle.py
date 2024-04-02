from unittest import TestCase, main

from project.vehicle import Vehicle


class TestVehicle(TestCase):
    def setUp(self):
        self.vehicle = Vehicle(51.25, 125.5)

    def test_correct_init(self):
        self.assertEqual(51.25, self.vehicle.fuel)
        self.assertEqual(51.25, self.vehicle.capacity)
        self.assertEqual(125.5, self.vehicle.horse_power)
        self.assertEqual(1.25, self.vehicle.fuel_consumption)

    def test_drive_when_fuel_is_not_enough_to_drive_the_distance_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.drive(50)
        self.assertEqual("Not enough fuel", str(ex.exception))

    def test_drive_when_fuel_is_enough_to_drive_the_distance(self):
        expected_fuel = 51.25 - (30*1.25)
        self.vehicle.drive(30)
        self.assertEqual(expected_fuel,self.vehicle.fuel)

    def test_refuel_when_amount_of_fuel_excise_capacity_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.refuel(10)
        self.assertEqual("Too much fuel",str(ex.exception))

    def test_refuel_when_fuel_can_fit_in_the_capacity(self):
        self.vehicle.fuel = 30
        self.vehicle.refuel(11.25)
        expected_fuel = 41.25
        self.assertEqual(expected_fuel,self.vehicle.fuel)

    def test_string_returns_correct_text(self):
        self.assertEqual(f"The vehicle has 125.5 horse power with 51.25 fuel left and 1.25 fuel consumption",self.vehicle.__str__())


if __name__ == "__main__":
    main()
