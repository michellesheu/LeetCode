import heapq

class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        n = len(nums)
        
        # Initialize the min-heap with (value, index)
        num_ind = [(nums[i], i) for i in range(n)]
        heapq.heapify(num_ind)
        
        # Perform k updates
        for _ in range(k):
            min_val, i = heapq.heappop(num_ind)
            # Multiply the smallest element
            min_val *= multiplier
            
            # Update the original array
            nums[i] = min_val
            
            # Push the updated value back into the heap
            heapq.heappush(num_ind, (min_val, i))
        
        return nums

