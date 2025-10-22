import collections
import bisect

class Solution:
    def maxFrequency(self, nums: list[int], k: int, numOperations: int) -> int:
        
        N = len(nums)
        
        # --- Step 1 & 2: Sort and Pre-calculate Frequencies ---
        
        # O(N log N)
        sorted_nums = sorted(nums) 
        
        # O(N)
        # We need the original frequencies (how many are *exactly* equal)
        counts = collections.Counter(nums)
        
        # We only need to check each unique number from nums as a target
        # O(N) in worst case
        potential_targets = set(nums) 
        
        max_freq = 0
        
        # --- Step 3: Iterate through potential targets ---
        # This loop runs O(N) times in the worst case
        for T in potential_targets:
            
            # --- Step 4: Find Candidates Quickly ---
            
            # O(1) average lookup
            # c_ambi: "ambiguous" group, can use keep or change tokens
            c_ambi = counts[T] 
            
            # O(log N)
            # Find the index of the first number >= T-k
            left_idx = bisect.bisect_left(sorted_nums, T - k)
            
            # O(log N)
            # Find the index of the first number > T+k
            right_idx = bisect.bisect_right(sorted_nums, T + k)
            
            # Total numbers in the range [T-k, T+k]
            c_total = right_idx - left_idx
            
            # c_pure: "pure change" group, *must* use change tokens
            c_pure = c_total - c_ambi
            
            # --- Step 5: Apply the Token Logic ---
            
            # We must use our change tokens on the pure group first.
            freq_from_pure = min(c_pure, numOperations)
            
            # See how many change tokens are left
            change_tokens_left = numOperations - freq_from_pure
            
            # See how many keep tokens we have
            keep_tokens = N - numOperations
            
            # The ambiguous group can use any of the keep tokens OR 
            # any of the leftover change tokens.
            available_tokens_for_ambi = keep_tokens + change_tokens_left
            freq_from_ambi = min(c_ambi, available_tokens_for_ambi)
            
            # The total frequency for this target T
            current_total_freq = freq_from_pure + freq_from_ambi
            
            # --- Step 6: Find the Maximum ---
            max_freq = max(max_freq, current_total_freq)
            
        return max_freq