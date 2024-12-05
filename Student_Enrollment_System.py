class Student:
    allo_prn=[]
    def __init__(self,stud):
       self.first_name=stud[0]
       self.middle_name=stud[1]
       self.last_name=stud[2]
       self.phone_number=stud[3]
       self.parent_name=stud[4]
       self.dob=stud[5]
       self.email_id=stud[6]
       self.addr=stud[7]
       self.caste=stud[8]
       self.marks=stud[9]
       self.yod=stud[10]
       self.adhnum=stud[11]
       self.generate_prn()
    
   
        
        

    def generate_prn(self):
        number=self.adhnum[6:12]
        prn=self.yod +self.caste+number
       
        if prn not in Student.allo_prn:
            Student.allo_prn.append(prn)
            print("prn is:",prn)
            self.admit()


    def admit(self):
        print("You are successfully admitted in COEP College")
        self.department()

    def department(self):
        
        print("\n 1.Cse \n2.ENTC \n3.Mech \n4.Electrical\n 5.Civil")
        a=int(input("Choose Departement "))

        if(a==1):
            print("You now successfully entered in CSE")
            self.courses()
        elif(a==2):
            print("Now you successfully enrolled in entc")
            self.courses()
        elif(a==3):
            print("Now you successfully enrolled in Mechanicl")
            self.courses()
        elif(a==4):
            print("Now you successfully enrooled in Electrical ")
            self.courses()
        elif(a==5):
            print("Now you are enrolled in Civil")
            self.courses()
        else:
            print("Enter a valid choice")
    def courses(self):
        print("The following are the courses alloted to you: ")
        print("1.Advanced Mathematics and Statistics \n 2.Discrete Mathematical Structure \n 3.Data Structure \n 4. Computer Graphics")

              



stud=[]
first_name=input("Enter your first name:")
middle_name=input("Enter middle name:")
last_name=input("Enter your last name")
phone_number=input("Enter your phone number:")
parent_name=input("Enter your parent full name")
dob=input("Enter your Date of Birth")
email_id=input("Enter your email id")
addr=input("Enter your address")
caste=input("Enter your caste")
marks=int(input("Enter your marks"))
year_of_ad=input("Enter year of admission")
adh_num=input("Enter a adhar number")

stud_info=[first_name,middle_name,last_name,phone_number,parent_name,dob,email_id,addr,caste,marks,year_of_ad,adh_num]



obj=Student(stud_info)
