# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        fast = head
        slow = head

        while(fast and fast.next):
            prev = slow
            slow = slow.next
            fast = fast.next.next

        l2 =slow.next
        slow.next = None

        
        curr = l2
        prev = None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        l2 = prev
        l1 = head

        l1_curr = l1
        l2_curr = l2
        
        while l1_curr and l2_curr:
            l1_next =l1_curr.next
            l2_next =l2_curr.next

            l1_curr.next = l2_curr
            l2_curr.next = l1_next

            l1_curr = l1_next
            l2_curr = l2_next

        return



        