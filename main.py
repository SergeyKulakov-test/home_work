list1 = [1, 2, 3, 4, 5, 6]
list2 = [10, 20, 30, 40, 50]

min_length = min(len(list1), len(list2))

result_list = []
for i in range(min_length):
    sum_elements = list1[i] + list2[i]
    result_list.append(sum_elements)

print("Список с суммами элементов:", result_list)