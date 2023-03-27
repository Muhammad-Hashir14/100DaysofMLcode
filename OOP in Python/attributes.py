# class attributes
class employee:
    increament = 1.08
    no_em = 0
    def __init__(self, Name, Designation, Salary):
        self.Name = Name
        self.Designation = Designation
        self.Salary = Salary
        employee.no_em  = self.no_em + 1
    def sal_inc(self):
        return self.Salary * employee.increament

emp_1 = employee("Bilal","Manager",30000)
print(emp_1.Salary)
print(emp_1.__dict__)
print(emp_1.sal_inc())
print(emp_1.__dict__)
emp_2 = employee("huzaifa","artist",40000)
print(emp_2.sal_inc())
print(employee.increament)
emp_1.increament = 1.1
print(emp_1.increament)
print(emp_1.sal_inc())
print(employee.no_em)
emp_3 = employee("owais","developer","50000")
print(employee.no_em)
