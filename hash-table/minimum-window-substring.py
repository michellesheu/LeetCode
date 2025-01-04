from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""
        
        # Dictionary to count characters in t
        t_char_freq = Counter(t)
        required = len(t_char_freq)  # Number of unique characters in t
        
        # Sliding window pointers
        l, r = 0, 0
        
        # Current state of the window
        window_counts = {}
        formed = 0
        
        # Result tuple: (window length, left pointer, right pointer)
        ans = float("inf"), None, None
        
        while r < len(s):
            # Add character to the window
            char = s[r]
            window_counts[char] = window_counts.get(char, 0) + 1
            
            # Check if this character's frequency matches the required frequency in t
            if char in t_char_freq and window_counts[char] == t_char_freq[char]:
                formed += 1
            
            # Try to shrink the window while it satisfies the condition
            while l <= r and formed == required:
                char = s[l]
                
                # Save the smallest window
                if r - l + 1 < ans[0]:
                    ans = (r - l + 1, l, r)
                
                # Shrink the window from the left
                window_counts[char] -= 1
                if char in t_char_freq and window_counts[char] < t_char_freq[char]:
                    formed -= 1
                
                l += 1
            
            # Expand the window
            r += 1
        
        # Return the smallest window or an empty string if no such window exists
        return "" if ans[0] == float("inf") else s[ans[1]:ans[2] + 1]
