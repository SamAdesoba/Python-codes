import unittest
import play_ground


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        print("I run before play_ground test")

    def tearDown(self) -> None:
        print("I run after play_ground test")

    def test_can_create_play_ground(self):
        basket1 = play_ground.PlayGround()
        self.assertIsNotNone(basket1)
        self.assertIsInstance(basket1, play_ground.PlayGround)


if __name__ == '__main__':
    unittest.main()
