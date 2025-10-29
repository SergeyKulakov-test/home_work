class ToDoList:
    def __init__(self):
        self.tasks = {}
        self.next_id = 1

    def add_task(self, task):
        task_id = self.next_id
        self.tasks[task_id] = {"task": task, "completed": False}
        print(f"Задача #{task_id} '{task}' добавлена.")
        self.next_id += 1

    def complete_task(self, task_id):
        try:
            task_id = int(task_id)
            if task_id in self.tasks:
                self.tasks[task_id]["completed"] = True
                print(f"Задача #{task_id} отмечена как выполненная.")
            else:
                print(f"Ошибка: Задача #{task_id} не найдена.")
        except ValueError:
            print("Ошибка: ID задачи должен быть числом.")

    def remove_task(self, task_id):
        try:
            task_id = int(task_id)
            if task_id in self.tasks:
                task_text = self.tasks[task_id]["task"]
                del self.tasks[task_id]
                print(f"Задача #{task_id} '{task_text}' удалена.")
            else:
                print(f"Ошибка: Задача #{task_id} не найдена.")
        except ValueError:
            print("Ошибка: ID задачи должен быть числом.")

    def list_tasks(self):
        if not self.tasks:
            print("Список задач пуст.")
            return
        print("\nСписок задач:")
        for task_id, task_info in self.tasks.items():
            status = "Выполнено" if task_info["completed"] else "Не выполнено"
            print(f"{task_id}. [{status}] {task_info['task']}")


def menu_add_task(todo_list):
    task = input("Введите задачу для добавления: ")
    todo_list.add_task(task)


def menu_list_tasks(todo_list):
    todo_list.list_tasks()


def menu_complete_task(todo_list):
    todo_list.list_tasks()
    task_id = input("Введите ID задачи для отметки выполнения: ")
    todo_list.complete_task(task_id)


def menu_remove_task(todo_list):
    todo_list.list_tasks()
    task_id = input("Введите ID задачи для удаления: ")
    todo_list.remove_task(task_id)


def main():
    todo = ToDoList()

    function_menu = {
        "1": ("Добавить задачу", menu_add_task),
        "2": ("Вывод списка задач", menu_list_tasks),
        "3": ("Отметить задачу как выполненную", menu_complete_task),
        "4": ("Удалить задачу", menu_remove_task),
    }

    while True:
        print("\nМЕНЮ:")
        for key, value in function_menu.items():
            print(f"{key}. {value[0]}")
        choice = input("Выберите пункт меню: ")
        if choice in function_menu:
            function_menu[choice][1](todo)
        else:
            print("Неверный пункт меню. Попробуйте снова.")


if __name__ == "__main__":
    main()