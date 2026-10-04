# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class NodeWrapper:
    def __init__(self, node):
        self.node = node

    def __lt__(self, other):
        return self.node.val < other.node.val

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []

        for head in lists:
            if head is not None:
                heapq.heappush(heap, NodeWrapper(head))

        dummy = ListNode()
        pointer = dummy

        while heap:
            curr_node = heapq.heappop(heap).node
            if curr_node.next is not None:
                heapq.heappush(heap, NodeWrapper(curr_node.next))
            pointer.next = curr_node
            pointer = pointer.next

        return dummy.next
