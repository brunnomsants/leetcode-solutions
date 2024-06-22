class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        setnuns = sorted(nums)
        lenrange = setnuns[len(setnuns)-1] + 2
        for i in range(0, lenrange):
            if i not in setnuns:
                return i
        return 0
        
        
print(Solution.missingNumber(0, [0,1]))