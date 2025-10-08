def max_number(num1, num2):
    if num1 > num2: res=num1
    elif num1 < num2: res=num2
    else: res="Числа равны"
    return res

print (max_number (7, 7))

def empty_function():
    pass
    return

def even_numbers(n):
    i = 0
    for i in range(i, n):
        if (i % 2 == 0) and (i != 0):
            yield i
def  test_max_number(num1, num2):
    assert max_number(num1, num2) == num2 and max_number(num1, num2) == num2, "Числа равны"
    assert max_number(num1, num2) == num1, "Первое число больше"
    assert max_number(num1, num2) == num2, "Второе число больше"

for i in even_numbers(5):
    print(i)