class Student:
    def __init__(self,roll_no,name,marks):
        self.name=name
        self.roll_no=roll_no
        self.marks=marks

    def display(self):
        print(f"Name:{self.name}")
        print(f"Roll No:{self.roll_no}")
        print(f"Marks:{self.marks}")
        print(f"Percentage:{self.percentage():.2f}%")
        if sum(self.marks)>=120:
            print("Result : Pass")
        else:
            print("Result : Fail")

    def percentage(self):
        return (sum(self.marks)/300)*100

Students=[]
while True:
    print("1.Add Student\n 2.Display Student\n 3.Display all students data\n 4.Exit")
    ch=int(input("Enter a choice:"))
    match ch:
        case 1: 
            name=input("Enter a name:")
            roll_no=int(input("Enter a roll No:"))
            marks = list(map(int, input("Enter numbers: ").split()))
            student=Student(roll_no,name,marks)
            Students.append(student)

        case 2:
            x=int(input("Enter a roll no:"))
            for student in Students:
                if student.roll_no==x:
                    student.display()
                    break
                else:
                    print("Student not found")

        case 3:
            for student in Students:
                student.display()

        case 4:
            print("Application closing...")
            break
        case _:
            print("Envalid Choice!")

        
