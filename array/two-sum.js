/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    charInd = {}
    for(let i = 0; i < nums.length; i++) {
        charInd[nums[i]] = i
    }
    console.log(charInd)
    for(let i = 0; i < nums.length; i++) {
        if(i != charInd[target-nums[i]] && target - nums[i] in charInd) {
            console.log(target-nums[i])
            return [i, charInd[target - nums[i]]]
        }
    }
};