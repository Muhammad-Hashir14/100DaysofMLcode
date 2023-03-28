class Employee:
    raise_amount = 1.06
    def __init__(self,fname,lname,sallary):
        self.fname = fname
        self.lname = lname
        self.sallary = sallary
    def fullname(self):
        return f"{self.fname} {self.lname}"
    def raisepay(self):
        self.sallary = self.sallary * Employee.raise_amount
        return self.sallary
class Developer(Employee):
    raise_amt = 1.2
    def __init__(self,fname,lname,sallary,role):
        super().__init__(fname,lname,sallary)
        self.role = role
    def raisepay(self):
        self.sallary = self.sallary * Developer.raise_amt
        return self.sallary
class Manager(Employee):
    def __init__(self,fname,lname,sallary,employees = None):
        if employees is None:
            self.employees = []
        else:
            self.employees = employees
    def add_emp(self,emp):
        self.emp = emp
        self.employees.append(self.emp)
    def remove_emp(self,emp):
        self.emp = emp
        employees.remove(self.emp)
    def display_emp(self):
        for employee in self.employees:
            print("-->",employee.fullname())

em1 = Employee("hashir","khatri",988989)
dv1 = Developer("Owais","liaquat",9000,"php")
emp2 = Employee("Bilal","khan",90888)
mn1 = Manager("Umar","Aziz",70000,[em1,dv1])
print(dv1.role)
print(dv1.raisepay())
print(mn1.display_emp())
mn1.add_emp(emp2)
print(mn1.display_emp())