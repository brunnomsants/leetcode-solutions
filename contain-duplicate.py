class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        dic = {}
        for i in nums:
            if(i in dic):
                return True
            dic[i] = 1
        return False
            