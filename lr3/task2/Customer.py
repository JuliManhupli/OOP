import re

class Customer:

    def __init__(self, name, surname, phone):
        self.__name = name
        self.__surname = surname
        self.__phone = phone

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
        pattern = re.compile("^+380\\d{9}$")
        if not pattern.match(phone):
            raise ValueError("Wrong phone format")
        self.__phone = phone

    def __str__(self):
        return f"Name: {self.__name} {self.__surname}\nPhone: {self.__phone}"
