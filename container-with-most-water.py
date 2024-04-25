class Solution:
    def maxArea(self, height: list[int]) -> int:
        y = 0
        r = len(height) - 1
        l = 0
        while r>l:
            z = (r-l)*min(height[r], height[l])
            y = max(y, z)
            if(height[r]>height[l]):
                l+=1
            else:
                r-=1                

        return y
        
print(Solution.maxArea(0, [2,3,4,5,18,17,6]))