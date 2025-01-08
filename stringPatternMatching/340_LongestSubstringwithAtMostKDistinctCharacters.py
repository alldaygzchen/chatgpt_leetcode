"""
## Problem: Sliding window
"""

class Solution:
    def lengthOfLongestSubstringKDistinct(self, s:str,k:int):
        
        ## the output
        max_len = float('-inf')
        
        ## the record
        char_count_dict = {}
        l = 0
        
        # iterate s 
        for r in range(len(s)):
            # update char_count_dict
            if s[r] in char_count_dict:
                char_count_dict[s[r]]+=1
            else:
                char_count_dict[s[r]]=1
            # check len(char_count_dict) == k:
            while len(char_count_dict) == k:
                # update max_len
                max_len = max(max_len,r-l+1)
                # update char_count_dict[s[l]]
                char_count_dict[s[l]]-=1
                # update char_count_dict[s[l]]==0
                if char_count_dict[s[l]]==0:
                    del char_count_dict[s[l]]
                # update l
                l+=1
        # return 
        return max_len



### test cases
s = Solution()
print(s.lengthOfLongestSubstringKDistinct("eceba",2)) #2
print(s.lengthOfLongestSubstringKDistinct("aa",1)) #1
