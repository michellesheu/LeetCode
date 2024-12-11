class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # If lengths are different, it's not an anagram
        if len(s) != len(t):
            return False
        
        # Initialize character frequency array
        char_freq = [0] * 26
        
        # Count characters in s
        for c in s:
            char_freq[ord(c) - ord('a')] += 1
        
        # Subtract character counts using t
        for c in t:
            idx = ord(c) - ord('a')
            char_freq[idx] -= 1
            if char_freq[idx] < 0:
                return False
        return True
        
        


