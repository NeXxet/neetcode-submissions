# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        queue = deque()
        curr = head

        while curr:
            queue.append(curr)
            curr = curr.next

        dummy = ListNode()
        prev = dummy
        left = True
        while queue:
            if left:
                curr = queue.popleft()
                prev.next = curr
                prev = curr
                left = False
            else:
                curr = queue.pop()
                prev.next = curr
                prev = curr
                left = True
        
        curr.next = None