class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest = 0
        l = 0
        freq = [0] * 26
        most_freq = 0 
        for r in range(len(s)):
            freq[ord(s[r]) - ord('A')] += 1
            most_freq = max(most_freq, freq[ord(s[r]) - ord('A')])
            
            # Adjust window size if replacements exceed `k`
            if (r - l + 1) - most_freq > k:
                freq[ord(s[l]) - ord('A')] -= 1
                l += 1
            
            # Update the longest valid window size
            longest = max(longest, r - l + 1)
        
        return longest
