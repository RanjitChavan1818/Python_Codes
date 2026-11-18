class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None

class DoublyLinkedList:
    def __init__(self):
        self.head=None

    def beginInsert(self,data):
        newNode=Node(data)
        if self.head is None:
            self.head=newNode
        else:
            newNode.next=self.head
            self.head.prev=newNode
            self.head=newNode

    def PairSum(self,target):
        my_set=set()
        temp=self.head
        result=[]
        while temp !=None:
            remaining=target-temp.data
            if remaining in my_set:
                result.append([remaining,temp.data])
            my_set.add(temp.data)
            temp=temp.next

        return result

dll=DoublyLinkedList()
dll.beginInsert(9)
dll.beginInsert(8)
dll.beginInsert(6)
dll.beginInsert(5)
dll.beginInsert(4)
dll.beginInsert(2)
dll.beginInsert(1)
print(dll.PairSum(7))