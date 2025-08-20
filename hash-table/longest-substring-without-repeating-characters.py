class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''
        input: string 
        output: length of longest unique substring
        m: sliding window
        init left to 0
        init max_length = float("-inf")
        init set to keep track of unique chars seen so far
        for right in range(len(s))
        if s[right] not in uniq:
            add to uniq
            update max_length 
        else:
            delete s[left] from uniq
            left += 1
        return max_length if max_length != float("-inf") else 0
        '''
        left = 0
        max_length = float("-inf")
        uniq = set()
        for right in range(len(s)):
            while s[right] in uniq:
                uniq.remove(s[left])
                left += 1
            uniq.add(s[right])
            max_length = max(max_length, right-left+1)
        return max_length if max_length != float("-inf") else 0