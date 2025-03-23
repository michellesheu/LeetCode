class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # build a hashmap for s to keep track of char freq
        # iterate through t 
        # if t char in s hashmap delete t from s hashmap
        # if hashmap value < 0 then return false
        # if hashmap values = 0 for all chars then true 
        s_count = Counter(s)
        for ch in t:
            if ch in s_count:
                s_count[ch] -= 1
                if s_count[ch] < 0:
                    return False
            else:
                return False
        return all(value == 0 for value in s_count.values())