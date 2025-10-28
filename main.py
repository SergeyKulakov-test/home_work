def book_list_view(library):
    if not library:
        print("В библиотеке нет книг")
        return
    for key in library:
        print(key)


def add_book(title, author, year, library):
    try:
        library[title] = {"Автор": author, "Год издания": year, "Наличие": None}
        return library
    except NameError:
        print("Библиотека не создана")

def remove_book(title, library):
    try:
        del library[title]
        print(f"Книга '{title}' была удалена из библиотеки.")
    except KeyError:
        print(f"Книги с названием '{title}' нет в библиотеке.")


def issue_book(title, library):
    if library[title]["Наличие"] == None:
        print("Книга в библиотеке, но ее статус не определен")
        return
    try:
        if library[title]["Наличие"] == False:
            print(f"Книга '{title}' уже выдана.")
        else:
            library[title]["Наличие"] = False
            print(f"Книга '{title}' успешно выдана.")
    except KeyError:
        print(f"Книга с названием '{title}' не найдена в библиотеке.")


def return_book(title, library):
    try:
        if library[title]["Наличие"] == True:
            print(f"Книга '{title}' уже находится в библиотеке.")
        else:
            library[title]["Наличие"] = True
            print(f"Книга '{title}' возвращена в библиотеку.")
    except KeyError:
        print(f"Книга с названием '{title}' не найдена в библиотеке.")


def find_book(title, library):
    if library[title]["Наличие"] == None:
        print("Книга в библиотеке, но ее статус не определен")
        return
    try:
        if library[title]["Наличие"]:
            status = "Книга доступна"
        else:
            status = "Книга выдана"
        print(f"Информация о книге '{title}':")
        print(f"  Автор: {library[title]["Автор"]}")
        print(f"  Год издания: {library[title]["Год издания"]}")
        print(f"  Наличие: {status}")
    except KeyError:
        print(f"Книга с названием '{title}' не найдена в библиотеке.")


def menu_book_list_view():
    print("Список книг в библиотеке")
    book_list_view(library)


def menu_add_book():
    print("Введите данные для добавления книги в библиотеку")
    title = input("Введите название книги: ")
    author = input("Введите автора книги: ")
    year = input("Введите год издания книги: ")
    add_book(title, author, year, library)


def menu_remove_book():
    title = input("Введите название книги для удаления: ")
    remove_book(title, library)


def menu_issue_book():
    title = input("Введите название книги для выдачи: ")
    issue_book(title, library)


def menu_return_book():
    title = input("Введите название книги для возврата: ")
    return_book(title, library)


def menu_find_book():
    title = input("Введите название книги для поиска: ")
    find_book(title, library)


def main():
    while True:
        print("МЕНЮ:")
        for key, value in function_menu.items():
            print(f"{key}. {value[0]}")
        choice = input("Выберите пункт меню: ")
        if choice in function_menu:
            function_menu[choice][1]()
        else:
            print("Неверный пункт меню. Попробуйте снова.")


function_menu = {
        "1": ("Просмотреть какие книги сейчас в библиотеке", menu_book_list_view),
        "2": ("Добавить книгу", menu_add_book),
        "3": ("Взять книгу", menu_issue_book),
        "4": ("Вернуть книгу", menu_return_book),
        "5": ("Найти книгу", menu_find_book),
        "6": ("Удалить книгу", menu_remove_book),
}


library = {
    "Маленький принц": {
        "Автор": "Антуана де Сент-Экзюпери",
        "Год издания": "1943",
        "Наличие": True
    },
    "Повелитель мух": {
        "Автор": "Уильям Голдинг",
        "Год издания": "1983",
        "Наличие": False
    },
    "Мастер и маргарита": {
        "Автор": "Михаил Афанасьевич Булгаков",
        "Год издания": "1967 ",
        "Наличие": True
    },
}


main()