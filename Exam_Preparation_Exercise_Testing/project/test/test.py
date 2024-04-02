from unittest import TestCase, main

from project.climbing_robot import ClimbingRobot


class TestClimbingRobot(TestCase):
    def setUp(self):
        self.robot = ClimbingRobot('Alpine', "metal", 100, 200)
        self.robot_with_installed_software = ClimbingRobot('Alpine', "metal", 100, 200)
        self.robot_with_installed_software.installed_software =[
            {"name":"Pycharm","capacity_consumption":50,"memory_consumption":49 },
            {"name":"CLion","capacity_consumption":49,"memory_consumption":51 }
        ]


    def test_correct_init(self):
        self.assertEqual('Alpine', self.robot.category)
        self.assertEqual("metal", self.robot.part_type)
        self.assertEqual(100, self.robot.capacity)
        self.assertEqual(200, self.robot.memory)
        self.assertEqual([],self.robot.installed_software)

    def test_invalid_category_raises_value_error(self):
        ALLOWED_CATEGORIES = ['Mountain', 'Alpine', 'Indoor', 'Bouldering']
        with self.assertRaises(ValueError) as ve:
            self.robot.category = "road"
        self.assertEqual(f"Category should be one of {ALLOWED_CATEGORIES}", str(ve.exception))

    def test_get_used_capacity_expect_success(self):
        result = self.robot_with_installed_software.get_used_capacity()
        expected = sum(s['capacity_consumption'] for s in self.robot_with_installed_software.installed_software)

        self.assertEqual(expected,result)

    def test_get_available_capacity_expect_success(self):
        expected = self.robot.capacity- sum(s['capacity_consumption'] for s in self.robot_with_installed_software.installed_software)
        result = self.robot_with_installed_software.get_available_capacity()

        self.assertEqual(expected,result)

    def test_get_used_memory_expect_success(self):
        result = self.robot_with_installed_software.get_used_memory()
        expected = sum(s['memory_consumption'] for s in self.robot_with_installed_software.installed_software)

        self.assertEqual(expected,result)

    def test_get_memory_capacity_expect_success(self):
        expected = self.robot.memory- sum(s['memory_consumption'] for s in self.robot_with_installed_software.installed_software)
        result = self.robot_with_installed_software.get_available_memory()

        self.assertEqual(expected,result)

    def test_install_software_with_max_equal_values_expects_success(self):
        result = self.robot.install_software({"name":"Pycharm","capacity_consumption":100,"memory_consumption":200 })
        self.assertEqual("Software 'Pycharm' successfully installed on Alpine part.", result)
        self.assertEqual(self.robot.installed_software,
                         [{"name":"Pycharm","capacity_consumption":100,"memory_consumption":200 }])

    def test_install_software_with_less_than_max_equal_values_expects_success(self):
        result = self.robot.install_software({"name":"Pycharm","capacity_consumption":10,"memory_consumption":20 })
        self.assertEqual("Software 'Pycharm' successfully installed on Alpine part.", result)
        self.assertEqual(self.robot.installed_software,
                         [{"name":"Pycharm","capacity_consumption":10,"memory_consumption":20 }])

    def test_install_software_with_one_value_more_than_max_equal_values_returns_error_msg(self):
        result = self.robot.install_software({"name":"Pycharm","capacity_consumption":10,"memory_consumption":2000})
        self.assertEqual("Software 'Pycharm' cannot be installed on Alpine part.", result)
        self.assertEqual(self.robot.installed_software,
                         [])

    def test_install_software_with_more_than_max_equal_values_returns_error_msg(self):
        result = self.robot_with_installed_software.install_software({"name":"Pycharm","capacity_consumption":49,"memory_consumption":50})
        self.assertEqual("Software 'Pycharm' cannot be installed on Alpine part.", result)
        self.assertEqual(self.robot.installed_software,
                         [])


if __name__ == "__main__":
    main()
