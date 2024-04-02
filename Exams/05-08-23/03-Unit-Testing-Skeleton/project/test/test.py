from unittest import TestCase, main

from project.second_hand_car import SecondHandCar


class TestSecondHandCar(TestCase):
    def setUp(self):
        self.car = SecondHandCar("Q7", "SUV", 5000, 25000)

    def test_correct_init(self):
        self.assertEqual("Q7", self.car.model)
        self.assertEqual("SUV", self.car.car_type)
        self.assertEqual(5000, self.car.mileage)
        self.assertEqual(25000, self.car.price)
        self.assertEqual([], self.car.repairs)

    def test_if_price_below_1_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.car.price = 0
        self.assertEqual('Price should be greater than 1.0!', str(ve.exception))

    def test_if_mileage_below_100_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.car.mileage = 99
        self.assertEqual('Please, second-hand cars only! Mileage must be greater than 100!', str(ve.exception))

    def test_set_promotional_price_if_new_price_greater_than_current_raises_value_erroe(self):
        with self.assertRaises(ValueError) as ve:
            self.car.set_promotional_price(26000.50)
        self.assertEqual("You are supposed to decrease the price!", str(ve.exception))

    def test_set_promotional_price_if_new_price_less_than_current_returns_new_price(self):
        result = self.car.set_promotional_price(20_000)
        self.assertEqual("The promotional price has been successfully set.", result)
        self.assertEqual(20_000, self.car.price)

    def test_need_repair_when_cost_greater_than_half_the_price_repair_impossible(self):
        results = self.car.need_repair(13000, "body work + paint the front doors")
        self.assertEqual("Repair is impossible!", results)

    def test_need_repair_when_cost_affordable_increases_car_price_and_adds_repair_description(self):
        result = self.car.need_repair(9000.10, "body work + paint the front doors")
        self.assertEqual("Price has been increased due to repair charges.", result)
        self.assertEqual(34_000.10, self.car.price)
        self.assertEqual(["body work + paint the front doors"], self.car.repairs)

    def test___gt__if_car_type_not_same_as_the_other_car_type_cannot_compare_prices(self):
        self.car2 = SecondHandCar("A4", "sedan", 1000, 8000)
        result = self.car > self.car2
        self.assertEqual("Cars cannot be compared. Type mismatch!", result)

    def test__gt__if_compare_same_types_car(self):
        self.car2 = SecondHandCar("Q6", "SUV", 1000, 23000)
        result = self.car > self.car2
        #self.assertEqual(True, result)
        self.assertTrue(result)

    def test_str_if_correct(self):
        expected_result = f"""Model Q7 | Type SUV | Milage 5000km\nCurrent price: 25000.00 | Number of Repairs: 0"""
        self.assertEqual(expected_result, str(self.car))



if __name__ == "__main__":
    main()
