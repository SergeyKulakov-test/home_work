def sum_even_numbers():
    sum = 0
    for i in range(0, 100):
        if i % 2 == 0:
            sum += i
    return print(f"Сумма четных чисел до 100: {sum}")

def square_odd_numbers():
    square_odd = []
    for i in range(0, 10):
        if i % 2 != 0:
            square_odd.append(i)
    square_odd = [x**2 for x in square_odd]
    return print(f"Список квадратов нечетных чисел до 10: {square_odd}")

def count_positive_numbers():
    count = 0
    while True:
        try:
            number = float(input("Введите число: "))
            if number < 0:
                break
            else:
                count += 1
        except ValueError:
            print("Ошибка! Пожалуйста, введите число.")
    return print(f"Количество введеных не отрицательных чисел: {count}")

sum_even_numbers()
square_odd_numbers()
count_positive_numbers()






