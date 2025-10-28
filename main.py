def book_list_view(library):
    if not library:
        print("В библиотеке нет книг")
        return
    for key in library:
        print(key)


def add_book(title, author, year):
    try:
        library[title] = {"Автор": author, "Год издания": year, "Наличие": None}
        return library
    except NameError:
        print("Библиотека не создана")

def remove_book(title):
    try:
        del library[title]
        print(f"Книга '{title}' была удалена из библиотеки.")
    except KeyError:
        print(f"Книги с названием '{title}' нет в библиотеке.")



library = {
    "Маленький принц": {
        "Автор": "Антуана де Сент-Экзюпери", "Год издания": "1943", "Наличие": "В наличии"
    },
    "Повелитель мух": {
"Автор": "Уильям Голдинг", "Год издания": "1983", "Наличие": "Нет в наличии"
    },
    "Мастер и маргарита": {
        "Автор": "Михаил Афанасьевич Булгаков", "Год издания": "1967 ", "Наличие": "В наличии"
    },
}


title = input("Введите название книги: ")
author = input("Введите автора книги: ")
year = input("Введите год издания книги: ")


add_book(title, author, year)
book_list_view(library)


title_delete = input("Введите название книги для удаления: ")


remove_book(title_delete)