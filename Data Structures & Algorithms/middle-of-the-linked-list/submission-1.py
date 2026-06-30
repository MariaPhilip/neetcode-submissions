# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow= head 
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

        

        # count = 0
        # curr = head
        # while curr:
        #     curr = curr.next
        #     count = count + 1

        # pos = int(count/2) 
        # print(pos)
        
        # curr = head
        # while curr:
        #     curr = curr.next
        #     pos = pos -1
        #     if pos == 0:
        #         head = curr
        #         break
        

        
        # return head
            



        

