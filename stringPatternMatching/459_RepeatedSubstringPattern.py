
"""
## Problem: Iteration
"""


class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        
        # the output 
        result = False

        # the record
        sub_str = ""

        # iterate 
        for r in range(len(s)):

            # check r <= len(s)//2
            if r <= len(s)//2:
                # update substring 
                sub_str = sub_str + s[r]
                # check len(s)%len(substring) =0 
                if len(s)%len(sub_str) ==0 and len(s)//len(sub_str)>1:
                    # check substring * len(s)%len(substring) == s
                    temp = sub_str * (len(s)//len(sub_str))
                    if temp == s:
                        result = True
                        return result
            # else check
            else:
                return result
        return result

        

### test cases
s = Solution()
# print(s.repeatedSubstringPattern("abab")) # true
# print(s.repeatedSubstringPattern("aba")) # false
# print(s.repeatedSubstringPattern("abcabcabcabc")) # true
print(s.repeatedSubstringPattern("ab")) # true