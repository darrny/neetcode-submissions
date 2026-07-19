# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(next = None)
        while head:
            temp = dummy.next
            dummy.next = head
            head = head.next
            dummy.next.next = temp
        return dummy.next