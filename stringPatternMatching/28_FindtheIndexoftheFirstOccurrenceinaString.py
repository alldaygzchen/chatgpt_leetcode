"""
## Problem: Sliding window
"""

from typing import List

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # the output
        result = -1
        # the record
        l=0
        # iterate haystack
        for r in range(len(haystack)):
            # check r-l+1 > len(needle)
            if r-l+1 > len(needle):
                # update l
                l+=1
            # check haystack substring equals needle
            if haystack[l:r+1] == needle:
                # yes, update result
                result = l
                return result
        return result



### test cases
s = Solution()
print(s.strStr("sadbutsad", "sad")) # 0
print(s.strStr("leetcode", "leeto")) # -1
