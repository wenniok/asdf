from abc import ABC, abstractmethod

WORKLOAD = 8


class Department:
    def __init__(self, name, code):
        self.__name = name
        self.__code = code

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name


class Employee(ABC):
    def __init__(self, code, name, salary, department):
        self.code = code
        self.name = name
        self.salary = salary
        self.__department = department

    @abstractmethod
    def calc_bonus(self):
        pass

    def get_hours(self):
        return WORKLOAD

    def get_department(self):
        return self.__department.get_name()

    def set_department(self, department_name):
        self.__department.set_department(department_name)


class Manager(Employee):
    def __init__(self, code, name, salary):
        super().__init__(code, name, salary, Department("managers", 1))

    def calc_bonus(self):
        return self.salary * 0.15


class Seller(Employee):
    def __init__(self, code, name, salary):
        super().__init__(code, name, salary, Department("sellers", 2))
        self.__sales = 0

    def get_sales(self):
        return self.__sales

    def put_sales(self, valor):
        self.__sales += valor

    def calc_bonus(self):
        return self.__sales * 0.15
