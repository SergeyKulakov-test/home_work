class FileManager:
    def __init__(self, filename):
        self.__filename = filename

    def set_filename(self, filename):
        if isinstance(filename, str) and filename.strip():
            self.__filename = filename.strip()
        else:
            print("Ошибка: Имя файла должна быть непустой строкой.")

    def read_file(self):
        try:
            with open(self.__filename, 'r', encoding='utf-8') as file:
                content = file.read()
                print(f"Содержимое файла {self.__filename}:")
                print(content)
        except FileNotFoundError:
            print(f"Ошибка: Файл '{self.__filename}' не найден.")
        except UnicodeDecodeError:
            print(f"Ошибка: Невозможно прочитать файл '{self.__filename}' в кодировке UTF-8.")

    def add_to_file(self):
        content = input("Введите текст для добавления в файл: ")
        with open(self.__filename, 'a', encoding='utf-8') as file:
            file.write(content + "\n")
        print(f"Текст успешно добавлен в файл '{self.__filename}'.")

    def read_file_line(self):
        try:
            with open(self.__filename, 'r', encoding='utf-8') as file:
                print(f"Содержимое файла {self.__filename} (построчно):")
                for line_num, line in enumerate(file, 1):
                    print(f"{line_num}: {line.strip()}")
        except FileNotFoundError:
            print(f"Ошибка: Файл '{self.__filename}' не найден.")
        except UnicodeDecodeError:
            print(f"Ошибка: Невозможно прочитать файл '{self.__filename}' в кодировке UTF-8.")

    def type_convert_file(self):
        try:
            with open(self.__filename, 'rb') as file, open(self.__filename + '.bin', 'wb') as data_new:
                data_new.write(file.read())
            print(f"Файл успешно конвертирован в бинарный: '{self.__filename}.bin'")
        except FileNotFoundError:
            print(f"Ошибка: Файл '{self.__filename}' не найден.")


def main():
    file_manager = FileManager("data.txt")

    menu_options = {
        "1": ("Прочитать файл", file_manager.read_file),
        "2": ("Добавить текст в файл", file_manager.add_to_file),
        "3": ("Прочитать файл построчно", file_manager.read_file_line),
        "4": ("Конвертировать файл в бинарный", file_manager.type_convert_file),
        "5": ("Выйти", None)
    }

    while True:
        print("МЕНЮ")

        for key, value in menu_options.items():
            print(f"{key}. {value[0]}")

        choice = input("Выберите пункт меню: ")

        if choice == "5":
            print("До свидания!")
            break
        elif choice in menu_options:
            menu_options[choice][1]()
        else:
            print("Неверный пункт меню. Попробуйте снова.")


if __name__ == "__main__":
    main()