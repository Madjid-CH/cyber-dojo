from abc import ABC, abstractmethod


class AccountServiceInterface(ABC):
    @abstractmethod
    def deposit(self, amount: int):
        pass

    @abstractmethod
    def withdraw(self, amount: int):
        pass

    @abstractmethod
    def print_statement(self):
        pass
