# creating a simple class with no constructor or attributes
class Employee:
    pass
employee_1 = Employee()
employee_2 = Employee()

print(employee_1)
print(employee_2)

# giving information to instances
employee_1.name = "Umer"
employee_1.age = 21
employee_1.designation = "Deveoper"
employee_1.sallary = 80000

employee_2.name = "owais"
employee_2.age = 20
employee_2.designation = "Engineer"
employee_2.sallary = 79999

print(employee_1.name)
print(employee_2.designation)

# creating new class with constructor and method
class Students:
    def __init__(self,st_name,st_id,st_section):
        self.st_name = st_name
        self.st_id = st_id
        self.st_section = st_section
    def st_fullinformtion(self):
        return f"Name : {self.st_name} :: ID : {self.st_id} :: Section : {self.st_section}"


st_1 = Students("umer","CSC-150","3C")
st_2 = Students("Talha","CSC-146","3C")
print(st_1.st_id)
print(st_2.st_name)

# full information of both students
print(st_1.st_fullinformtion())
print(st_2.st_fullinformtion())









