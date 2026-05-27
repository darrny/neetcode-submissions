# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # initialise a dummy list
        # while both lists still exist
        # compare the first value of the two lists
            # if value of first list is lower than value of second list, put that value in the dummy list, then update first list to its tail
            # else, do the same for second list
            # if one of the lists don't exist anymore, we just add the other list to the end of the dummy list
        dummy = node = ListNode()

        while list1 and list2:
            if list1.val < list2.val:
                node.next = list1
                list1 = list1.next
                node = node.next
            else:
                node.next = list2
                list2 = list2.next
                node = node.next
            
        if not list1:
            node.next = list2
        if not list2:
            node.next = list1

        return dummy.next