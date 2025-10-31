class BankAccount:
    def __init__(self, initial_balance=0):
        self.__balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Успешно внесено: {amount} руб. Текущий баланс: {self.__balance} руб.")
        else:
            print("Ошибка: Сумма для депозита должна быть положительной.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Ошибка: Сумма для снятия должна быть положительной.")
        elif amount > self.__balance:
            print(f"Ошибка: Недостаточно средств. Текущий баланс: {self.__balance} руб.")
        else:
            self.__balance -= amount
            print(f"Успешно снято: {amount} руб. Текущий баланс: {self.__balance} руб.")

    def get_balance(self):
        return self.__balance

    def display_balance(self):
        print(f"Текущий баланс: {self.__balance} руб.")

