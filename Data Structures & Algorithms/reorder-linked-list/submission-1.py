# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        second_list = slow.next
        slow.next = None

        dummy = ListNode()

        while second_list:
            temp = second_list
            second_list = second_list.next
            temp.next = dummy.next
            dummy.next = temp

        first, second = head, dummy.next

        while second:
            temp_1 = first.next
            temp_2 = second.next
            first.next = second
            second.next = temp_1
            first = temp_1
            second = temp_2
            