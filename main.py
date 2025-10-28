def book_list_view(library):
    if not library:
        print("В библиотеке нет книг")
        return
    for key in library:
        print(key)


def add_book(title, author, year, library):
    try:
        library[title] = {"Автор": author, "Год издания": year, "Наличие": True}
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
    try:
        if library[title]["Наличие"]:
            status = "В наличии"
        else:
            status = "Выдана"
        print(f"Информация о книге '{title}':")
        print(f"  Автор: {library[title]["Автор"]}")
        print(f"  Год издания: {library[title]["Год издания"]}")
        print(f"  Наличие: {status}")
    except KeyError:
        print(f"Книга с названием '{title}' не найдена в библиотеке.")




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


title = input("Введите название книги: ")
author = input("Введите автора книги: ")
year = input("Введите год издания книги: ")


add_book(title, author, year, library)
book_list_view(library)


title_issue = input("Введите название книги для выдачи: ")

issue_book(title_issue, library)

title_return = input("Введите название книги для возврата: ")

return_book(title_return, library)

find_book(title_return, library)

title_delete = input("Введите название книги для удаления: ")

remove_book(title_delete, library)