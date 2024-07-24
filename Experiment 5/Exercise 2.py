from abc import ABC, abstractmethod

class Employee:
    
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'{self.name}'


class EmployeeDB(ABC):

    @abstractmethod
    def work(self, name):
        pass

class Developer(EmployeeDB):
    
    def work(self, name):
        return f'{name} is a Developer'

class Analyst(EmployeeDB):
    
    def work(self, name):
        return f'{name} is an Analyst'

class Tester(EmployeeDB):
    
    def work(self, name):
        return f'{name} is a Tester'

class SoftwareEngineer(EmployeeDB):

    def work(self, name):
        return f"{name} is a Software Engineer"


name = Employee('Sohaib')
name2 = Employee('Haris')
name3 = Employee('Rimmel')
name4 = Employee('Hassan')
dev = Developer()
print(dev.work(name))
ana = Analyst()
print(ana.work(name2))
test = Tester()
print(test.work(name3))
se = SoftwareEngineer()
print(se.work(name4))