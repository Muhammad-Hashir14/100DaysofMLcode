class Employee:
    def __init__(self,fname,lname,sallary):
        self.fname = fname
        self.lname = lname
        self.sallary = sallary
    @property
    def email(self):
        return f"{self.fname}.{self.lname}@email.com"
    @property
    def fullname(self):
        return f"{self.fname} {self.lname}"
    @fullname.setter
    def f_name(self,name):
        first,last = name.split(" ")
        self.fname = first
        self.lname = last
    @fullname.deleter
    def fullname(self):
        self.fname = None
        self.lname = None
emp1 = Employee("Hashir","khatri",200000)
print(emp1.email)
emp1.fname = "talha"
print(emp1.email)
print(emp1.fullname)
emp1.f_name = "umar aziz"
print(emp1.fullname)
del emp1.fullname
print(emp1.fullname)