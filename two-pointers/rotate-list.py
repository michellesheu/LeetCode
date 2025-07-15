# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head
        length, tail = 1, head        
        # stop at last element and get length of list
        while tail.next:
            tail = tail.next
            length += 1
        k = k % length
        if k == 0:
            return head
        # last elem rotated points to old head
        curr = head
        # find pivot point curr
        for _ in range(length - k - 1):
            curr = curr.next
        # save new head which is after pivot point
        new_head = curr.next
        # new tail points to end
        curr.next = None
        # last element points to old head
        tail.next = head
        return new_head
