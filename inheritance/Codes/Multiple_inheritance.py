class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
class employee:
    def __init__(self,salary,cabin_no):
        self.salary=salary
        self.cabin_no=cabin_no
          

class Hod(person,employee):
    def __init__(self, name, age,designation,salary,cabin_no):
        self.designation=designation
        person.__init__(self,name, age)
        employee.__init__(self,salary,cabin_no)       


obj=Hod("Vaibhav","30","Head of CSE department","100000","R-5")
print(obj.salary)