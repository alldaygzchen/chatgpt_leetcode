"""
## Problem: Sliding window
# key word: positive integers
"""

from typing import List
class Solution:
    def minSubArrayLenBf(self, target: int, nums: List[int]) -> int:
        # the output
        min_len = float('inf')

        for r in range(len(nums)):
            
            # itself is equal or greater than target
            if nums[r] >= target:
                min_len = 1
                return min_len
            
            for l in range(0,r):
                current_sum = 0
                for i in range(l, r):
                    current_sum += nums[i] 
                # add the current r value since we are counting the sum of the subarray of the current r value
                current_sum += nums[r]
                if current_sum >= target:
                    min_len = min(min_len, r-l+1)
        
        return 0 if min_len == float('inf') else min_len
    
    # try to add some data structure to optimize the time complexity
    # data structure using varaibles is enough to store previous information
    
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # the output
        min_len = float('inf')
        # the record
        l = 0
        current_sum = 0
        
        
        for r in range(len(nums)):

            current_sum += nums[r]

            while current_sum >= target:
                min_len = min(min_len, r-l+1)
                current_sum -= nums[l]
                l += 1
        return 0 if min_len == float('inf') else min_len


    

# Test Cases
sol = Solution()
print(sol.minSubArrayLen(7, [2,3,1,2,4,3])) # 2
print(sol.minSubArrayLen(4, [1,4,4])) # 1
print(sol.minSubArrayLen(11, [1,1,1,1,1,1,1,1])) # 0