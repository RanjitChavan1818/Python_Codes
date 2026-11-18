#push()-> 1) Transfer all element from stack1 to stack2
#         2) Insert Element to stack1
#         3) Transfer stack2 to stack1

#pop()-> top element of stack1

#peek()--> Return top element of satck1

class StackUsingQueue:
    def __init__(self):
        self.st1=[]
        self.st2=[]

    def push(self,x):
        while self.st1:
            self.st2.append(self.st1.pop())

        self.st1.append(x)

        while self.st2:
            self.st1.append(self.st2.pop())

    def pop(self):
        if not self.st1:
            print("Stack is empty")
            return -1
        top_element=self.st1.pop()
        return top_element

    def peek(self):
        if not self.st1:
            print("Stack is empty")
            return -1
        return self.st1[-1]

    def is_empty(self):
        return len(self.st1)==0