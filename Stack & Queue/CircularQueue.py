class myCircularQueue:
    def __init__(self,size):
        self.size=size
        self.arr=[0]*self.size
        self.front=-1
        self.rear=-1
    
    def enqueue(self,x):
        if ((self.rear+1)%self.size)==self.front:
            print("Overflow")
        else:
            self.rear=(self.rear+1)%self.size
            self.arr[self.rear]=x
            if self.front==-1:
                self.front=0
    
    def dequeue(self):
        if self.front==-1:
            print("Underflow")
            return
        else:
            val=self.arr[self.front]
            if self.front==self.rear:
                self.front=self.rear=-1
            else:
                self.front=(self.front+1)%self.size

        return val
    
    def isEmpty(self):
        return self.front==-1
    
    def isFull(self):
        return (self.rear+1)%self.size==self.front
    
    def display(self):
        if self.front==-1:
            print("Underflow")
            return
        else:
            print("Elements in Circular Queue:")
            if self.front<=self.rear:
                for i in range(self.front,self.rear+1):
                    print(self.arr[i])
            else:
                for i in range(self.front,self.size):
                    print(self.arr[i])
                for j in range(0,self.rear+1):
                    print(self.arr[j])
    
    


cq=myCircularQueue(4)
cq.enqueue(10)
cq.enqueue(20)
cq.enqueue(30)
cq.enqueue(40)
print("Is Circular Queue Full:","Yes" if cq.isFull() else "No")
cq.display()
cq.dequeue()
print("Array after deleting 1 elemnet")
cq.display()
# print(cq.isFull())


        