class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        somarray = nums1+nums2
        somarray.sort()
        if(len(somarray) % 2 == 1): 
            return float(somarray[len(somarray)//2])
        return float((somarray[len(somarray)//2 - 1] + somarray[len(somarray)//2])/2.0)
