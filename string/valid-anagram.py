class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # input: s: string t: string lowercase english
        # output: return true if anagram (every char in s is in t/same frequency, same length)
        # make a dict of t's char freqs and use to keep track of frequencies in s that are in t and subtract if in t if freq < 0 return False if char not in t return False
        # t_chars {c:1,a:1,r:1}
        # O(n), n is length of both strings time bc look through every char in s and O(1) lookup in dict
        # O(k) = O(1) space to make dict of t's lowercase English char keys (26)
        if len(s) != len(t):
            return False
        t_chars = [0]*26
        for char in t:
            print(f"{char}= {ord(char)}= {ord(char)-ord('a')}=")
            t_chars[ord(char)-ord('a')] += 1
        for char in s:
            if t_chars[ord(char)-ord('a')] > 0:
                t_chars[ord(char)-ord('a')] -= 1
                if t_chars[ord(char)-ord('a')] < 0:
                    return False
            else:
                return False
        return True
            