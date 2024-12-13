class Shop:
    def __init__(self, shop_name, location, t_employee, salary):
        self.S_name = shop_name
        self.loc = location
        self.t_employee = t_employee
        self.salary = salary
    
    def Shop_Details(self):
        print("Shop Name: ", self.S_name)
        print("Location: ", self.loc)
        print("Total Employees in shop: ", self.t_employee)

class Worker1(Shop):
    def __init__(self, shop_name, location, t_employee, salary, w1_name, phone_num, addr):
        
        Shop.__init__(self, shop_name, location, t_employee, salary)
        self.w1_name = w1_name
        self.phone_num = phone_num
        self.addr = addr

    def Worker1_details(self):
        print("Worker Name: ", self.w1_name)
        print("Worker Phone Number: ", self.phone_num)
        print("Worker Address: ", self.addr)

class Worker2(Shop):
    def __init__(self, shop_name, location, t_employee, salary, w2_name, designation, speciality):
       
        Shop.__init__(self, shop_name, location, t_employee, salary)
        self.w2_name = w2_name
        self.post = designation
        self.speciality = speciality

    def Worker2_details(self):
        print("Worker 2nd Name:", self.w2_name)
        print("Position in shop:", self.post)
        print("Speciality of worker 2nd is:", self.speciality)

class Customer(Worker1, Worker2):
    def __init__(self, shop_name, location, t_employee, salary, w1_name, phone_num, addr, w2_name, designation, speciality, name, number):
       
        Worker1.__init__(self, shop_name, location, t_employee, salary, w1_name, phone_num, addr)
        Worker2.__init__(self, shop_name, location, t_employee, salary, w2_name, designation, speciality)
        
        self.name = name
        self.number = number

    def Customer_Details(self):
        print("Customer Name: ", self.name)
        print("Customer Mobile Number:", self.number)


obj = Customer("Shree Grocery Store", "Sangola", 4, 15000, "Ganya", "9740052", "Ambikavasti", "Somya", "Manager", "Negotiation", "Suresh", 840502)
obj.Shop_Details()
