
class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:  
        seq = set(nums)
        ln = 0
        for i in nums:
            if i - 1 not in seq:
                f = i +1
                while f in seq:
                    f+=1
                ln = max(ln, f - i)    
        return ln