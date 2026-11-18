# def hello():
#     print("Hello Ranjit")

#Now you want to print "Function started" before hello() runs.
# def hello():
#     print("Function started")
#     print("Hello Ranjit")
    # But this changes an original function

# With a decorator:

# def my_decorator(func):
#     def wrapper():
#         print("Function Started")
#         func()

#     return wrapper # if we don't return it, then TypeError found.'NoneType' object is not callable

# @my_decorator
# def hello():
#     print("Hello")

# hello()


# What exactly happens with @?
# @my_decorator
# def hello():
#     print("Hello Ranjit")

# ********** This is equivalent to:
# def hello():
#     print("Hello Ranjit")

# hello = my_decorator(hello)


#######----> Built-in decorators <-----------
# 1 @staticmethod
# 2 @classmethod
# 3 @property

class Student:
    @staticmethod
    def college_name():
        return "SKN Sinhgad College Of Engineering"

# You can call:
print(Student.college_name())
#Without creating an object
