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

    def endInsert(self,data):
        newNode=Node(data)
        temp=self.head
        while temp.next!=None:
            temp=temp.next
        temp.next=newNode

    def LocationInsert(self,data,loc):
        newNode=Node(data)
        prev=None
        count=0
        curr=self.head
        while curr !=None and count<loc:
            prev=curr
            curr=curr.next
            count+=1
        prev.next=newNode
        newNode.next=curr

    def traverse(self):
        if self.head==None:
            print("Empty Linked List")
        else:
            temp=self.head
            while  temp !=None:
                print(temp.data,end="-->")
                temp=temp.next

    def beginDelete(self):
        if self.head==None:
            print("SLL is empty")
        elif self.head.next==None:
            print("Only one element in Linked list")
            self.head=None
        else:
            temp=self.head
            self.head=temp.next

    def endDelete(self):
        if self.head==None:
            print("SLL is empty")
        elif self.head.next==None:
            print("Only one element in Linked list")
        else:
            prev=None
            curr=self.head
            while curr.next!=None:
                prev=curr
                curr=curr.next
            prev.next=None

    def specificDelete(self,target):
        if self.head == None:
            print("SLL is empty")
            return
        
        if self.head.data == target:
            self.head = self.head.next
            return
      
        
        prev=self.head
        curr=self.head.next
        while curr !=None:
            if curr.data==target:
               prev.next=curr.next
               return
                
            prev=curr
            curr=curr.next
    def middleElement(self):
        slow=self.head
        fast=self.head
        while fast !=None and fast.next!=None:
            slow=slow.next
            fast=fast.next.next
        print(slow.data)

    def reverseLL(self):
        temp=self.head
        prev=None
        
        while temp!=None:
            front=temp.next
            temp.next=prev
            prev=temp
        return prev




        
sll=SinglyLinkedList()
sll.beginInsert(10)
sll.endInsert(20)
sll.endInsert(30)
sll.endInsert(40)
sll.endInsert(50)
sll.endInsert(60)
sll.traverse()
print()
sll.middleElement()

print()
# sll.beginDelete()
# sll.traverse()
# print()
# sll.endDelete()
# sll.traverse()
# print()
# sll.specificDelete(40)
# sll.traverse()
