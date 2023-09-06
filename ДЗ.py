class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.marks = []

    def mark_lecturer(self, lecturer, course, mark):
        if (isinstance(lecturer, Lecturer)
                and course in lecturer.courses_attached
                and course in self.courses_in_progress):
            if course in lecturer.grades:
                lecturer.grades[course] += [mark]
                lecturer.marks += [mark]
            else:
                lecturer.grades[course] = [mark]
                lecturer.marks += [mark]
        else:
            return 'Ошибка'

    def __str__(self):
        s_marks = sum(self.marks)
        l_marks = len(self.marks)
        res = (f"Имя: {self.name}\n"
               f"Фамилия: {self.surname}\n"
               f"Средняя оценка за домашнее задание: {round(s_marks / l_marks, 2) if l_marks != 0 else 0}\n"
               f"Курсы в процессе изучения: {', '.join(self.courses_in_progress)}\n"
               f"Завершенные курсы: {', '.join(self.finished_courses)}")
        return res

    def __lt__(self, other):
        if not isinstance(other, Student):
            print(f'{other} не студент!')
            return
        return (sum(self.marks) / len(self.marks)) < (sum(other.marks) / len(other.marks))


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if (isinstance(student, Student)
                and course in self.courses_attached
                and course in student.courses_in_progress):
            if course in student.grades:
                student.grades[course] += [grade]
                student.marks += [grade]
            else:
                student.grades[course] = [grade]
                student.marks += [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = (f"Имя: {self.name}\n"
               f"Фамилия: {self.surname}")
        return res


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        self.marks = []

    def __str__(self):
        s_marks = sum(self.marks)
        l_marks = len(self.marks)
        res = (f"Имя: {self.name}\n"
               f"Фамилия: {self.surname}\n"
               f"Средняя оценка за лекции: {round(s_marks / l_marks, 2) if l_marks != 0 else 0}")
        return res

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print(f'{other} не лектор!')
            return
        return (sum(self.marks) / len(self.marks)) < (sum(other.marks) / len(other.marks))


def comparison(list_names, course):
    marks_list = []
    for name in list_names:
        if isinstance(name, Lecturer):
            marks_list.extend(name.grades[course])
        if isinstance(name, Student):
            marks_list.extend(name.grades[course])
    return (f'Средняя оценка по курсу {course}: '
            f'{round(sum(marks_list) / len(marks_list), 2)}')


# Лекторы
lect1 = Lecturer('Yana', 'Bush')
lect1.courses_attached += ['Python']
lect1.courses_attached += ['JS']

lect2 = Lecturer('Roman', 'Black')
lect2.courses_attached += ['Python']
lect2.courses_attached += ['JS']

# Студенты
stud1 = Student('Ilya', 'Lyasota', 'male')
stud1.courses_in_progress += ['Python']
stud1.courses_in_progress += ['JS']
stud1.finished_courses += ['Введение в программирование']
stud1.finished_courses += ['Основы Git']

stud2 = Student('Kirill', 'White', 'male')
stud2.courses_in_progress += ['Python']
stud2.courses_in_progress += ['JS']
stud2.finished_courses += ['Введение в программирование']
stud2.finished_courses += ['Основы Git']

# Контролеры
rev1 = Reviewer('Nick', 'Fill')
rev1.courses_attached += ['Python']
rev1.courses_attached += ['JS']

rev2 = Reviewer('Bob', 'Bond')
rev2.courses_attached += ['Python']
rev2.courses_attached += ['JS']

# Оценка контролерами студентов
rev1.rate_hw(stud1, 'Python', 10)
rev1.rate_hw(stud1, 'Python', 10)
rev1.rate_hw(stud1, 'Python', 10)
rev1.rate_hw(stud1, 'JS', 6)
rev1.rate_hw(stud1, 'JS', 7)
rev1.rate_hw(stud1, 'JS', 5)

rev2.rate_hw(stud2, 'Python', 4)
rev2.rate_hw(stud2, 'Python', 2)
rev2.rate_hw(stud2, 'Python', 7)
rev2.rate_hw(stud2, 'JS', 7)
rev2.rate_hw(stud2, 'JS', 2)
rev2.rate_hw(stud2, 'JS', 7)

# Оценка студентами лекторов
stud1.mark_lecturer(lect1, 'Python', 5)
stud1.mark_lecturer(lect1, 'Python', 10)
stud1.mark_lecturer(lect1, 'Python', 7)
stud1.mark_lecturer(lect1, 'JS', 4)
stud1.mark_lecturer(lect1, 'JS', 2)
stud1.mark_lecturer(lect1, 'JS', 6)

stud1.mark_lecturer(lect1, 'Python', 1)
stud1.mark_lecturer(lect1, 'Python', 10)
stud1.mark_lecturer(lect1, 'Python', 4)
stud1.mark_lecturer(lect1, 'JS', 6)
stud1.mark_lecturer(lect1, 'JS', 1)
stud1.mark_lecturer(lect1, 'JS', 9)

stud2.mark_lecturer(lect2, 'Python', 2)
stud2.mark_lecturer(lect2, 'Python', 4)
stud2.mark_lecturer(lect2, 'Python', 6)
stud2.mark_lecturer(lect2, 'JS', 3)
stud2.mark_lecturer(lect2, 'JS', 7)
stud2.mark_lecturer(lect2, 'JS', 1)

stud2.mark_lecturer(lect2, 'Python', 1)
stud2.mark_lecturer(lect2, 'Python', 10)
stud2.mark_lecturer(lect2, 'Python', 4)
stud2.mark_lecturer(lect2, 'JS', 6)
stud2.mark_lecturer(lect2, 'JS', 1)
stud2.mark_lecturer(lect2, 'JS', 9)

# Вывод
print('__Студенты__')
print(stud1)
print()
print(stud2)
print()
print(stud1 < stud2, stud1 > stud2)
print()

print('__Лекторы__')
print(lect1)
print()
print(lect2)
print()
print(lect1 < lect2, lect1 > lect2)
print()

print('__Контролер__')
print(rev1)
print()
print(rev2)
print()

# Используем внешнюю функцию
print('__Средняя оценка по курсу__')
student_list = [stud1, stud2]
lecturer_list = [lect1, lect2]
print(comparison(student_list, 'Python'))
print(comparison(student_list, 'JS'))
print(comparison(lecturer_list, 'Python'))
print(comparison(lecturer_list, 'JS'))

