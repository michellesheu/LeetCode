class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # return list of lists of unique indexed triplet == 0 
        # sort array first to handle duplicate numbers in order
        # fix a number, use two pointers to get the additive inverse and update ptrs if sum too big or small, if sum is equal then add to output and move pointers toward each other, skip duplicate numbers in array and move pointers towards each other, end loop at len(nums)-1
        nums.sort()
        print(nums)
        output = []
        for i in range(len(nums)-1):
            if i != 0 and nums[i] == nums[i-1]:
                continue
            curr_target = -nums[i] # 1
            print(f"{curr_target=}")
            left = i + 1
            right = len(nums) - 1
            while left < right:
                print(f"{nums[left]=} {nums[right]=}")
                print(f"{nums[left] + nums[right]=}")
                if nums[left] + nums[right] == curr_target:
                    print("--------------------------------------")
                    print(f"{[nums[left], nums[right],nums[i]]=}")
                    output.append([nums[left], nums[right],nums[i]])
                    print(f"{output= }")
                    while left < len(nums) - 1 and nums[left] == nums[left+1]:
                        left += 1
                    while right < len(nums) - 1 and nums[right] == nums[right-1]:
                        right -= 1
                    left += 1
                    right -= 1
                    
                    print("--------------------------------------")
                elif nums[left] + nums[right] < curr_target:
                    left += 1
                else:
                    right -= 1
        return output


