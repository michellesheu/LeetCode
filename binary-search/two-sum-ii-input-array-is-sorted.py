class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # input: list of sorted nums in increasing order
        # output: return list of indices+1 that sum to target
        # use 2 ptrs for O(1) space constraint with left as lower and right as upper bound
        # while left < right
        # if num[left] + num[right] == target, return [left+1,right+1]
        # elif sum is too big, right -= 1
        # else (sum too small) left += 1
        left = 0
        right = len(numbers) - 1
        while left < right:
            t_sum = numbers[left] + numbers[right]
            if t_sum == target:
                return [left+1,right+1]
            elif t_sum > target:
                right -= 1
            else:
                left +=1