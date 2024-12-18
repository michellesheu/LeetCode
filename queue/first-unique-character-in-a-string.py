class Solution:
    def firstUniqChar(self, s: str) -> int:
        ind_freq = [0] * 26
        for i in range(len(s)):
            ind_freq[ord(s[i])-ord('a')] += 1
        for i in range(len(s)):
            if ind_freq[ord(s[i])-ord('a')] == 1:
                return i
        return -1


