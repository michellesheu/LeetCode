class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # bc input strs is lowercase letters make tuple by converting arr of len 26 as a key signature of anagrams
        # char maps to index ex. 'a' is index 0, determine freq of each char and store in corresponding index
        # iterate through each char in str in strs and make key signature
        # return the values in dict

        freq_map = defaultdict(list)
        for str in strs:
            possible_chars = [0] * 26
            for ch in str:
                ch_index = ord(ch)-ord('a')
                possible_chars[ch_index] += 1
            freq_map[tuple(possible_chars)].append(str)
        return list(freq_map.values())

