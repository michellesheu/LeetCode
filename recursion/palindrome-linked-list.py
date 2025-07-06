# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return True

        # 1. Find the middle of the linked list
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # 2. Reverse the second half
        def reverse_ll(node):
            prev = None
            curr = node
            while curr:
                next_temp = curr.next
                curr.next = prev
                prev = curr
                curr = next_temp
            return prev
        
        second_half_reversed = reverse_ll(slow)

        # 3. Compare the first and reversed second halves
        first_half = head
        while second_half_reversed:
            if first_half.val != second_half_reversed.val:
                return False
            first_half = first_half.next
            second_half_reversed = second_half_reversed.next
            
        return True