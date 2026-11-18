def RemoveNthNode(self,head,n):
    slow=head
    fast=head
    for _ in range(n):
        fast=fast.next

    if fast==None:
        return head.next

    while fast.next is not None:
        slow=slow.next
        fast=fast.next
    slow.next=slow.next.next
    return head

# fast pointer la n step chalwa
# check kara fast pointer none aahe ka, sel tr mag first element delet karaycha aahe
# Jr nasel tr fast pointer cha nect null yei paryant chalwa, sobat slow pan
# Jo delete karaycha element asel to slow cha next ch asel
# so, slow.next=slow.next.next