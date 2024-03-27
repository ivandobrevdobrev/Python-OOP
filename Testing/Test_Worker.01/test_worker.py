from unittest import TestCase, main

from worker import Worker


class TestWorker(TestCase):
    def setUp(self):
        self.worker  = Worker("Ivan",25_000, 100)  # runs before every Test case

    def test_correct_init(self):
        self.assertEqual("Ivan", self.worker.name)
        self.assertEqual(25000, self.worker.salary)
        self.assertEqual(100, self.worker.energy)
        self.assertEqual(0, self.worker.money)

    def test_work_when_worker_has_energy_expect_money_to_increase_energy_to_reduce(self):
        expected_money = self.worker.salary * 2 # ще го пускаме 2 пъти
        expected_energy = self.worker.energy -2

        self.worker.work()
        self.worker.work()   # пускаме го 2 пъти , за да видим дали са занулени данните

        self.assertEqual(expected_money,self.worker.money)
        self.assertEqual(expected_energy,self.worker.energy)

    def test_work_when_worker_doesnt_have_energy(self):
        self.worker.energy = 0 # Arrange

        with self.assertRaises(Exception) as ex:
            self.worker.work()  # Act

        self.assertEqual('Not enough energy.', str(ex.exception))

    def test_rest_increases_energy_with_one(self):
        expected_energy = self.worker.energy + 1

        self.worker.rest()
        self.assertEqual(expected_energy, self.worker.energy)

    def test_get_info_if_returns_correct_string(self):
        self.assertEqual('Ivan has saved 0 money.', self.worker.get_info())


if __name__ == "__main__":
    main()