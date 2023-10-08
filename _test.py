import unittest
import solution  # Assuming the code is saved in a file named 'solution.py'

class TestSavingsAccountFunctions(unittest.TestCase):

    def setUp(self):
        # Reset the account balance to its initial state before each test.
        solution.account_balance = 100

    def test_initial_balance(self):
        self.assertEqual(solution.check_balance(), 100)

    def test_valid_deposit(self):
        self.assertEqual(solution.deposit(50), 150)

    def test_valid_withdrawal(self):
        self.assertEqual(solution.withdraw(30), 120)

    def test_withdrawal_exceeding_balance(self):
        self.assertEqual(solution.withdraw(200), "Insufficient funds!")

    def test_multiple_transactions(self):
        solution.deposit(100)
        solution.withdraw(50)
        self.assertEqual(solution.check_balance(), 150)

if __name__ == "__main__":
    unittest.main()
