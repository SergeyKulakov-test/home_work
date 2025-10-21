students = [
    {"name": "Harry", "grades": [80, 90, 78]},
    {"name": "Hermiona", "grades": [95, 90, 97]},
    {"name": "Ron", "grades": [60, 70, 64]},
    {"name": "Draco", "grades": [60, 75, 70]}
]


def calculate_average(grades):
    return sum(grades) / len(grades)


def average_point(students):
    for student in students:
        status_student = "Отстающий"
        if calculate_average(student["grades"]) > 75:
           status_student = "Успешен"
        print(f"Студент: {student["name"]}")
        print(f"Средний балл: {round(calculate_average(student["grades"]), 2)}")
        print(f"Студент: {status_student} \n")
    return


def total_score(students):
    score = 0
    for student in students:
        score += calculate_average(student["grades"]) / len(students)
    print(f"Общий средний балл: {round(score, 2)}\n")
    return


def laggard_student(students):
    worst_student = 0
    for i in range(len(students)):
        if i > 0:
           if calculate_average(students[i]["grades"]) < calculate_average(students[i-1]["grades"]):
            worst_student = i
    students.pop(worst_student)
    return students


def add_student(students):
    name_student = input('Введите имя нового студента:  ')
    while True:
        try:
            grades_student = input('Введите оценки студента через пробел:  ')
            return students.append({"name": name_student, "grades": [float(grade) for grade in grades_student.split()]})
        except ValueError:
            print("Ошибка! Пожалуйста, вводите только числа.")


def students_control(students):
    if len(students) == 0:
        print("Список студентов пуст\n")
        add_student(students)
    average_point(students)
    total_score(students)
    add_student(students)
    average_point(students)
    total_score(students)
    laggard_student(students)
    average_point(students)
    total_score(students)
    return

students_control(students)





