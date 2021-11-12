import json


class Event:

    def __init__(self, regular_tickets, advance_tickets, student_tickets, late_tickets, ticket_cost):
        self.regular_tickets = regular_tickets
        self.advance_tickets = advance_tickets
        self.student_tickets = student_tickets
        self.late_tickets = late_tickets
        self.ticket_cost = ticket_cost
        self.__advance_ticket_cost = round(self.__ticket_cost * 0.6, 2)
        self.__student_ticket_cost = round(self.__ticket_cost * 0.5, 2)
        self.__late_ticket_cost = round(self.__ticket_cost * 1.1, 2)
        Event.add_event_to_file(self)

    def add_event_to_file(self):
        information_about_event = {
            'Number of tickets': self.__regular_tickets,
            'Cost of regular tickets': self.__ticket_cost,
            'Number of advance tickets': self.__advance_tickets,
            'Cost of advance tickets': self.__advance_ticket_cost,
            'Number of student tickets': self.__student_tickets,
            'Cost of student tickets': self.__student_ticket_cost,
            'Number of late tickets': self.__late_tickets,
            'Cost of late tickets': self.__late_ticket_cost
        }
        with open('event.json', 'w') as f:
            json.dump(information_about_event, f)

    @property
    def regular_tickets(self):
        return self.__regular_tickets

    @regular_tickets.setter
    def regular_tickets(self, regular_tickets):
        if not isinstance(regular_tickets, int):
            raise TypeError("Incorrect type of number of advance tickets input")
        if not regular_tickets > 0:
            raise ValueError("Incorrect value of number of regular tickets input")
        self.__regular_tickets = regular_tickets

    @property
    def advance_tickets(self):
        return self.__advance_tickets

    @advance_tickets.setter
    def advance_tickets(self, advance_tickets):
        if not isinstance(advance_tickets, int):
            raise TypeError("Incorrect type of number of advance tickets input")
        if not advance_tickets > 0:
            raise ValueError("Incorrect value of number of advance tickets input")
        self.__advance_tickets = advance_tickets

    @property
    def student_tickets(self):
        return self.__student_tickets

    @student_tickets.setter
    def student_tickets(self, student_tickets):
        if not isinstance(student_tickets, int):
            raise TypeError("Incorrect type of number of student tickets input")
        if not student_tickets > 0:
            raise ValueError("Incorrect value of number of student tickets input")
        self.__student_tickets = student_tickets

    @property
    def late_tickets(self):
        return self.__late_tickets

    @late_tickets.setter
    def late_tickets(self, late_tickets):
        if not isinstance(late_tickets, int):
            raise TypeError("Incorrect type of number of late tickets input")
        if not late_tickets > 0:
            raise ValueError("Incorrect value number of late tickets input")
        self.__late_tickets = late_tickets

    @property
    def ticket_cost(self):
        return self.__ticket_cost

    @ticket_cost.setter
    def ticket_cost(self, ticket_cost):
        if not isinstance(ticket_cost, int):
            raise TypeError("Incorrect type of number of advance tickets input")
        if not ticket_cost > 0:
            raise ValueError("Incorrect value of number of regular tickets input")
        self.__ticket_cost = ticket_cost

    @staticmethod
    def get_cost():
        with open("event.json", "r") as f:
            data = json.load(f)
        cost_regular = data.get('Cost of regular tickets')
        return cost_regular

    @staticmethod
    def find_by_number(number):
        with open("tickets.json", "r") as f:
            data = json.load(f)
        for t in data:
            if t['Number'] == number:
                return t

    def __str__(self):
        return f"Event information:\n" \
               f"Number of regular tickets: {self.__regular_tickets}, cost {self.__ticket_cost}\n" \
               f"Number of regular tickets: {self.__advance_tickets}, cost {self.__advance_ticket_cost}\n" \
               f"Number of regular tickets: {self.__student_tickets}, cost {self.__student_ticket_cost}\n" \
               f"Number of regular tickets: {self.__late_tickets}, cost {self.__late_ticket_cost}\n"


