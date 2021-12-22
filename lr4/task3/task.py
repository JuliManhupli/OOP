from task3.abstract import *
from task3.config import *

cursor = db.cursor()


class CourseFactory(ICourseFactory):
    """
    This is a class for creating new courses and teachers
    """
    def create_course(self, course_name, course_program, course_type, teacher):
        """
        Method to create a new course
        :param course_name: name of course
        :param course_program: course
        :param course_type: course type (local or offsite)
        :param teacher: name of the teacher who is teaching the course

        :return: class instance LocalCourse or OffsiteCourse
        """
        if course_type == "local":
            self.add_course(course_name, course_program, "local", teacher)
            return LocalCourse(course_name, course_program, teacher)
        elif course_type == "offsite":
            self.add_course(course_name, course_program, "offsite", teacher)
            return OffsiteCourse(course_name, course_program, teacher)
        else:
            TypeError("Incorrect course type")

    def add_course(self, course_name, course_program, course_type, teacher):
        """
        Method that adds information about course to the database
        :param course_name: name of course
        :param course_program: course
        :param course_type: course type (local or offsite)
        :param teacher: name of the teacher who is teaching the course

        :return: None
        """
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
        """
        Method that returns information about all courses

        :return: tuple of courses data values
        """
        cursor.execute("SELECT course.course_name, course.course_type, course.course_program, teacher.teacher_name "
                       "FROM course JOIN teacher ON teacher.id = course.id_teacher")
        result = cursor.fetchall()
        return result

    def create_teacher(self, name):
        """
        Method for creating a new teacher
        :param name: name of teacher

        :return: class instance Teacher
        """
        self.add_teacher(name)
        return Teacher(name)

    def add_teacher(self, name):
        """
        Method that adds information about name to the database
        :param name: name of teacher

        :return: None
        """
        sql = "INSERT INTO teacher (teacher_name) VALUES (%s)"
        cursor.execute(sql, (name,))
        db.commit()

    def get_teacher(self):
        """
        Method that returns information about all teachers

        :return: tuple of teachers data values
        """
        cursor.execute("SELECT * FROM teacher")
        result = cursor.fetchall()
        all_teacher = dict(result)
        return all_teacher


class Teacher(ITeacher, ABC):
    """
    Class that stores information about a teacher
    """

    def __init__(self, name):
        """
        Class constructor Teacher
        :param name: name of teacher
        """
        self.name = name
        self.__courses = []

    @property
    def name(self):
        """
        Teacher name getter
        :return: name
        """
        return self.__name

    @name.setter
    def name(self, name):
        """
        Teacher name setter
        :param name: name
        :return: None
        """
        if not name:
            raise ValueError("Teacher name is not specified")
        if not isinstance(name, str):
            raise TypeError("Incorrect teacher name type")
        self.__name = name

    def add_course(self, course):
        """
        Method to add a course to the teacher's class
        :param course: class instance LocalCourse or OffsiteCourse
        :return: None
        """
        if not isinstance(course, (LocalCourse, OffsiteCourse)):
            raise TypeError("That is not a LocalCourse or OffsiteCourse type!")
        self.__courses.append(course)

    def __str__(self):
        """
        Objects in string form
        :return: string of class value
        """
        return f'Teacher {self.__name}'


class Course(ICourse):
    """
    Course class
    """
    def __init__(self, course_name, course_program, teacher):
        """
        Class constructor Course
        :param course_name: name of course
        :param course_program: course program
        :param teacher: name of teacher
        """
        self.course_name = course_name
        self.course_program = course_program
        self.teacher = teacher

    @property
    def course_name(self):
        """
        Course name getter
        :return: course_name
        """
        return self.__course_name

    @course_name.setter
    def course_name(self, course_name):
        """
        Course name setter
        :param course_name: name of course
        :return: None
        """
        if not course_name:
            raise ValueError("Course name is not specified")
        if not isinstance(course_name, str):
            raise TypeError("Incorrect course name type")
        self.__course_name = course_name

    @property
    def course_program(self):
        """
        Course program getter
        :return: course_program
        """
        return self.__course_program

    @course_program.setter
    def course_program(self, course_program):
        """
        Course program setter
        :param course_program: course program
        :return: None
        """
        if not isinstance(course_program, list):
            raise TypeError("Incorrect course program type")
        if not all(isinstance(value, str) for value in course_program):
            raise TypeError("That is not a str type!")
        self.__course_program = course_program

    @property
    def teacher(self):
        """
        Teacher getter
        :return: teacher
        """
        return self.__teacher

    @teacher.setter
    def teacher(self, teacher):
        """
        Teacher setter
        :param teacher: class instance Teacher
        :return: None
        """
        if not isinstance(teacher, Teacher):
            raise TypeError("That is not a Teacher type!")
        self.__teacher = teacher

    def __str__(self):
        """
        Objects in string form
        :return: string of class value
        """
        return f'Course: {self.__course_name}\n' \
               f'{self.__teacher}\n' \
               f'program {self.__course_program}\n'


class LocalCourse(ILocalCourse, Course):
    """
    Class of Local Courses
    Implements Course
    """

    def __init__(self, course_name, course_program, teacher):
        """
        Class constructor LocalCourse
        :param course_name: name of course
        :param course_program: course
        :param teacher: name of the teacher who is teaching the course
        """
        super().__init__(course_name, course_program, teacher)
        self.course_type = "local"

    def __str__(self):
        """
        Objects in string form
        :return: string of class value
        """
        return f'Local course: {self.course_name}\n' \
               f'{self.teacher}\n' \
               f'program {self.course_program}\n'


class OffsiteCourse(IOffsiteCourse, Course):
    """
    Class of Offsite Courses
    Implements Course
    """

    def __init__(self, course_name, course_program, teacher):
        """
        Class constructor OffsiteCourse
        :param course_name: name of course
        :param course_program: course
        :param teacher: name of the teacher who is teaching the course
        """
        super().__init__(course_name, course_program, teacher)
        self.course_type = "offsite"

    def __str__(self):
        """
        Objects in string form
        :return: string of class value
        """
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
