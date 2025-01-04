"""
## Problem: Count frequencies
# key word: non-empty subarray
# Prefix sum: Create a cumulative sum as key and the count as value
# If the cumulative sum - k in the dictionary, increment the count
"""

from typing import List
class Solution:
    # time exceeds
    def subarraySumBf(self, nums: List[int], k: int) -> int:

        # the output
        count = 0

        for r in range(len(nums)):
            # itself is k
            if nums[r] == k:
                count += 1
            # check different subarrays current_sum = nums[l] + nums[l+1] + ... + nums[r]
            for l in range(0,r):
                current_sum = 0
                for i in range(l, r):
                    current_sum += nums[i] 
                # add the current r value since we are counting the sum of the subarray of the current r value
                current_sum += nums[r]
                if current_sum == k:
                    count += 1

        return count

    # try to add some data structure to optimize the time complexity
    # hashmap is efficient to retrieve information about all prefices
    def subarraySum(self, nums: List[int], k: int) -> int:

        # the output
        count = 0
        # the record
        sum_dict = {}
        
        cummulative_sum = 0

        for r in range(len(nums)):

            cummulative_sum += nums[r]

            if cummulative_sum == k:
                count += 1

            # check sum_dict has record of cummulative_sum - k
            if cummulative_sum - k in sum_dict:
                count += sum_dict[cummulative_sum-k]

            sum_dict[cummulative_sum] = sum_dict.get(cummulative_sum, 0) + 1

        
        return count


# Test Cases
sol = Solution()
# print(sol.subarraySumBf([1,1,1], 2)) # 2
# print(sol.subarraySumBf([1,2,3], 3)) # 2
print(sol.subarraySum([1,1,1], 2)) # 2
print(sol.subarraySum([1,2,3], 3)) # 2