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
    def detecLoop(self):# Above code not important
        temp=self.head
        my_set=set()
        while temp is not None:
            if temp in my_set:
                return True

            my_set.add(temp)
            temp=temp.next
        return False 

    def detectLoopOptimal(self,head): 
        slow=head
        fast=head
        while fast != None and fast.next != None:
            slow=slow.next
            fast=fast.next.next
            if slow==fast:
                return True
        return False
    



