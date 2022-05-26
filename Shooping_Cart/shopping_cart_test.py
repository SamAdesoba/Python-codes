import unittest
import shopping_cart


class MyTestCase(unittest.TestCase):
    def test_shopping_cart_can_be_created(self):
        basket1 = shopping_cart.ShoppingCart([], 3000)
        self.assertIsNotNone(basket1)
        self.assertIsInstance(basket1, shopping_cart.ShoppingCart)

    def test_shopping_cart_can_have_len(self):
        basket1 = shopping_cart.ShoppingCart(["shoe"], 3000)
        self.assertEqual(1, basket1.get_length())
        basket2 = shopping_cart.ShoppingCart(["shoe", "bag"], 3000)
        self.assertEqual(2, basket2.get_length())
        basket3 = shopping_cart.ShoppingCart(["shoe", "bag", "vibrator"], 3000)
        self.assertEqual(3, basket3.get_length())
        basket4 = shopping_cart.ShoppingCart(["shoe", "bag", "vibrator", "Kiss"], 3000)
        self.assertRaises(ValueError, basket4.get_length)

    def test_shopping_cart_can_add_item(self):
        basket1 = shopping_cart.ShoppingCart([], 3000)
        basket1.add("Shoe")
        self.assertEqual("Shoe", basket1.get_item(0))
        basket1.add("Bag")
        self.assertEqual("Bag", basket1.get_item(1))
        basket1.add("Vibrator")
        self.assertEqual("Vibrator", basket1.get_item(2))
        basket1.add("kiss")
        self.assertEqual("Bag", basket1.get_item(0))



if __name__ == '__main__':
    unittest.main()
