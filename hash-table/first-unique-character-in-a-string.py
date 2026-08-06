from collections import Counter
class Solution:
    def firstUniqChar(self, s: str) -> int:
        # input: string s 
        # brute force: iterate through s at each ch and index and check if that ch is at every index after if it's not then return that index if the ch repeats then break and have to check next character in the s until the end of s. if reach end of s, return -1
        # output: return index of first uniq ch else return -1 if only duplicates
        # use a set of ch and index tuple to keep track of seen uniq chs and their index
        # iterate thru s 
        # if ch in seen then remove ch and index and continue from next ch at the index + 1 after the previously seen ch and index
        # else add ch,index to seen (this will be earliest uniq ch)
        # return seen's index val if there is one in seen else return -1 after for loop 
        s_freq = Counter(s)
        for i, ch in enumerate(s): 
            if s_freq[ch] == 1:
                return i
        return -1
        