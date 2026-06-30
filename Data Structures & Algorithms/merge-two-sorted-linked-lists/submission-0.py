# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        curr_1 =list1
        curr_2 =list2
        list3  =ListNode()
        curr_3 =list3
        while curr_1 and curr_2:
            if curr_1.val<=curr_2.val:
                curr_3.next = ListNode(curr_1.val)
                curr_1 = curr_1.next
                curr_3 = curr_3.next
                
            else:
                curr_3.next = ListNode(curr_2.val)
                curr_2 = curr_2.next
                curr_3 = curr_3.next


        while curr_1:
            curr_3.next = ListNode(curr_1.val)
            curr_1 = curr_1.next
            curr_3 = curr_3.next
        
        while curr_2:
            curr_3.next = ListNode(curr_2.val)
            curr_2 = curr_2.next
            curr_3 = curr_3.next

        return list3.next

