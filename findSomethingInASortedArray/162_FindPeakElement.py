"""
## Problem: Binary Search
## keyword: nums[i] != nums[i + 1]
## Think as an algo that constanly shrink the range to get all possible values at current situation
"""
from typing import List
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        
        ## the output
        result = nums[0] 

        ## the record
        l = 0
        r= len(nums)-1

        # check l <=r
        while (l<=r):
            # check l==r
            if l==r:
                result = l
                return result
            # count mid 
            mid = (l+r)//2
            # check nums[mid]<nums[mid+1]
            if nums[mid]<nums[mid+1]:
                # update l
                l = mid+1
            # check nums[mid]>nums[mid+1]
            if nums[mid]>nums[mid+1]:
                # update r 
                r = mid
## test cases
s= Solution()
print(s.findPeakElement([1,2,3,1])) #2
print(s.findPeakElement([1,2,1,3,5,6,4])) # 1,5