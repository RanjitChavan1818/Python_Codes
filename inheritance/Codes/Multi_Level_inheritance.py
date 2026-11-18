class Bank:
    def __init__(self,b_name,location):
        self.bank_name=b_name
        self.loc=location

    def display(self):
        print("Bank name: ",(self.bank_name))
        print("Bank Location:",(self.loc))    


class Branch(Bank):
    def __init__(self, b_name, location,no_employee,manager):
        self.employee=no_employee
        self.manager=manager


        Bank.__init__(self,b_name, location) 
    def Branch_info(self):
        print("Manager:",(self.manager))
        print("No of employee in beanch:",(self.employee))


class Customer(Branch):
    def __init__(self, customer_name,age,addr,b_name, location, no_employee, manager):
        self.name=customer_name
        self.age=age
        self.addr=addr

        super().__init__(b_name, location, no_employee, manager)                   

    def customer_Details(self):
        print("Name:",(self.name))
        print("Age:",(self.age))
        print("Address:",(self.addr))    

obj=Customer("Abhi",25,"Koshti galli","State Bank of India","Sangola",32,"Ranjit Chavan")  
obj.customer_Details()  
obj.display()    