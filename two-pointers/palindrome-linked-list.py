# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # reverse the linked list 
        # iterate through both lists with two pointers and return false if val from lists doesn't match
        def reverse_ll(head):
            prev = None
            curr = head
            while curr:
                next = curr.next
                curr.next = prev
                prev = curr
                curr = next
            return prev # prev is at head of reversed ll
        ptr_og = head
        ptr_rev = reverse_ll(head)
        while ptr_og and ptr_rev:
            print(f"ptr_og val {ptr_og.val} ptr_rev val {ptr_rev.val}")
            if ptr_og.val != ptr_rev.val:
                return False
            ptr_og = ptr_og.next
            ptr_rev = ptr_rev.next
        return True