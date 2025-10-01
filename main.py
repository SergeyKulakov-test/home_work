try:
    print("Сложение")
    num1 = float(input("Введите первое число: "))
    num2 = float(input("Введите второе число: "))
    result1 = num1 + num2
except ValueError:
    print("Ошибка: введено не число!")
else:
    print(f"Результат сложения: {result1}")

try:
    print("Вычитание")
    num3 = float(input("Введите первое число: "))
    num4 = float(input("Введите второе число: "))
    result2 = num3 - num4
except ValueError:
    print("Ошибка: введено не число!")
else:
    print(f"Результат вычитания: {result2}")

try:
    print("Умножение")
    num5 = float(input("Введите первое число: "))
    num6 = float(input("Введите второе число: "))
    result3 = num5 * num6
except ValueError:
    print("Ошибка: введено не число!")
else:
    print(f"Результат умножения: {result3}")

try:
    print("Деление")
    num7 = float(input("Введите первое число: "))
    num8 = float(input("Введите второе число: "))
    result = num7 / num8
except ValueError:
    print("Ошибка: введено не число!")
except ZeroDivisionError:
    print("Ошибка: Деление на ноль!")
else:
    print(f"Результат деления: {result}")
