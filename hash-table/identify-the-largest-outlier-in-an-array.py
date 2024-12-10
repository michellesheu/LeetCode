class Solution:
    def getLargestOutlier(self, nums: List[int]) -> int:
        # Initialize variables
        ans = float('-inf')  # Track the largest potential outlier
        total_sum = sum(nums)  # Calculate total sum of the array
        
        # Use a frequency dictionary with doubled keys
        freq = {}
        for n in nums:
            freq[n*2] = freq.get(n*2, 0) + 1
        
        # Find potential outliers
        for n in nums:
            # Calculate the target sum of special numbers
            target = total_sum - n
            
            # Check if target exists in frequency map
            # Two conditions for a valid outlier:
            # 1. Target appears at least twice 
            # 2. OR target appears once and is not the current number's doubled value
            if freq.get(target, 0) >= 2 or \
            (freq.get(target, 0) == 1 and target != n*2):
                # Update the largest potential outlier
                ans = max(ans, n)
        
        return ans