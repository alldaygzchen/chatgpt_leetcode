"""
## Problem: Sliding window
# use set to store the characters that have been seen
"""

from typing import List
class Solution:

    def lengthOfLongestSubstringBf(self, s: str) -> int:

        # the output
        max_len = float('-inf')

        # edge case
        if len(s) == 0:
            return 0

        for r in range(len(s)):
            # itself
            max_len = max(max_len, 1)
            for l in range(0,r):
                char_st =set()
                continue_flag = True
                for i in range(l, r):
                    if s[i] in char_st:
                        max_len = max(max_len, len(char_st))
                        continue_flag = False
                        break
                    char_st.add(s[i])
                if continue_flag:
                    if s[r] in char_st:
                        max_len = max(max_len, len(char_st))
                    else:
                        char_st.add(s[r])
                        max_len = max(max_len, len(char_st))
        return max_len


    def lengthOfLongestSubstring(self, s: str) -> int:

        # the output
        max_len = float('-inf')

        # the record
        char_set = set()

        l = 0

        # edge case
        if len(s) == 0:
            return 0
        
        for r in range(len(s)):
            while s[r] in char_set:
                char_set.remove(s[l])
                l += 1
            
            char_set.add(s[r])
            max_len = max(max_len, r-l+1)
        return max_len
    
    # too hard to think of
    # def lengthOfLongestSubstring2(self, s: str) -> int:
    #     char_index = {}
    #     start = 0
    #     max_length = 0

    #     #aba => ba
    #     #abb => b
    #     #abba => ba
    #     for i, char in enumerate(s):
    #         if char in char_index and char_index[char] >= start:
    #             start = char_index[char] + 1
    #         char_index[char] = i
    #         max_length = max(max_length, i - start + 1)

    #     return max_length
# Test Cases
sol = Solution()
print(sol.lengthOfLongestSubstring("abcabcbb")) # 3
print(sol.lengthOfLongestSubstring("bbbbb")) # 1
print(sol.lengthOfLongestSubstring("pwwkew")) # 3
# print(sol.lengthOfLongestSubstringBf("ckilbkd")) #5