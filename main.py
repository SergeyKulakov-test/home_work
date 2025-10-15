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
            square_odd.append(i**2)
    return print(f"Список квадратов нечетных чисел до 10: {square_odd}")

def count_positive_numbers():
    count = 0
    while True:
        number = float(input("Введите число: "))
        if number < 0:
            break
        else:
            count += 1
    return print(f"Количество введеных не отрицательных чисел: {count}")

sum_even_numbers()
square_odd_numbers()
count_positive_numbers()






