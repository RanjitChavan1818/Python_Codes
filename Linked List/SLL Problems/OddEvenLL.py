#Given A linked list 
# Rearrange linked list, first connect all odd index(position) nodes then connect by even positions.
def OddEvenLL(self,head):
    if head is None or head.next is None:
        return head
    values=[]
    temp=head
    while temp and temp.next:
        values.append(temp.val)
        temp=temp.next.next #For odd index node

    temp=head.next #set at 2nd node
    while temp and temp.next:
        values.append(temp.val)
        temp=temp.next.next #For even index node

    temp=head
    index=0
    while temp is not None:
        temp.val=values[index]
        index+=1
        temp=temp.next

    return head


## Above is Brute Force Method
def optimal(self,head):
    if head is None or head.next is None:
        return head
    odd=head
    even=head.next
    even_head=even
    while even is not None and even.next is not None:
        odd.next=odd.next.next
        odd=odd.next
        even.next=even.next.next
        even=even.next
    odd.next=even_head
    return head
