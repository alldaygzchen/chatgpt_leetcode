
"""
## Problem: Sliding window
"""


from typing import List
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:

        # the output
        result = []
        
        # the record
        char_count_dict_p = {}
        char_count_dict_s = {}
        l=0
        
        # get the char_count_dict of p
        for char in p:
            if char in char_count_dict_p:
                char_count_dict_p[char] += 1
            else:
                char_count_dict_p[char] = 1
        
        # iterate s
        for r in range(len(s)):
            # add current value to char_count_dict of s 
            if s[r] in char_count_dict_s:
                char_count_dict_s[s[r]] += 1
            else:
                char_count_dict_s[s[r]] = 1

            # Check if char_count_dict of p equals char_count_dict of s
            if (char_count_dict_s == char_count_dict_p):
                result.append(l)


            # Check r-l+1 > len(p)
            if r-l+1 == len(p):
                
                # remove the left value from char_count_dict of s
                # check value of char_count_dict of s is zero, remove the key
                if char_count_dict_s[s[l]] > 1:
                    char_count_dict_s[s[l]] -= 1
                else:
                    del char_count_dict_s[s[l]]
                
                # update l      
                l+=1
            
        return result


### test cases
s = Solution()
print(s.findAnagrams("cbaebabacd", "abc")) # [0,6]
print(s.findAnagrams("abab", "ab")) # [0,1,2]