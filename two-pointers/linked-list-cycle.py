# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # 3 2 0 4 -> 2
        #       s 
        #       f 
        # 3 2 0 4
        #     s
        #         f
        slow = fast = head
        while fast and slow.next:
            if fast == slow:
                return True
            slow = slow.next
            fast = fast.next.next
        return False
