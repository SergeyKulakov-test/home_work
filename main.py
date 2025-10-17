list1 = [1, 2, 3, 4, 5, 6]
list2 = [10, 20, 30, 40, 50]

max_length = max(len(list1), len(list2))

result_list = []
for i in range(max_length):
    element1 = list1[i] if i < len(list1) else 0
    element2 = list2[i] if i < len(list2) else 0
    result_list.append(element1 + element2)

print("Список с суммами элементов:", result_list)