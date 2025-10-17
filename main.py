my_list = []

for i in range(5):
    text = input(f"Введите строку {i+1}: ")
    my_list.append(text)

my_list[0], my_list[-1] = my_list[-1], my_list[0]

print("Список после замены:", my_list)