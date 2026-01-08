from abc import ABC, abstractmethod

class Employee(ABC):
    def __init__(self, name, id):
        self.name = name
        self.id = id

    @abstractmethod
    def calculate_wage(self):
        pass

class FullTimeEmployee(Employee):
    def __init__(self, name, id, salary):
        super().__init__(name, id)
        self.salary = salary

    def calculate_wage(self):
        return self.salary
    