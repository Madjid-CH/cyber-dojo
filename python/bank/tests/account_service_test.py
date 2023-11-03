import io
import sys
from datetime import datetime
from unittest.mock import patch, MagicMock

from banking.account_service import AccountService, TransactionRepository


class TestAccountService:

    @staticmethod
    def assert_printed_balances_are_equal(actual_balance: str, expected_balance: str):
        assert actual_balance.replace(" ", "") == expected_balance.replace(" ", "")

    @patch('banking.account_service.DatePicker')
    def test_outside_in_behaviour(self, date_picker_mock):
        capture_output = io.StringIO()
        sys.stdout = capture_output
        transaction_repository = TransactionRepository()
        date_picker_mock.now = MagicMock(side_effect=[
            datetime(2012, 1, 10),
            datetime(2012, 1, 13),
            datetime(2012, 1, 14),
        ])
        account_service = AccountService(transaction_repository)
        account_service.deposit(1000)
        account_service.deposit(2000)
        account_service.withdraw(500)
        account_service.print_statement()
        expected_balance = (
            """Date       || Amount || Balance
            14/01/2012 || -500   || 2500
            13/01/2012 || 2000   || 3000
            10/01/2012 || 1000   || 1000
            """)
        sys.stdout = sys.__stdout__
        self.assert_printed_balances_are_equal(capture_output.getvalue(), expected_balance)
