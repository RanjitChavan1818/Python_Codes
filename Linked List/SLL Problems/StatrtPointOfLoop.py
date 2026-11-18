def StPointtLoopOptimal(self):# Above code not important
    temp=self.head
    my_set=set()
    while temp is not None:
        if temp in my_set:
            return temp

        my_set.add(temp)
        temp=temp.next
    return None  # Time Complexity- O(N), Space Complexity- O(N)

def StPointtLoopOptimal(self,head):  #Optimal, T- O(N), S-O(1)
    slow=head
    fast=head
    while fast != None and fast.next != None:
        slow=slow.next
        fast=fast.next.next
        if slow==fast:
            slow=head
            while fast!=slow:
                slow=slow.next
                fast=fast.next
            return slow
    return None
