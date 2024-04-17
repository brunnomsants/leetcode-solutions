class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        
        posdic = {}
        for i in range(len(nums)):
            posdic[nums[i]] = i
        for i in range(len(nums)):
            if target - nums[i] in posdic and posdic[target-nums[i]] != i:
                return (i, posdic[target-nums[i]])                