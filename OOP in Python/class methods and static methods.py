import datetime
class Employee:
    inc = 1.06
    def __init__(self, firstname , lastname , sallary):
        self.firstname = firstname
        self.lastname  = lastname
        self.sallary = sallary
    def fullname(self):
        return f"{self.firstname} {self.lastname}"
    @classmethod
    def bonus(cls, amount):
        cls.bonus = amount
    def increament(self):
        self.sallary = self.sallary * Employee.inc
        return self.sallary
    @staticmethod
    def isaweekday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return True
        else:
            return False

employee_1 = Employee("Umar","Aziz",180000)
print(employee_1.firstname)
print(employee_1.fullname())
print(employee_1.sallary)
print(employee_1.increament())
employee_1 = Employee.bonus(1.2)
print(Employee.bonus)
employee_2 = Employee("Muhammad","owais",180000)
print(employee_2.increament())
data = datetime.date(2023,3,26)
print(Employee.isaweekday(data))