import collections
class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:
        res = []
        for key, value in collections.Counter(nums).items():
            if(value>len(nums)//3):
                res.append(key)
        return res