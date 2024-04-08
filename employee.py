class Employee():
    # Initialize the object
    def __init__(self, name, employee_number):
        self.__name = name
        self.__employee_num = employee_number

    # Accessor for the __name attribute
    def get_name(self):
        return self.__name
    # Accessor for the __employee_number attribute
    def get_employee_number(self):
        return self.__employee_number
    # Mutator for the __name attribute
    def set_name(self, name):
        self.__name = name
    # Mutator for the __employee_number attribute
    def set_employee_number(self, employee_number):
        self.__employee_number = employee_number


class ProductionWorker(Employee):
    def __init__([self, name, employee_number, shift_number, pay_rate]):
        Employee.__init__(self, name, employee_number)
        self.__shift_number = shift_number
        self.__pay_rate = pay_rate
    # Accessor for the __shift_number attribute
    def get_shift_number(self):
        return self.__shift_number
    # Accessor for the __pay_rate attribute
    def get_pay_rate(self):
        return self.__pay_rate
    # Mutator for the __shift_number attribute
    def set_shift_number(self, shift_number):
        self.__shift_number = shift_number
    # Mutator __pay_rate attribute
    def set_pay_rate(self, pay_rate):
        self.__pay_rate = pay_rate