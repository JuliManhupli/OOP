from abc import abstractmethod, ABC


class ICourseFactory(ABC):
    """
    CourseFactory class interface
    """
    @abstractmethod
    def create_course(self, course_name, course_program, course_type, teacher):
        """ Method for creating a new course """
        pass

    @abstractmethod
    def add_course(self, course_name, course_program, course_type, teacher):
        """ Method for adding course information to the database """
        pass

    @abstractmethod
    def get_course(self):
        """ Method for displaying information about all courses """
        pass

    @abstractmethod
    def create_teacher(self, name):
        """ Method for creating a new teacher """
        pass

    @abstractmethod
    def add_teacher(self, name):
        """ Method for adding teacher information to the database """
        pass

    @abstractmethod
    def get_teacher(self):
        """ Method for displaying information about all teachers """
        pass


class ITeacher(ABC):
    """
    Teacher class interface
    """
    @property
    @abstractmethod
    def name(self):
        """ Teacher name getter """
        pass

    @name.setter
    @abstractmethod
    def name(self, name):
        """ Teacher name setter """
        pass

    @abstractmethod
    def add_course(self, course):
        """ Method for adding a course to a teacher class """
        pass

    @abstractmethod
    def __str__(self):
        pass


class ICourse(ABC):
    """
    Course class interface
    """
    @property
    @abstractmethod
    def course_name(self):
        """ Course name getter """
        pass

    @course_name.setter
    @abstractmethod
    def course_name(self, course_name):
        """ Course name setter """
        pass

    @property
    @abstractmethod
    def teacher(self):
        """ Teacher getter """
        pass

    @teacher.setter
    @abstractmethod
    def teacher(self, teacher):
        """ Teacher setter """
        pass

    @property
    @abstractmethod
    def course_program(self):
        """ Teacher setter """
        pass

    @course_program.setter
    @abstractmethod
    def course_program(self, course_program):
        """ Course program setter """
        pass

    @abstractmethod
    def __str__(self):
        pass


class ILocalCourse(ABC):
    """
    LocalCourse class interface
    """
    @abstractmethod
    def __str__(self):
        pass


class IOffsiteCourse(ABC):
    """
    OffsiteCourse class interface
    """
    @abstractmethod
    def __str__(self):
        pass




