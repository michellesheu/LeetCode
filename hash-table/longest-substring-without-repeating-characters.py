class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0 
        longest = 0
        res = []
        uniq = set()
        for r in range(len(s)):
            if s[r] not in uniq:
                uniq.add(s[r])
                longest = max(longest, r - l + 1)
            else:
                while s[r] in uniq:
                    uniq.remove(s[l])
                    l += 1 
                uniq.add(s[r])    
        return longest