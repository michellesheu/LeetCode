class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # input: strs a list of lowercase letter strings aka can use a 26 ch array
        # output: a list of list of anagrams (same freq of chars aka same len)
        # make hashmap to keep track of sortedchar_listofstr(sorted char is unique key) by checking if sortedchar in hashmap then add to list else add new key to hashmap
        # "aet":["ate", "eat", "tea"], "ant":[...], "abt":[...]
        # add hashmap values to output list
        sorted_ana = {}
        for s in strs:
            key = "".join(sorted(s))
            if key in sorted_ana:
                sorted_ana[key].append(s)
            else:
                sorted_ana[key] = [s]
        return list(sorted_ana.values())
