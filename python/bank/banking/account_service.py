from collections import namedtuple
from datetime import datetime

from banking.account_service_interface import AccountServiceInterface

Transaction = namedtuple('Transaction', ['date', 'amount'])


class TransactionRepository:
    def __init__(self):
        self._transactions: list[Transaction] = []

    def add_transaction(self, date: datetime, amount: int):
        self._transactions.append(Transaction(date, amount))

    def get_transactions(self):
        return self._transactions

    def get_ordered_transactions(self):
        return sorted(self._transactions, key=lambda t: t.date, reverse=True)

    def get_total_balance(self):
        return sum(t.amount for t in self._transactions)


class Printer:
    def __init__(self):
        self._header = "Date       || Amount || Balance"

    def print_transaction(self, transaction: Transaction, transaction_balance: int):
        formatted_date = self.print_formatted_date(transaction.date)
        print(f"{formatted_date} || {transaction.amount} || {transaction_balance}")

    def print_header(self):
        print(self._header)

    @staticmethod
    def print_formatted_date(date: datetime) -> str:
        return date.strftime("%d/%m/%Y")


class DatePicker:
    @staticmethod
    def now() -> datetime:
        return datetime.now()


class AccountService(AccountServiceInterface):

    def __init__(self, transaction_repository: TransactionRepository):
        self._transactions_repository = transaction_repository
        self._printer = Printer()

    def deposit(self, amount: int):
        self._transactions_repository.add_transaction(DatePicker.now(), amount)

    def withdraw(self, amount: int):
        self._transactions_repository.add_transaction(DatePicker.now(), -amount)

    def print_statement(self):
        self._printer.print_header()
        current_balance = self._transactions_repository.get_total_balance()
        for transaction in self._transactions_repository.get_ordered_transactions():
            self._printer.print_transaction(transaction, current_balance)
            current_balance -= transaction.amount
