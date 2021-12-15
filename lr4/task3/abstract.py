from abc import abstractmethod, ABC


class ICourseFactory(ABC):

    @abstractmethod
    def create_course(self, course_name, course_program, course_type, teacher):
        pass

    @abstractmethod
    def add_course(self, course_name, course_program, course_type, teacher):
        pass

    @abstractmethod
    def get_course(self):
        pass

    @abstractmethod
    def create_teacher(self, name):
        pass

    @abstractmethod
    def add_teacher(self, name):
        pass

    @abstractmethod
    def get_teacher(self):
        pass


class ITeacher(ABC):

    @property
    @abstractmethod
    def name(self):
        pass

    @name.setter
    @abstractmethod
    def name(self, name):
        pass

    @abstractmethod
    def add_course(self, course):
        pass

    @abstractmethod
    def __str__(self):
        pass


class ICourse(ABC):

    @property
    @abstractmethod
    def course_name(self):
        pass

    @course_name.setter
    @abstractmethod
    def course_name(self, course_name):
        pass

    @property
    @abstractmethod
    def teacher(self):
        pass

    @teacher.setter
    @abstractmethod
    def teacher(self, teacher):
        pass

    @property
    @abstractmethod
    def course_program(self):
        pass

    @course_program.setter
    @abstractmethod
    def course_program(self, course_program):
        pass

    @abstractmethod
    def __str__(self):
        pass


class ILocalCourse(ABC):

    @abstractmethod
    def __str__(self):
        pass


class IOffsiteCourse(ABC):

    @abstractmethod
    def __str__(self):
        pass




