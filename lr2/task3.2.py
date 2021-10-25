
class Student:
    """
    Class Student
    This class stores information about a student
    It accepts 4 parameters:
    number of record book, name, surname and grades
    Class has a method for calculating the average score
    """
    recordBookNumbers = []

    def __init__(self, number, name, surname, grades):
        self.record_book = number
        self.name = name
        self.surname = surname
        self.grades = grades

    @property
    def record_book(self):
        return self.__record_book

    @record_book.setter
    def record_book(self, number):
        if not number:
            raise ValueError("Record book number is not specified")
        if not isinstance(number, int):
            raise TypeError("Incorrect record book number type")
        if number <= 0:
            raise ValueError("Incorrect value record book number")
        if number in self.recordBookNumbers:
            raise ValueError("Duplicate record book number")
        self.recordBookNumbers.append(number)
        self.__record_book = number

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Name is not specified")
        if not isinstance(name, str):
            raise TypeError("Incorrect name type")
        self.__name = name

    @property
    def surname(self):
        return self.__surname

    @surname.setter
    def surname(self, surname):
        if not surname:
            raise ValueError("Surname is not specified")
        if not isinstance(surname, str):
            raise TypeError("Incorrect surname type")
        self.__surname = surname

    @property
    def grades(self):
        return self.__grades

    @grades.setter
    def grades(self, grades):
        if not grades:
            raise ValueError("Grades are not specified")
        if not isinstance(grades, dict):
            raise TypeError("Incorrect grades type")
        if not all(isinstance(key, str) for key in grades.keys()):
            raise TypeError("Incorrect key type")
        if not all(isinstance(values, int) for values in grades.values()):
            raise TypeError("Incorrect values type")
        if not all(60 <= values <= 100 for values in grades.values()):
            raise ValueError("Grade must be between 0 and 100")
        self.__grades = grades

    def get_average_score(self):
        average_score = sum(self.__grades.values()) / len(self.__grades.values())
        return round(average_score, 2)

    def __str__(self):
        return f"Record book number {self.__record_book}\nName {self.__name} " \
               f"{self.__surname}\nGrades {self.__grades}"


class Group:
    """
    Class Group
    This class stores information about students in a group
    It accepts data parameters about students
    The class has a method for identifying the top 5 students
    """
    cout_of_students = 0
    sameName = []

    def __init__(self, *student):
        self.student = student

        for st in self.student:
            if st.name + st.surname in self.sameName:
                raise ValueError("Duplicate name and surname")
            self.sameName.append(st.name + st.surname)

        self.cout_of_students += 1
        if self.cout_of_students > 20:
            raise Exception("Too many students")

    @property
    def student(self):
        return self.__student

    @student.setter
    def student(self, value):
        self.__student = list(value)

    def add_student(self, student):
        self.student.append(student)
        self.cout_of_students += 1
        if self.cout_of_students > 20:
            raise Exception("Too many students")

    def del_product(self, student):
        self.student.remove(student)
        self.cout_of_students -= 1

    def five_best_students(self):
        average_score = {}
        for st in self.student:
            average_score[st.name + " " + st.surname] = st.get_average_score()
        sorted_average_score = {k: v for k, v in sorted(average_score.items(), key=lambda item: item[1], reverse=True)}
        return list(sorted_average_score.items())[0:5]

    def __str__(self):
        list_students = '\n'.join(list(map(str, self.student)))
        return f"Students: \n{list_students}\n"


if __name__ == '__main__':
    o1 = Student(1111, "One", "student", {
        "OOP": 71,
        "Database": 67,
        "English": 60
    })
    o2 = Student(2222, "Two", "student", {
        "OOP": 86,
        "Database": 97,
        "English": 92
    })
    o3 = Student(3333, "Three", "student", {
        "OOP": 81,
        "Database": 75,
        "English": 79
    })
    o4 = Student(4444, "Four", "student", {
        "OOP": 61,
        "Database": 65,
        "English": 69
    })
    o5 = Student(5555, "Five", "student", {
        "OOP": 86,
        "Database": 72,
        "English": 69
    })
    o6 = Student(6666, "Six", "student", {
        "OOP": 73,
        "Database": 75,
        "English": 60
    })
    print(o1.get_average_score())
    st1 = Group(o1, o2, o3, o4, o6)
    print(st1)
    st1.add_student(o5)
    print(st1)
    print(st1.five_best_students())
