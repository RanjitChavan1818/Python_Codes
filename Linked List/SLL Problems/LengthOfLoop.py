class Solution:
    def lengthOfloop(self,head):
        temp=head
        my_dict={}
        travel=0
        while temp is not None:
            if temp in my_dict:
                return travel-my_dict[temp]
            my_dict[temp]=travel
            travel+=1
            temp=temp.next

        return 0
    def optimal(self,head):
        slow=head
        fast=head
        while fast !=None and fast.next !=None:
            slow=slow.next
            fast=fast.next.next
            if slow==fast:
                slow=slow.next
                count=1
                while slow !=fast:
                    slow=slow.next
                    count+=1
                return count
        return 0
