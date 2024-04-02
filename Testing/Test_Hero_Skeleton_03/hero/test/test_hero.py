from unittest import TestCase, main

from project.hero import Hero


class TestHero(TestCase):
    def setUp(self):
        self.hero = Hero("Ivan",5,10.00,5.5)
        self.enemy_hero = Hero("Mike",4,9.00,5.7)

    def test_correct_init(self):
        self.assertEqual("Ivan",self.hero.username)
        self.assertEqual(5,self.hero.level)
        self.assertEqual(10.00, self.hero.health)
        self.assertEqual(5.5,self.hero.damage)

    def test_enemy_same_as_username_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.hero.battle(self.hero)
        self.assertEqual("You cannot fight yourself", str(ex.exception))

    def test_if_health_is_less_equal_zero_raises_exception(self):
        self.hero.health = 0
        with self.assertRaises(ValueError) as ve:
            self.hero.battle(self.enemy_hero)

        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ve.exception))

    def test_if_enemy_hero_health_is_less_equal_zero_raises_exception(self):
        self.enemy_hero.health = 0
        with self.assertRaises(ValueError) as ve:
            self.hero.battle(self.enemy_hero)
        self.assertEqual(f"You cannot fight Mike. He needs to rest", str(ve.exception))

    def test_fight_with_result_draw_returns_draw_and_decreases_both_health(self):
        self.hero.health = 9.00
        results = self.hero.battle(self.enemy_hero)

        self.assertEqual("Draw", results)
        self.assertEqual(-18.5, self.enemy_hero.health)
        self.assertEqual(-13.80, self.hero.health)

    def test_fight_enemy_and_win_increases_stats(self):
        self.hero = Hero("Ivan", 1, 100, 100)  # put easy nums here for easy calculation
        self.enemy_hero = Hero("Mike", 1, 50, 50)

        expected_level = self.hero.level +1
        expected_damage = self.hero.damage +5
        expected_health = self.hero.health - self.enemy_hero.damage + 5
        result = self.hero.battle(self.enemy_hero)

        self.assertEqual("You win",result)
        self.assertEqual(expected_level,self.hero.level)
        self.assertEqual(expected_health,self.hero.health)
        self.assertEqual(expected_damage,self.hero.damage)

    def test_fight_enemy_and_lose_expect_enemy_stats_increase(self):
        self.hero = Hero("Ivan", 1, 100, 100)  # put easy nums here for easy calculation
        self.enemy_hero = Hero("Mike", 1, 50, 50)
        self.hero, self.enemy_hero = self.enemy_hero, self.hero # razmenqme gi da moje da zagubim bitkata, da ne stevame novi stosinosti

        expected_level = self.enemy_hero.level + 1
        expected_damage = self.enemy_hero.damage + 5
        expected_health = self.enemy_hero.health - self.hero.damage + 5

        result = self.hero.battle(self.enemy_hero)

        self.assertEqual("You lose", result)
        self.assertEqual(expected_level, self.enemy_hero.level)
        self.assertEqual(expected_health, self.enemy_hero.health)
        self.assertEqual(expected_damage, self.enemy_hero.damage)

    def test_correct_str(self):
        expected_result = f"Hero Ivan: 5 lvl\n" \
                          f"Health: 10.0\n" \
                          f"Damage: 5.5\n"

        self.assertEqual(expected_result,self.hero.__str__())


if __name__ == "__main__":
    main()
