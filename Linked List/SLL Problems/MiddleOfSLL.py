
# Using Tortoise-hare method
# By slow and Fast Pointer

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None


class SinglyLinkedList(Node):
    def __init__(self):
        self.head=None

    def beginInsert(self,data):
        newNode=Node(data)
        if self.head==None:
            self.head=newNode
        else:
            newNode.next=self.head
            self.head=newNode

    def middleElement(self):  # Main Logic
        slow=self.head
        fast=self.head
        while fast !=None and fast.next!=None:
            slow=slow.next
            fast=fast.next.next
        print(slow.data)