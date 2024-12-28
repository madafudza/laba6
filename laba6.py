import unittest
from unittest.mock import Mock, patch

class BankAccount:
    def __init__(self, accountNumber: str, balance: float = 0.0):
        if balance < 0:
            raise ValueError("Initial balance cannot be negative")
        self.accountNumber = accountNumber
        self.balance = balance

    def deposit(self, amount: float):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self.balance += amount

    def withdraw(self, amount: float):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount

    def getBalance(self):
        return self.balance

class TestBankAccount(unittest.TestCase):
    def test_initialization_valid_balance(self):
        account = BankAccount("12345", 100.0)
        self.assertEqual(account.getBalance(), 100.0)

    def test_initialization_invalid_balance(self):
        with self.assertRaises(ValueError):
            BankAccount("12345", -50.0)

    def test_deposit_valid_amount(self):
        account = BankAccount("12345", 100.0)
        account.deposit(50.0)
        self.assertEqual(account.getBalance(), 150.0)

    def test_deposit_invalid_amount(self):
        account = BankAccount("12345", 100.0)
        with self.assertRaises(ValueError):
            account.deposit(0.0)
        with self.assertRaises(ValueError):
            account.deposit(-10.0)

    def test_withdraw_valid_amount(self):
        account = BankAccount("12345", 100.0)
        account.withdraw(50.0)
        self.assertEqual(account.getBalance(), 50.0)

    def test_withdraw_insufficient_funds(self):
        account = BankAccount("12345", 100.0)
        with self.assertRaises(ValueError) as context:
            account.withdraw(150.0)
        self.assertEqual(str(context.exception), "Insufficient funds")

    def test_withdraw_invalid_amount(self):
        account = BankAccount("12345", 100.0)
        with self.assertRaises(ValueError):
            account.withdraw(0.0)
        with self.assertRaises(ValueError):
            account.withdraw(-20.0)

    def test_get_balance_after_operations(self):
        account = BankAccount("12345", 100.0)
        account.deposit(50.0)
        account.withdraw(30.0)
        self.assertEqual(account.getBalance(), 120.0)

    @patch('laba6.BankAccount.getBalance')
    def test_mocked_get_balance(self, mock_get_balance):
        mock_get_balance.return_value = 500.0
        account = BankAccount("12345")
        self.assertEqual(account.getBalance(), 500.0)


if __name__ == "__main__":
    unittest.main()
