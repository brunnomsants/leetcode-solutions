class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        setnums = set()
        for num in nums1:
            if num in nums2:
                setnums.add(num)
        return setnums
    
print(Solution.intersection(0, [1,2,2,1], [2,2]))
        