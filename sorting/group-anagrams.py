class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # create a dict with uniq key of sorted str anagram and value as list of str anagrams
        # iterate thru str in strs sort the str and add str to dict if in dict else add new entry
        # return list of dict values
        anagrams = []
        ana_strs = {}
        for str in strs:
            ana = ''.join(sorted(str))
            if ana in ana_strs:
                ana_strs[ana].append(str)
            else:
                ana_strs[ana] = [str]
        return list(ana_strs.values())