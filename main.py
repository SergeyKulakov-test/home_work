def input_number_list(list_name):
    while True:
        try:
            numbers = input(f"Введите числа для {list_name} через пробел: ")
            return [int(num) for num in numbers.split()]
        except ValueError:
            print("Ошибка! Пожалуйста, вводите только целые числа.")

def sum_numbers(list_1, list_2):
    max_length = max(len(list_1), len(list_2))
    result_list = []
    for i in range(max_length):
        element_1 = list_1[i] if i < len(list_1) else 0
        element_2 = list_2[i] if i < len(list_2) else 0
        result_list.append(element_1 + element_2)
    return print("Список с суммами элементов:", result_list)

list_1 = input_number_list("первого списка")
list_2 = input_number_list("второго списка")

sum_numbers(list_1, list_2)