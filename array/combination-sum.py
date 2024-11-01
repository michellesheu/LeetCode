class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:        
        results = []
        def backtrack(remain, comb, start):
            # make a deep copy of the current combination
            if remain == 0:
                results.append(list(comb))
                return 
            elif remain < 0:
                # exceed scope
                return
            for i in range(start, len(candidates)):
                comb.append(candidates[i])
                # give the current num another chance
                backtrack(remain - candidates[i], comb, i)
                #backtrack, remove num from combination
                comb.pop()
        backtrack(target, [], 0)
        return results

        