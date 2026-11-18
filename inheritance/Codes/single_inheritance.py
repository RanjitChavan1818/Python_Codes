
class Teacher:
    def __init__(self, name, age, phone_num):
        self.name = name
        self.age = age
        self.phone_num = phone_num

    def display(self):
        print("Name: ", self.name)
        print("Age:", self.age)
        print("Phone Number:", self.phone_num)


class Student(Teacher):
    def __init__(self, name, age, phone_num, standard):
        self.standard = standard
        super().__init__(name, age, phone_num)

    def show(self):
        print("Standard:", self.standard)


obj = Student("Ranjit Netaji Chavan", "20", "9740094236", "2nd year B.tech")
print(obj.standard)  
