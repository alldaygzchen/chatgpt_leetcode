"""
## Problem: Binary Search
## Keyword:Sorted ,array unique
## Think as an algo that constanly shrink the range to get all possible values at current situation
## The binary search will return the index of one of the occurrences of the target value, but it is not guaranteed which one.
"""
from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        ## the result 
        result = -1
        ## the records
        l = 0
        r = len(nums)-1

        # check l<=r:
        while (l<=r):
            # count mid
            mid = (l+r)//2
            # check nums[mid] == target and return
            if nums[mid] == target:
                result = mid
                return result 
            # check nums[mid] > target and update 
            if nums[mid] > target:
                r= mid-1
            # check nums[mid] < target and update 
            if nums[mid] < target:
                l= mid+1
        # return 
        return result 
## test cases
s =Solution()
print(s.search([-1,0,3,5,9,12],9)) #4
print(s.search([-1,0,3,5,9,12],2)) #-1