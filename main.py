class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({"task": task, "completed": False})
        print(f"Задача '{task}' добавлена.")

    def complete_task(self, task):
        for t in self.tasks:
            if t["task"] == task:
                t["completed"] = True
                print(f"Задача '{task}' отмечена как выполненная.")
                return
        print(f"Ошибка: Задача '{task}' не найдена.")

    def remove_task(self, task):
        for t in self.tasks:
            if t["task"] == task:
                self.tasks.remove(t)
                print(f"Задача '{task}' удалена.")
                return
        print(f"Ошибка: Задача '{task}' не найдена.")

    def list_tasks(self):
        if not self.tasks:
            print("Список задач пуст.")
            return
        print("\nСписок задач:")
        for i, task_item in enumerate(self.tasks, 1):
            status = "Выполнено" if task_item["completed"] else "Не выполнено"
            print(f"{i}. [{status}] {task_item['task']}")


def menu_add_task():
    task = input("Введите задачу для добавления: ")
    todo.add_task(task)
    return todo


def menu_list_tasks():
    todo.list_tasks()


def menu_complete_task():
    task = input("Введите задачу для отметки выполнения: ")
    todo.complete_task(task)


def menu_remove_task():
    task = input("Введите задачу для удаления: ")
    todo.remove_task(task)


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
        "1": ("Добавить задачу", menu_add_task),
        "2": ("Вывод списка задач", menu_list_tasks),
        "3": ("Отметить задачу как выполненную", menu_complete_task),
        "4": ("Удалить задачу", menu_remove_task),
}


todo = ToDoList()
main()