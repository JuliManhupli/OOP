import re
import datetime


class Person:

    def __init__(self, name, surname, phone, birth_date):
        self.name = name
        self.surname = surname
        self.phone = phone
        self.birth_date = birth_date

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if not name:
            raise TypeError("Name is not specified")
        if not isinstance(name, str):
            raise TypeError("Incorrect name type")
        self.__name = name

    @property
    def surname(self):
        return self.__surname

    @surname.setter
    def surname(self, surname):
        if not surname:
            raise TypeError("Surname is not specified")
        if not isinstance(surname, str):
            raise TypeError("Incorrect surname type")
        self.__surname = surname

    @property
    def phone(self):
        return self.__phone

    @phone.setter
    def phone(self, phone):
        if not isinstance(phone, str):
            raise TypeError("Incorrect phone type")
        pattern = re.compile("^[+]380\\d{9}$")
        if not pattern.match(phone):
            raise ValueError("Wrong phone format")
        self.__phone = phone

    @property
    def birth_date(self):
        return self.__birth_date

    @birth_date.setter
    def birth_date(self, birth_date):
        """Phone setter"""
        if not isinstance(birth_date, str):
            raise TypeError("Incorrect data type")
        if not datetime.datetime.strptime(birth_date, "%d.%m.%Y"):
            raise ValueError("Wrong data format")
        self.__birth_date = birth_date

    def __str__(self):
        return f"Name: {self.__name} {self.__surname}\nPhone: {self.__phone}\nDate of Birth: {self.__birth_date}\n"


class Notebook:

    def __init__(self, notebook = None):
        if notebook is None:
            notebook = []
        self.notebook = notebook

    @property
    def notebook(self):
        return self.__notebook

    @notebook.setter
    def notebook(self, notebook):
        if not isinstance(notebook, list):
            raise TypeError("Wrong type of people!")
        if not all(isinstance(person, Person) for person in notebook):
            raise ValueError("Wrong value of one of people!")
        self.__notebook = notebook

    def __add__(self, other):
        if isinstance(other, Person):
            if other in self.notebook:
                raise ValueError("This person is on the list")
            notebook = self.notebook.copy()
            notebook.append(other)
            return Notebook(notebook)
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, Person):
            if other not in self.notebook:
                raise ValueError("This person is not on the list.")
            notebook = self.notebook.copy()
            notebook.remove(other)
            return Notebook(notebook)
        return NotImplemented

    def __mul__(self, other):
        if isinstance(other, str):
            for person in self.notebook:
                if (person.value == other for _ in ("name", "surname", "phone", "birth_date")):
                    return person
        return NotImplemented

    def __iadd__(self, other):
        if isinstance(other, Person):
            if other in self.notebook:
                raise ValueError("This person is on the list")
            self.notebook.append(other)
            return self
        return NotImplemented

    def __isub__(self, other):
        if isinstance(other, Person):
            if other not in self.notebook:
                raise ValueError("This person is not on the list.")
            self.notebook.remove(other)
            return self
        return NotImplemented

    def __str__(self):
        all_records = ''.join(list(map(str, self.notebook)))
        return f"{all_records}"


if __name__ == "__main__":
    p1 = Person("First", "person", "+380508007020", "01.04.2000")
    p2 = Person("Second", "person", "+380508007021", "01.04.2000")
    p3 = Person("Third", "person", "+380508007022", "01.04.2000")

    d = Notebook()

    d = d + p3
    d += p2
    d += p1
    print(d)
    d = d - p2
    print(d)
    d = d * "+380508007022"
    print(d)

