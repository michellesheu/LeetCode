# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        odd_tail = head
        even_tail = head.next
        even_head = even_tail
        # even will be at end of list
        while even_tail and even_tail.next:
            odd_tail.next = odd_tail.next.next
            even_tail.next = even_tail.next.next
            odd_tail = odd_tail.next
            even_tail = even_tail.next
        odd_tail.next = even_head
        return head