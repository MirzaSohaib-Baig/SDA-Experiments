from abc import ABC, abstractmethod

class Restraunt(ABC):

    @abstractmethod
    def __init__(self, num_of_employees):
        pass
    
    @abstractmethod
    def print_department(self):
        pass

class Cheif(Restraunt):
    
    def __init__(self, num_of_employees):
        self.num_of_employees = num_of_employees
 
    def print_department(self):
        print(f"Chiefs: {self.num_of_employees}")

class Waiter(Restraunt):
    
    def __init__(self, num_of_employees):
        self.num_of_employees = num_of_employees
        self.childs = []
 
    def print_department(self):
        print(f"Waiters: {self.num_of_employees}")
        total_emp_count = self.num_of_employees
        for child in self.childs:
            total_emp_count += child.num_of_employees
            child.print_department()
            print(f'Total employees: {total_emp_count}')

    def add_child_dept(self, dept): 
        self.childs.append(dept)
#
chief = Cheif(400)
waiter = Waiter(50)
waiter.add_child_dept(chief)
# print dept
waiter.print_department()