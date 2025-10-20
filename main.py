def input_number_list(list_name):
    while True:
        try:
            numbers = input(f"Введите числа для {list_name} через пробел: ")
            return [int(num) for num in numbers.split()]
        except ValueError:
            print("Ошибка! Пожалуйста, вводите только целые числа.")


def sum_numbers(list_1, list_2):
    min_length = min(len(list_1), len(list_2))
    result_list = []
    for i in range(min_length):
        result_list.append(list_1[i] + list_2[i])
    if len(list_1) > min_length:
        result_list.extend(list_1[min_length:])
    else:
        result_list.extend(list_2[min_length:])
    print("Список с суммами элементов:", result_list)


list_1 = input_number_list("первого списка")
list_2 = input_number_list("второго списка")

sum_numbers(list_1, list_2)