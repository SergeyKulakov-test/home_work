class BankAccount:
    def __init__(self, initial_balance=0):
        self.__balance = initial_balance  # Приватный атрибут

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Успешно внесено: {amount} руб. Текущий баланс: {self.__balance} руб.")
            return True
        else:
            print("Ошибка: Сумма для депозита должна быть положительной.")
            return False

    def withdraw(self, amount):
        if amount <= 0:
            print("Ошибка: Сумма для снятия должна быть положительной.")
            return False
        elif amount > self.__balance:
            print(f"Ошибка: Недостаточно средств. Текущий баланс: {self.__balance} руб.")
            return False
        else:
            self.__balance -= amount
            print(f"Успешно снято: {amount} руб. Текущий баланс: {self.__balance} руб.")
            return True

    def get_balance(self):
        return self.__balance

    def display_balance(self):
        print(f"Текущий баланс: {self.__balance} руб.")


def get_positive_number(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("Ошибка: Введите положительное число.")
                continue
            return value
        except ValueError:
            print("Ошибка: Введите корректное число.")


def menu_display_balance(account):
    account.display_balance()


def menu_deposit(account):
    amount = get_positive_number("Введите сумму для внесения: ")
    account.deposit(amount)


def menu_withdraw(account):
    amount = get_positive_number("Введите сумму для снятия: ")
    account.withdraw(amount)


def main():
    account = BankAccount(1000)

    menu_options = {
        "1": ("Показать баланс", menu_display_balance),
        "2": ("Внести деньги", menu_deposit),
        "3": ("Снять деньги", menu_withdraw),
        "4": ("Выйти", None)
    }

    while True:
        print("БАНКОВСКИЙ СЧЕТ")
        for key, value in menu_options.items():
            print(f"{key}. {value[0]}")
        choice = input("Выберите пункт меню: ")
        if choice == "4":
            print("До свидания!")
            break
        elif choice in menu_options:
            if choice != "4":
                menu_options[choice][1](account)
        else:
            print("Неверный пункт меню. Попробуйте снова.")


if __name__ == "__main__":
    main()