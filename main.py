def create_list():
    list_elements = input('Введите элементы списка через пробел:  ')
    list_elements = list(list_elements.split())
    return list_elements


def number_elements(list_elements):
    set_1 = set(list_elements)
    set_length = len(set_1)
    print(f"Уникальные элементы: {set_1}",f"Количество уникальных элементов: {set_length}", sep='\n')
    return


number_elements(create_list())



