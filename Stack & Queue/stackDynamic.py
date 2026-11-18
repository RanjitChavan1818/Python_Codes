class myStack:
    def __init__(self):
        self.arr=[]

    def push(self,x):
        self.arr.append(x)

    def pop(self):
        if not self.arr:
            print("Stack Underflow")
            return -1
        return self.arr.pop()
    
    def peak(self):
        if not self.arr:
            print("Stack Underflow")
            return -1
        return self.arr[-1]
    
    def isEmpty(self):
        return len(self.arr)==0
    
    def size(self):
        return len(self.arr)
    
st=myStack()
st.push(10)
st.push(20)
st.push(30)
st.push(40)

print("Popped Element:",st.pop())
print("Peak Element:",st.peak())
print("Is Stack Empty:", "Yes" if st.isEmpty() else "No")
print("Current size of stack:",st.size())