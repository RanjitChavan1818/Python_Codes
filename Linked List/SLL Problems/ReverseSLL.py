
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

    def reverseLL(self):  # Main Code of reverse,  Just reversed the links
        temp=self.head
        prev=None
        
        while temp!=None:
            front=temp.next
            temp.next=prev
            prev=temp
        return prev