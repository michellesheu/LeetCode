# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # fast and slow pointer at head
        # move fast 2 ahead of slow
        # check if fast.next and fast are null to avoid access null error if fast is at final node
        # slow will be at middle of list
        fast = head
        slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        return slow
        