class Ticket:
    recordTicket = []
    advance_tickets = 0
    student_tickets = 0
    late_tickets = 0

    def __init__(self, number, cost=Event.get_cost(),  ticket_type='Regular ticket'):

        self.number = number
        self.cost = cost
        self.type = ticket_type

        Ticket.add_ticket_to_file(self)
        Ticket.check_number_of_tickets()

    def add_ticket_to_file(self):
        ticket = {
            'Number': self.number,
            'Type': self.type,
            'Cost': self.cost
        }
        Ticket.recordTicket.append(ticket)
        with open('tickets.json', 'w') as f:
            json.dump(Ticket.recordTicket, f)

    @staticmethod
    def check_number_of_tickets():
        with open("event.json", "r") as f:
            data = json.load(f)
        max_tickets = data.get('Number of tickets')
        if len(Ticket.recordTicket) > max_tickets:
            raise Exception("Tickets expired")

    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self, number):
        for t in self.recordTicket:
            if t['Number'] == number:
                raise ValueError("Duplicate tickets' number")
        if not isinstance(number, int):
            raise TypeError("Incorrect type of number tickets input")
        if not number > 0:
            raise ValueError("Incorrect value of number tickets input")
        self.__number = number

    @property
    def cost(self):
        return self.__cost

    @cost.setter
    def cost(self, cost):
        if isinstance(cost, str):
            raise TypeError("Incorrect cost of tickets type input")
        if not cost > 0:
            raise ValueError("Incorrect cost of tickets value input")
        self.__cost = cost

    def __str__(self):
        return f"{self.type}: number {self.number}, cost {self.cost}"


class AdvanceTicket(Ticket):

    def __init__(self, number):
        with open("event.json", "r") as f:
            data = json.load(f)
        cost_advance = data.get('Cost of advance tickets')
        super().__init__(number, cost_advance, 'Advance ticket')
        AdvanceTicket.check_number_of_advance_tickets()

    @staticmethod
    def check_number_of_advance_tickets():
        Ticket.advance_tickets += 1
        with open("event.json", "r") as f:
            data = json.load(f)
        max_advance_tickets = data.get('Number of advance tickets')
        if Ticket.advance_tickets > max_advance_tickets:
            raise Exception("Advance tickets expired")


class StudentTicket(Ticket):

    def __init__(self, number):
        with open("event.json", "r") as f:
            data = json.load(f)
        cost_student = data.get('Cost of student tickets')
        super().__init__(number, cost_student, 'Student ticket')
        StudentTicket.check_number_of_student_tickets()

    @staticmethod
    def check_number_of_student_tickets():
        Ticket.student_tickets += 1
        with open("event.json", "r") as f:
            data = json.load(f)
        max_student_tickets = data.get('Number of student tickets')
        if Ticket.student_tickets > max_student_tickets:
            raise Exception("Student tickets expired")


class LateTicket(Ticket):

    def __init__(self, number):
        with open("event.json", "r") as f:
            data = json.load(f)
        cost_late = data.get('Cost of late tickets')
        super().__init__(number, cost_late, 'Late ticket')
        LateTicket.check_number_of_late_tickets()

    @staticmethod
    def check_number_of_late_tickets():
        Ticket.late_tickets += 1
        with open("event.json", "r") as f:
            data = json.load(f)
        max_late_tickets = data.get('Number of late tickets')
        if Ticket.late_tickets > max_late_tickets:
            raise Exception("Late tickets expired")


if __name__ == '__main__':
    o = Event(10, 2, 1, 2, 300)

    o1 = Ticket(1)
    o2 = AdvanceTicket(4)
    o3 = StudentTicket(3)
    o4 = LateTicket(6)
    # print(o)
    print(o1)
    print(o2)
    print(o3)
    print(o.find_by_number(6))
