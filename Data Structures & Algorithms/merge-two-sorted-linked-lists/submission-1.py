# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        ptr1 = list1
        ptr2 = list2
        dummy = ListNode()
        curr = dummy
        while ptr1 and ptr2:
            if ptr1.val <= ptr2.val:
                temp = ptr1.next
                curr.next = ptr1
                ptr1.next = None
                ptr1 = temp
            else:
                temp = ptr2.next
                curr.next = ptr2
                ptr2.next = None
                ptr2 = temp
            curr = curr.next
        
        if not ptr1:
            curr.next = ptr2
        else:
            curr.next = ptr1
        return dummy.next