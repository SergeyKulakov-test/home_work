def max_number(num1, num2):
    if num1 > num2:
        return num1
    return num2

def empty_function():
    pass

def even_numbers(n):
    for i in range(0, n):
        if i % 2 == 0:
            yield i

def  test_max_number():
    assert max_number(3, 5) == 5, "Ошибка, не равно 5"
    assert max_number(4, 2) == 4, "Ошибка, не равно 4"
    assert max_number(8, 8) == 8, "Ошибка, не равно 8"
    print("Тесты пройдены")

for i in even_numbers(5):
    print(i)

test_max_number()








