class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy  # prev initially points to dummy
        
        while prev.next and prev.next.next:
            # identify the two nodes to swap
            first = prev.next
            second = first.next
            
            # swapping logic
            prev.next = second
            first.next = second.next
            second.next = first
            
            # move prev pointer forward by two nodes for next swap
            prev = first
        
        return dummy.next
