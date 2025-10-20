def input_number_list(list_name):
    numbers = input(f"Введите числа для {list_name} через пробел: ")
    return [int(num) for num in numbers.split()]

def sum_numbers(list1, list2):
    max_length = max(len(list1), len(list2))
    result_list = []
    for i in range(max_length):
        element1 = list1[i] if i < len(list1) else 0
        element2 = list2[i] if i < len(list2) else 0
        result_list.append(element1 + element2)
    return print("Список с суммами элементов:", result_list)

list1 = input_number_list("первого списка")
list2 = input_number_list("второго списка")


sum_numbers(list1, list2)