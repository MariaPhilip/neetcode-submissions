# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        len_list=0
        curr=head
        while(curr):
            curr = curr.next
            len_list+=1

        pos = len_list -n
        print(pos)
        
        curr=prev=head
        if not pos:
            return head.next
        while(pos):
            prev = curr
            curr = curr.next
            pos-=1

        prev.next = curr.next

        return head




