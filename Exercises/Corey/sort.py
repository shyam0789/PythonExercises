class Employee:
    def __init__(self,name,age,salary):
        self.name = name
        self.age = age
        self.salary = salary

    def __repr__(self):
        return f"{self.name},{self.age},{self.salary}"


e1 = Employee("Shyam",36,3000)
e2 = Employee("Mowni",33,4000)
e3 = Employee("X",40,5000)

emp_list = [e1,e2,e3]

def sort_employee(emp):
    return emp.name

sorted_emp_list = sorted(emp_list,key=sort_employee)
print(sorted_emp_list)

from operator import attrgetter
sorted_emp_list = sorted(emp_list,key=attrgetter("salary"),reverse=True)
print(sorted_emp_list)

