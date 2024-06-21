class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        dic = {}
        for i in range(len(nums)):
            if(nums[i] in dic):
                dic[nums[i]] += 1
            else:
                dic[nums[i]] = 1
        major = 0
        for i in dic:
            if dic[i] > len(nums) / 2:
                major = i
                return major
        return 0