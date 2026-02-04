class Employee:
    def __init__(self,id,name):
        self.id = id
        self.name = name

    def __repr__(self):
        return f"Name of the Employee: {self.name} & ID of the Employee: {self.id}"


emp1 = Employee(10655102,"Shyam Sundar Selvamani")

print(emp1)

del emp1.id
try:
    print(emp1.id)
except Exception as e:
    print(e)
del emp1
try:
    print(emp1)
except Exception as e:
    print(e)

