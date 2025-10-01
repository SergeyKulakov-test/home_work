try:
    print("Сложение")
    num1 = float(input("Введите первое число: "))
    num2 = float(input("Введите второе число: "))
    result1 = num1 + num2
    print(f"Результат сложения: {result1}")

    print("Вычитание")
    num3 = float(input("Введите первое число: "))
    num4 = float(input("Введите второе число: "))
    result2 = num3 - num4
    print(f"Результат вычитания: {result2}")

    print("Умножение")
    num5 = float(input("Введите первое число: "))
    num6 = float(input("Введите второе число: "))
    result3 = num5 * num6
    print(f"Результат умножения: {result3}")

    print("Деление")
    num7 = float(input("Введите первое число: "))
    num8 = float(input("Введите второе число: "))
    result = num7 / num8
    print(f"Результат деления: {result}")
except ValueError:
    print("Ошибка: введено не число!")
except ZeroDivisionError:
    print("Ошибка: Деление на ноль!")

