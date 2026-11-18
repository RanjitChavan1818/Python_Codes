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

    def endInsert(self,data):
        newNode=Node(data)
        if self.head is None:
            self.head=newNode
        else:
            curr=self.head
            while curr.next!=None:
                curr=curr.next

            curr.next=newNode
            newNode.prev=curr

    def locationInsert(self,data,loc):
        newNode=Node(data)
        if loc==0:
            self.beginInsert(data)
            return
        count=0
        curr=self.head
        while curr and count<loc-1:
            curr=curr.next
            count+=1
        newNode.next=curr.next
        newNode.prev=curr
        if curr.next :
            curr.next.prev=newNode
        curr.next=newNode
    def traversal(self):
        temp=self.head
        while temp is not None:
            print(temp.data,end="-->")
            temp=temp.next

    def beginDelete(self):
        if self.head==None:
            print("Doubly linked list is empty")
        else:
            temp=self.head
            self.head=temp.next
    def endDelete(self):
        if self.head==None:
            print("Doubly linked list is empty")
        elif self.head.next==None:
            self.head=None
        else:
            temp=self.head
            while temp.next.next !=None:
                temp=temp.next
            temp.next=None

    def specificDelete(self,x):
        if self.head.data==x:
            self.beginDelete()
        else:
            temp=self.head
            prev=None
            while temp is not None:
                if temp.data==x:
                    prev.next=temp.next
                prev=temp
                temp=temp.next

    def reverse(self):
        if self.head is None or self.head.next is None:
            return self.head
        else:
            prev=None
            curr=self.head
            while curr is not None:
                front=curr.next
                curr.next=prev
                curr.prev=front
                prev=curr
                curr=front

        self.head= prev

    def removeDuplicates(self,k):
        if self.head.next is None and self.head.data==k:
            return None

        new_head=self.head
        prev=None
        temp=self.head
        while temp is not None:
            if temp.data==k:
                if prev is not None:
                    prev.next=temp.next
                if temp.next is not None:
                    temp.next.prev=prev
                if temp==new_head:
                    new_head=new_head.next
            prev=temp
            temp=temp.next
        return new_head


dll=DoublyLinkedList()
dll.beginInsert(10)
dll.endInsert(20)
dll.endInsert(30)
dll.endInsert(40)
dll.locationInsert(35,4)
dll.traversal()
dll.reverse()

print()

dll.traversal()

            
