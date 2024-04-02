from unittest import TestCase, main

from project.robot import Robot


class TestRobot(TestCase):
    ALLOWED_CATEGORIES = ['Military', 'Education', 'Entertainment', 'Humanoids']
    PRICE_INCREMENT = 1.5

    def setUp(self):
        self.robot = Robot("r1", "Military", 50, 100.0)

    def test_correct_init(self):
        self.assertEqual("r1", self.robot.robot_id)
        self.assertEqual("Military", self.robot.category)
        self.assertEqual(50, self.robot.available_capacity)
        self.assertEqual(100.0, self.robot.price)
        self.assertEqual([], self.robot.hardware_upgrades)
        self.assertEqual([], self.robot.software_updates)

    def test_invalid_category_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.robot.category = "Cleaning"
        self.assertEqual(f"Category should be one of '{self.ALLOWED_CATEGORIES}'", str(ve.exception))

    def test_price_below_zero_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.robot.price = -1
        self.assertEqual("Price cannot be negative!", str(ve.exception))

    def test_upgrade_hardware_component_already_in_the_list_raises_error(self):
        hardware_component = "video_card"
        self.robot.hardware_upgrades = ["video_card"]
        expected = f"Robot r1 was not upgraded."
        result = self.robot.upgrade(hardware_component, 25.0)
        self.assertEqual(expected, result)

    def test_upgrade_hardware_component_added_correctly_in_the_list(self):
        hardware_component = "video_card"
        expected = f'Robot r1 was upgraded with video_card.'
        result = self.robot.upgrade(hardware_component, 25.0)
        self.assertEqual(expected, result)

    def test_upgrade_price_calculated_correctly(self):
        hardware_component = "video_card"
        self.robot.upgrade(hardware_component, 25.0)
        expected_price = 100.0 + (25.0 * 1.5)
        result = self.robot.price
        self.assertEqual(expected_price, result)

    def test_update_version_older_than_versions_in_software_list_returns_msg(self):
        self.robot.software_updates = [1.5, 1.8]
        expected = f"Robot r1 was not updated."
        actual = self.robot.update(1.6, 25)
        self.assertEqual(expected, actual)

    def test_update_available_capacity_not_enough_returns_msg(self):
        self.robot.software_updates = [1.5, 1.8]
        expected = f"Robot r1 was not updated."
        actual = self.robot.update(1.9, 51)
        self.assertEqual(expected, actual)

    def test_update_software_updates_with_success(self):
        self.robot.software_updates = [1.5, 1.8]
        actual = self.robot.update(1.9, 25)
        expected = f'Robot r1 was updated to version 1.9.'
        self.assertEqual(expected, actual)

    def test_update_software_updates_with_success_software_added_to_list_capacity_updated(self):
        self.robot.software_updates = [1.5, 1.8]
        self.robot.update(1.9, 24)
        expected_software_list = [1.5, 1.8, 1.9]
        self.assertEqual(expected_software_list, self.robot.software_updates)
        self.assertEqual(26, self.robot.available_capacity)

    def test_gt_if_first_robot_price_greater_than_second_returns_msg(self):
        self.robot2 = Robot("r2", "Military", 50, 99.0)
        expected = f'Robot with ID r1 is more expensive than Robot with ID r2.'
        actual = self.robot.__gt__(self.robot2)

        self.assertEqual(expected, actual)

    def test_gt_if_both_robot_prices_are_equall_returns_msg(self):
        self.robot2 = Robot("r2", "Military", 50, 100)
        expected = f'Robot with ID r1 costs equal to Robot with ID r2.'
        actual = self.robot.__gt__(self.robot2)

        self.assertEqual(expected, actual)

    def test_gt_if_first_robot_price_less_than_second_returns_msg(self):
        self.robot2 = Robot("r2", "Military", 50, 101)
        expected = f'Robot with ID r1 is cheaper than Robot with ID r2.'
        actual = self.robot.__gt__(self.robot2)

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    main()
