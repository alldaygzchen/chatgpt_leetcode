
"""
## Problem: Other
# Create a dictionary with the key of reviewed and the value of index
"""


from typing import List
class Solution:
    def twoSum_bf(self, nums: List[int], target: int) -> List[int]:
        for r in range(len(nums)):
            # check different values of l to get the sum of the target
            for l in range(0,r):
                if nums[l] + nums[r] == target:
                    return [l,r]
                
    # try to add some data structure to optimize the time complexity 
    # hashmap is efficient to retrieve information about all elements up to the current element          
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # the record
        sum_dict = {}
        
        for r in range(len(nums)):
            # check sun_dict has record of target - nums[r]
            if target - nums[r] in sum_dict:
                return [sum_dict[target - nums[r]], r]
            sum_dict[nums[r]] = r



    
# Test Cases
sol = Solution()
print(sol.twoSum([2,7,11,15], 9)) # [0,1]
print(sol.twoSum([3,2,4], 6)) # [1,2]
print(sol.twoSum([3,3], 6)) # [0,1]