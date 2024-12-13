class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freq_strs = defaultdict(list)
        for s in strs:
            freq_strs[tuple(sorted(s))].append(s)
        print(freq_strs)
        return list(freq_strs.values())