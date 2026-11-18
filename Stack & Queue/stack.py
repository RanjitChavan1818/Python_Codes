class myStack:
    def __init__(self,size):
        self.size=size
        self.arr=[0]*self.size
        self.top=-1

    #push operation
    def push(self,x):
        if self.top==self.size-1:
            print("Stack Overflow")
            return
        
        self.top+=1
        self.arr[self.top]=x

    #pop operation
    def pop(self):
        if self.top==-1:
            print("Underflow")
            return -1
        
        val=self.arr[self.top]
        self.top-=1
        return val
    
    # peak element
    def peak(self):
        if self.top==-1:
            print("Empty Stack")
            return
        return self.arr[self.top]
    
    # Check if stack is empty
    def isEmpty(self):
        return self.top==-1
    
    # Check if stack is full
    def isFull(self):
        return self.top==self.size-1
    


st=myStack(4)
st.push(10)
st.push(20)
st.push(30)
st.push(40)

print("Popped:",st.pop())

print("Top Element:",st.peak())

print("Is stack Empty:","Yes" if st.isEmpty() else "No")

print("Is stack Full:","Yes" if st.isFull() else "No")