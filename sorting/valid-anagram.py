class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # input: s: string t: string lowercase english
        # output: return true if anagram (every char in s is in t/same frequency, same length)
        # make a dict of t's char freqs and use to keep track of frequencies in s that are in t and subtract if in t if freq < 0 return False if char not in t return False
        # t_chars {c:1,a:1,r:1}
        # O(s) time bc look through every char in s and O(1) lookup in dict
        # O(t) space to make dict of t's char keys
        if len(s) != len(t):
            return False
        t_chars = {}
        for char in t:
            t_chars[char] = t_chars.get(char, 0) + 1
        for char in s:
            if char in t_chars:
                t_chars[char] -= 1
                if t_chars[char] < 0:
                    return False
            else:
                return False
        return True
            