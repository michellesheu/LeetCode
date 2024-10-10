class Solution:
    def longestPalindrome(self, s: str) -> int:
        freq_map = {}
        for ch in s:
            freq_map[ch] = freq_map.get(ch, 0) + 1
            res = 0
            has_odd_freq = False
        print(freq_map)
        for ch in freq_map:
            print(ch)
            if freq_map[ch] % 2 == 0:
                res += freq_map[ch]
            else:
                res += freq_map[ch] - 1
                has_odd_freq = True
        if has_odd_freq:
            return res + 1
        return res
