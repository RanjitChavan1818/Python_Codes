class A:
    def ran(self):
        print("Ranjit")

class B(A):
    def log():
        print("Class B")

class C(A):
    def log():
        print("Class C")


class D(B,C):
    def new():
        print("Hello World")                        

obj=D
obj.log()
