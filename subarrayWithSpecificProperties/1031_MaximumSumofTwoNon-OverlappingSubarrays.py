"""
## Problem: Sliding window
# target: the longest subaaray with 2 elements
# write comment strucute
"""
from typing import List

class Solution:
    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:
        
        # the output
        max_sum =0
        
        # the record
        id_prefix_dict ={}
        id_prefix_dict[-1]=0
        prefix_sum = 0
        max_sum_firstLen =0
        max_sum_secondLen =0

        # iterate (consider the current state)
        for r in range(0,len(nums)):

            prefix_sum +=nums[r]
            id_prefix_dict[r] = prefix_sum  


            if r>=(firstLen+secondLen)-1:

                # get the sum_firstLen_r
                sum_firstLen_r = id_prefix_dict[r] - id_prefix_dict[r-firstLen]

                # get the sum_secondLen_r
                sum_secondLen_r = id_prefix_dict[r] - id_prefix_dict[r-secondLen]

                # get the max_sum_secondLen and update  
                max_sum_secondLen =  max(max_sum_secondLen,id_prefix_dict[r-firstLen] - id_prefix_dict[r-firstLen-secondLen])
                
                # get the max_sum_firstLen and update
                max_sum_firstLen =  max(max_sum_firstLen,id_prefix_dict[r-secondLen] - id_prefix_dict[r-secondLen-firstLen])

                # get max_sum and update 
                # (max record) vs (max_sum_secondLen+sum_firstLen_r)vs (max_sum_firstLen+sum_secondLen_r)
                max_sum = max(max_sum ,max_sum_secondLen+sum_firstLen_r, max_sum_firstLen+sum_secondLen_r)

                # print('max_sum_secondLen',max_sum_secondLen,'sum_firstLen_r',sum_firstLen_r)
                # print('max_sum_firstLen',max_sum_firstLen,'sum_secondLen_r',sum_secondLen_r)
        

        # return output
        return max_sum

    # def maxSumTwoNoOverlap(self,nums, L, M):
    #     n = len(nums)
        
    #     # Initialize variables to store the maximum sums
    #     max_L = max_M = 0
    #     result = 0
        
    #     # Initialize prefix sums array
    #     prefix_sums = [0] * (n + 1)
        
    #     # Iterate through the array to calculate prefix sums and find the maximum sum of two non-overlapping subarrays
    #     for i in range(1, n + 1):
    #         prefix_sums[i] = prefix_sums[i - 1] + nums[i - 1]
            
    #         if i >= L + M:
    #             # Update the maximum sum of subarray of length L ending before the current index
    #             max_L = max(max_L, prefix_sums[i - M] - prefix_sums[i - M - L])
                
    #             # Update the maximum sum of subarray of length M ending before the current index
    #             max_M = max(max_M, prefix_sums[i - L] - prefix_sums[i - L - M])
                
    #             # Calculate the maximum sum of two non-overlapping subarrays
    #             result = max(result, max_L + prefix_sums[i] - prefix_sums[i - M], max_M + prefix_sums[i] - prefix_sums[i - L])
        
    #     return result
s = Solution()
print(s.maxSumTwoNoOverlap([0,6,5,2,2,5,1,9,4],1,2))#20
print(s.maxSumTwoNoOverlap([3,8,1,3,2,1,8,9,0],3,2)) #29
print(s.maxSumTwoNoOverlap([2,1,5,6,0,9,5,0,3,8],4,3)) #31
print(s.maxSumTwoNoOverlap([1,0,1],1,1)) #2