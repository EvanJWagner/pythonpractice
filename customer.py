class Person():
    # Initialize the object
    def __init__(self, name, address, phone):
        self.__name = name
        self.__address = address
        self.__phone = phone

    # Accessor for the __name attribute
    def get_name(self):
        return self.__name
    # Accessor for the __address attribute
    def get_address(self):
        return self.__address
    # Accessor for the __phone attribute
    def get_phone_number(self):
        return self.__phone
    # Mutator for the __name attribute
    def set_name(self, name):
        self.__name = name
    # Mutator for the __address attribute
    def set_address(self, address):
        self.__address = address
    # Mutator for the __phone attribute
    def set_phone_number(self, phone):
        self.__phone = phone


class Customer(Person):
    def __init__(self, name, address, phone, customer_number, mailing_list_status):
        Person.__init__(self, name, address, phone)
        self.__customer_number = customer_number
        self.__mailing_list_status = mailing_list_status
    # Accessor for the __customer_number attribute
    def get_customer_number(self):
        return self.__customer_number
    # Accessor for the __mailing_list_status attribute
    def get_mailing_list_status(self):
        return self.__mailing_list_status
    # Mutator for the __customer_number attribute
    def set_customer_number(self, customer_number):
        self.__customer_number = customer_number
    # Mutator __mailing_list_status attribute
    def set_mailing_list_status(self, mailing_list_status):
        self.__mailing_list_status = mailing_list_status
