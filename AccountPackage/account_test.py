import unittest
import account


class account_test(unittest.TestCase):

    def setUp(self) -> None:
        self.account1 = account.Account("Samson", "1234", "07068038660")

    def tearDown(self) -> None:
        self.balance = 0

    def test_that_account_can_be_created(self):
        self.assertIsNotNone(self.account1)
        self.assertIsInstance(self.account1, account.Account)

    def test_that_account_has_a_name(self):
        name = self.account1.name
        self.assertEqual("Samson", name)

    def test_that_account_has_a_paasword(self):
        password = self.account1.password
        self.assertEqual("1234", password)

    def test_that_account_has_phone_number(self):
        phone_number = self.account1.phone_number
        self.assertEqual("07068038660", phone_number)

    def test_that_account_can_deposit(self):
        account1 = account.Account("Samson", "1234", "07068038660")
        account1.deposit(5000)
        self.assertEqual(5000, account1.balance)

    def test_that_account_cannot_accept_negative_deposit(self):
        account1 = self.account1
        account1.deposit(2000)
        self.assertRaises(ValueError, account1.deposit, -1000)
        self.assertEqual(2000, account1.balance)

    def test_that_account_can_withdraw(self):
        account1 = self.account1
        account1.deposit(2000)
        self.assertEqual(2000, account1.balance)
        account1.withdraw(1000, "1234")
        self.assertEqual(1000, account1.balance)

    def test_that_account_cannot_withdraw_negative_amount(self):
        account1 = account.Account("Samson", "1234", "07068038660")
        account1.deposit(2000)
        self.assertEqual(2000, account1.balance)
        self.assertRaises(ValueError, account1.withdraw, -1000, "1234")
        self.assertEqual(2000, account1.balance)

    def test_that_account_cannot_withdraw_with_wrong_password(self):
        account1 = account.Account("Samson", "1234", "07068038660")
        account1.deposit(2000)
        self.assertEqual(2000, account1.balance)
        self.assertRaises(ValueError, account1.withdraw, 1000, "1233")
        self.assertEqual(2000, account1.balance)

    def test_that_account_cannot_withdraw_above_balance(self):
        account1 = account.Account("Samson", "1234", "07068038660")
        account1.deposit(2000)
        self.assertEqual(2000, account1.balance)
        self.assertRaises(ValueError, account1.withdraw, 3000, "1234")
        self.assertEqual(2000, account1.balance)

    def test_that_account_can_load_airtime(self):
        account1 = account.Account("Samson", "1234", "07068038660")
        account1.deposit(2000)
        self.assertEqual(2000, account1.balance)
        account1.load_airtime(200, "07068038660")
        self.assertEqual(1800, account1.balance)

    def test_that_account_cannot_load_negative_airtime_amount(self):
        account1 = account.Account("Samson", "1234", "07068038660")
        account1.deposit(2000)
        self.assertEqual(2000, account1.balance)
        self.assertRaises(ValueError, account1.withdraw, -1000, "07068038660")
        self.assertEqual(2000, account1.balance)

    def test_that_account_cannot_load_above_balance(self):
        account1 = account.Account("Samson", "1234", "07068038660")
        account1.deposit(200)
        self.assertEqual(200, account1.balance)
        self.assertRaises(ValueError, account1.withdraw, 300, "07068038660")
        self.assertEqual(200, account1.balance)

    def test_that_create_another_account(self):
        account2 = account.Account("Adesoba", "2283", "07041917414")
        self.assertEqual("Adesoba", account2.name)
        self.assertEqual("2283", account2.password)
        self.assertEqual("07041917414", account2.phone_number)
        self.assertIsInstance(account2, account.Account)

    def test_that_account_can_transfer(self):
        account1 = account.Account("Samson", "1234", "07068038660")
        account2 = account.Account("Adesoba", "2283", "07041917414")
        account1.deposit(5000)
        account1.transfer(account2, 2000, "1234")
        self.assertEqual(3000, account1.balance)
        self.assertEqual(2000, account2.balance)


if __name__ == "__main__":
    unittest.main()
