class myQueue:
    def __init__(self,size):
        self.size=size
        self.arr=[0]*self.size
        self.front=-1
        self.rear=-1

    def enqueue(self,x):
        if self.rear==self.size-1:
            print("Overflow")
            return
        if self.front==-1:
            self.front=0
        self.rear+=1
        self.arr[self.rear]=x

    def dequeue(self):
        if self.front==-1:
            print("Underflow")
            return
            
        
        val=self.arr[self.front]
        self.front+=1
        if self.front>self.rear:
            self.front=self.rear=-1
    
        return val
    
    def isEmpty(self):
        return self.front==-1
    
    def isFull(self):
        return self.rear==self.size-1
    
    def display(self):
        if self.front==-1:
            print("Queue is Empty")
        else:
            print("Element in Queue:")
            for i in range(self.front,self.rear+1):
                print(self.arr[i])
    

qu=myQueue(4)
qu.enqueue(10)
qu.enqueue(20)
qu.enqueue(30)
qu.enqueue(40)
print("Is Queue Full:","Yes" if qu.isFull() else "No")

qu.display()

print("Is Queue Empty:","Yes"if qu.isEmpty() else "No")


        