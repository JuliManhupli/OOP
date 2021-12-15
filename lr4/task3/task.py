from task3.abstract import *
from task3.connector_db import *

cursor = db.cursor()


class CourseFactory(ICourseFactory):

    def create_course(self, course_name, course_program, course_type, teacher):
        if course_type == "local":
            self.add_course(course_name, course_program, "local", teacher)
            return LocalCourse(course_name, course_program, teacher)
        elif course_type == "offsite":
            self.add_course(course_name, course_program, "offsite", teacher)
            return OffsiteCourse(course_name, course_program, teacher)
        else:
            TypeError("Incorrect course type")

    def add_course(self, course_name, course_program, course_type, teacher):
        id_teacher = 0
        all_teacher = self.get_teacher()
        for k, v in all_teacher.items():
            if v == teacher.name:
                id_teacher = k
        course_program = ', '.join([str(elem) for elem in course_program])
        sql = "INSERT INTO course (course_name, course_type, course_program, id_teacher) VALUES (%s, %s, %s, %s)"
        val = (course_name, course_type, course_program, id_teacher)
        cursor.execute(sql, val)
        db.commit()

    def get_course(self):
        cursor.execute("SELECT course.course_name, course.course_type, course.course_program, teacher.teacher_name "
                       "FROM course JOIN teacher ON teacher.id = course.id_teacher")
        result = cursor.fetchall()
        return result

    def create_teacher(self, name):
        self.add_teacher(name)
        return Teacher(name)

    def add_teacher(self, name):
        sql = "INSERT INTO teacher (teacher_name) VALUES (%s)"
        cursor.execute(sql, (name,))
        db.commit()

    def get_teacher(self):
        cursor.execute("SELECT * FROM teacher")
        result = cursor.fetchall()
        all_teacher = dict(result)
        return all_teacher


class Teacher(ITeacher, ABC):

    def __init__(self, name):
        self.name = name
        self.__courses = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Teacher name is not specified")
        if not isinstance(name, str):
            raise TypeError("Incorrect teacher name type")
        self.__name = name

    def add_course(self, course):
        if not isinstance(course, (LocalCourse, OffsiteCourse)):
            raise TypeError("That is not a LocalCourse or OffsiteCourse type!")
        self.__courses.append(course)

    def __str__(self):
        return f'Teacher {self.__name}'


class Course(ICourse):

    def __init__(self, course_name, course_program, teacher):
        self.course_name = course_name
        self.course_program = course_program
        self.teacher = teacher

    @property
    def course_name(self):
        return self.__course_name

    @course_name.setter
    def course_name(self, course_name):
        if not course_name:
            raise ValueError("Course name is not specified")
        if not isinstance(course_name, str):
            raise TypeError("Incorrect course name type")
        self.__course_name = course_name

    @property
    def course_program(self):
        return self.__course_program

    @course_program.setter
    def course_program(self, course_program):
        if not isinstance(course_program, list):
            raise TypeError("Incorrect course program type")
        if not all(isinstance(value, str) for value in course_program):
            raise TypeError("That is not a str type!")
        self.__course_program = course_program

    @property
    def teacher(self):
        return self.__teacher

    @teacher.setter
    def teacher(self, teacher):
        if not isinstance(teacher, Teacher):
            raise TypeError("That is not a Teacher type!")
        self.__teacher = teacher

    def __str__(self):
        return f'Course: {self.__course_name}\n' \
               f'{self.__teacher}\n' \
               f'program {self.__course_program}\n'


class LocalCourse(ILocalCourse, Course):

    def __init__(self, course_name, course_program, teacher):
        super().__init__(course_name, course_program, teacher)
        self.course_type = "local"

    def __str__(self):
        return f'Local course: {self.course_name}\n' \
               f'{self.teacher}\n' \
               f'program {self.course_program}\n'


class OffsiteCourse(IOffsiteCourse, Course):

    def __init__(self, course_name, course_program, teacher):
        super().__init__(course_name, course_program, teacher)
        self.course_type = "offsite"

    def __str__(self):
        return f'Offsite course: {self.course_name}\n' \
               f'{self.teacher}\n' \
               f'program {self.course_program}\n'


if __name__ == '__main__':
    c = CourseFactory()
    t1 = CourseFactory().create_teacher("Lisa")
    t2 = CourseFactory().create_teacher("Koy")
    c1 = CourseFactory().create_course('Python for beginners', ['Operators', 'Cycle', 'List'], 'offsite', t1)
    c2 = CourseFactory().create_course('Graphic Designer', ['Illustrator', 'Photoshop', 'InDesign'], 'local', t1)
    c3 = CourseFactory().create_course('Project Manager', ['Project management', 'Product management'], 'offsite', t2)
    for x in c.get_course():
        print(x)
