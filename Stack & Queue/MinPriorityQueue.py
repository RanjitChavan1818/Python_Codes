

class minPriorityQueue:
    def __init__(self,size):
        self.size=size
        self.arr=[0]*self.size
        self.count=0

    def isEmpty(self):
        return self.count==0

    def isFull(self):
        return self.count==self.size

    def enqueue(self,x):
        if self.isFull():
            print("Overflow")
            return
        self.arr[self.count]=x
        self.count+=1

    def dequeue(self):
        if self.isEmpty():
            print("Underflow")
            return

        minIndex=0
        for i in range(1,self.count):
            if self.arr[i]<self.arr[minIndex]:
                minIndex = i

        minValue=self.arr[minIndex]
        for i in range(minIndex,self.count-1):
            self.arr[i]=self.arr[i+1]

        self.count-=1

        return minValue

    def peek(self):
        if self.isEmpty():
            print("Underflow")
            return
        minValue=self.arr[0]
        for i in range(1,self.count):
            if self.arr[i]<minValue:
                minValue=self.arr[i]

        return minValue

    def display(self):
        if self.isEmpty():
            print("Underflow")
            return

        print("Priority Queue:",end=" ")
        for i in range(self.count):
            print(self.arr[i],end=" ")
        print()

pq=minPriorityQueue(5)

pq.enqueue(20)
pq.enqueue(50)
pq.enqueue(10)
pq.enqueue(40)

pq.display()
print(pq.dequeue())

# pq.display()
# print(pq.dequeue())

# pq.display()
# print(pq.dequeue())



