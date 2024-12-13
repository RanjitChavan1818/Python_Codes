class SyClassroom:
    def __init__(self,room_no,no_sub,cc):
        self.room_no=room_no
        self.no_sub=no_sub
        self.cc=cc


    def di_sy(self):
        print("Room No:",(self.room_no))
        print("No of Banches:",(self.no_sub))
        print("No of windows in room",(self.cc))


class Student1(SyClassroom):
    def __init__(self, room_no, no_sub, cc,s1_grade,s1_name):
        self.s1=s1_name
        self.s1_grade=s1_grade
        super().__init__(room_no, no_sub, cc)

    def s1_details(self):
        print("Student name:",(self.s1))  
        print("Student Geade:",(self.s1_grade))
        
class Student2(SyClassroom):
    def __init__(self, room_no, no_sub, cc,s2_grade,s2_name):
        self.s2_name=s2_name
        self.s2_grade=s2_grade
        super().__init__(room_no, no_sub, cc)
    def s2_details(self):
        print("Student name:",(self.s2_name))  
        print("Student Geade:",(self.s2_grade))
        

class Student3(SyClassroom):
    def __init__(self, room_no, no_sub, cc,s3_grade,s3_name):
        self.s3_name=s3_name
        self.s3_grade=s3_grade
        SyClassroom.__init__(self,room_no, no_sub, cc)
    def s3_details(self):
        print("Student name:",(self.s3_name))  
        print("Student Geade:",(self.s3_grade))
        
obj1=Student3(411,6,"Jaggu Dada",95,"Vibhav")
obj1.di_sy()