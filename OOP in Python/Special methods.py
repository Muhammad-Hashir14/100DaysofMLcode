print('test'.__len__())
class Employee:
    def __init__(self, fname,lname,sallary):
        self.fname = fname
        self.lname = lname
        self.sallary = sallary
    def fullname(self):
        return f"{self.fname} {self.lname}"
    def __repr__(self):
        return f"Employee({self.fname} - {self.lname} - {self.sallary})"
    def __str__(self):
        return f"Employee FullName : {emp1.fullname()})"
    def __add__(self,other):
        return self.sallary + other.sallary
    def __sub__(self,other):
        return self.sallary - other.sallary
    def __mul__(self,other):
        return self.sallary * other.sallary
emp1 = Employee("umar","Aziz",6454)
emp2 = Employee("owais","Aziz",7000)

print(emp1.fullname())
print(emp1.__repr__())
print(emp1.__str__())
print(emp1 + emp2)
print(emp1 - emp2)
print(emp1 * emp2)

# Calculator
class calculator:
    first_number = 0
    second_number = 0
    def __init__(self):
        calculator.first_number = int(input("Enter your Number : "))

    def __add__(self,other):
        return calculator.first_number + other.first_number

num1 = calculator()
num2 = calculator()
print(num1 + num2)