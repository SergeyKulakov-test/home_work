def book_list_view(library):
    if not library:
        print("В библиотеке нет книг")
        return
    for key in library:
        print(key)


def add_book():
    title = input("Введите название книги: ")
    author = input("Введите автора книги: ")
    while True:
        try:
            year = int(input("Введите год издания книги: "))
            library[title] = {"Автор": author, "Год издания": str(year), "Наличие": None}
            return library
        except ValueError:
            print("Год должен быть числом!")


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


add_book()
book_list_view(library)