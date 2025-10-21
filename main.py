students = [
    {"name": "Harry", "grades": [80, 90, 78]},
    {"name": "Hermiona", "grades": [95, 90, 97]},
    {"name": "Ron", "grades": [60, 70, 64]},
    {"name": "Draco", "grades": [60, 75, 70]}
]


def calculate_average(grades):
    return sum(grades) / len(grades)


def average_point(students):
    total_score = 0
    for student in students:
        status_student = "Отстающий"
        if calculate_average(student["grades"]) > 75:
           status_student = "Успешен"
        total_score += calculate_average(student["grades"])/len(students)
        print(f"Студент: {student["name"]}", f"Средний балл: {round(calculate_average(student["grades"]), 2)}", f"Студент: {status_student} \n", sep="\n" )
    return print(f"Общий средний балл: {round(total_score, 2)}\n")


def laggard_student(students):
    worst_student = 0
    for i in range(len(students)):
        if i > 0:
           if calculate_average(students[i]["grades"]) < calculate_average(students[i-1]["grades"]):
            worst_student = i
    students.pop(worst_student)
    return students


average_point(students)


students.append({"name": "Sedrik", "grades": [85, 90, 98]})


average_point(students)


laggard_student(students)


average_point(students)

