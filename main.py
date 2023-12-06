class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def show_info(self):
      print(f'Имя: {self.name}, Фамилия: {self.surname}, Пол: {self.gender}')

    def rate_hw(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'
        if grade > 10:
          return 'Оценка не может быть больше 10 баллов'

    def average(self):
        sum_gr = 0
        len_gr = 0
        for course in self.grades.values():
            sum_gr += sum(course)
            len_gr += len(course)
            average_grade = (sum_gr / len_gr)
        return average_grade

    def __lt__(self, other):
      return self.average() < other.average()

    def __str__(self):
      print(f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {round(self.average(), 2)}\nКурсы в процессе изучения: {' '.join([str(i) for i in self.courses_in_progress])} \nЗавершенные курсы:{' '.join([str(i) for i in self.finished_courses])}")
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    # def rate_hw(self, student, course, grade):
    #     if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
    #         if course in student.grades:
    #             student.grades[course] += [grade]
    #         else:
    #             student.grades[course] = [grade]
    #     else:
    #         return 'Ошибка'

    def show_info(self):
      print(f'Имя: {self.name}, Фамилия: {self.surname}')
class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
      print(f'Имя: {self.name}\nФамилия: {self.surname}')
class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
    def average(self):
        sum_gr = 0
        len_gr = 0
        for course in self.grades.values():
            sum_gr += sum(course)
            len_gr += len(course)
            average_grade = (sum_gr / len_gr)
        return average_grade

    def __lt__(self, other):
      return self.average() < other.average()

    def __str__(self):
      print(f'Имя: {self.name}\nФамилия: {self.surname},\nСредняя оценка за лекции: {round(self.average(), 2)}')


# cool_mentor.rate_hw(best_student, 'Python', 10)
# cool_mentor.rate_hw(best_student, 'Python', 10)
# cool_mentor.rate_hw(best_student, 'Python', 10)

best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']

student_1 = Student('Ivanov', 'Ivan', 'f')
student_1.courses_in_progress += ['Python']
student_1.finished_courses += ['Java']

mentor_1 = Mentor('Djek', 'Ripher')
mentor_1.courses_attached += ['Python']

cool_mentor = Mentor('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']

reviewer_1 = Reviewer('Petr', 'Petrov')
reviewer_1.courses_attached += ['Python']

reviewer_2 = Reviewer('Jek', 'Sparrow')
reviewer_2.courses_attached += ['Python']
reviewer_2.courses_attached += ['Java']

reviewer_1.rate_hw(best_student, 'Python', 10)
reviewer_1.rate_hw(best_student, 'Python', 10)
reviewer_1.rate_hw(best_student, 'Python', 10)

reviewer_2.rate_hw(student_1, 'Python', 10)
reviewer_2.rate_hw(student_1, 'Python', 8)

lector_1 = Lecturer('Uma', 'Turman')
lector_1.courses_attached += ['Python']

lector_2 = Lecturer('Sidor', 'Sidorovich')
lector_2.courses_attached += ['Python']

best_student.rate_hw(lector_1, 'Python', 10)
best_student.rate_hw(lector_1, 'Python', 8)

student_1.rate_hw(lector_2, 'Python', 2)
student_1.rate_hw(lector_2, 'Python', 3)
student_1.rate_hw(lector_2, 'Python', 5)

print(best_student.grades)

best_student.__str__()
student_1.__str__()

lector_1.__str__()
lector_2.__str__()

reviewer_1.__str__()
reviewer_2.__str__()

print(lector_1 < lector_2)
print(best_student < student_1)

spisok_stud = [best_student, student_1]
subjekt = 'Python'

def aver_rate_for_homework(spisok_stud, subjekt):   # мой рабочий вариант
  list_homework = []
  for i in spisok_stud:
    if subjekt not in i.courses_in_progress:
      average_course = f"Студент {i.name} не изучает курс {subjekt}"
    else:
      list_homework.append(i.average())
    if len(list_homework) != 0:
      average_course = f"Средняя оценка за домашние задания по всем студентам в рамках курса {subjekt} состовляет: {round(sum(list_homework) / len(list_homework), 2)}."
  print(average_course)

aver_rate_for_homework(spisok_stud, subjekt)

subjekt = 'Python с нуля'
aver_rate_for_homework(spisok_stud, subjekt)

spisok_lecturer = [lector_1, lector_2]
subjekt = 'Python'

def aver_rate_for_lessons(spisok_lecturer, subjekt):   # мой рабочий вариант
  list_lecturers = []
  for i in spisok_lecturer:
    if subjekt not in i.courses_attached:
      average_course = f"Лектор {i.name} не преподает на курсе {subjekt}"
    else:
      list_lecturers.append(i.average())
    if len(list_lecturers) != 0:
      average_course = f"Средняя оценка за лекции всех лекторов в рамках курса {subjekt} состовляет: {round(sum(list_lecturers) / len(list_lecturers), 2)}."
  print(average_course)

aver_rate_for_lessons(spisok_lecturer, subjekt)

subjekt = 'Python с нуля'
aver_rate_for_lessons(spisok_lecturer, subjekt)