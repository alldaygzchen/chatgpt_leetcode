"""
Problem: Other
# create a s_to_t to prevent one to many mapping
# create a t_to_s to prevent many to one mapping
"""


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        ## the output
        result = True

        ## the record
        s_t_dict = {}
        t_s_dict = {}
        
        
        # check len(s) = len(t)
        if len(s) != len(t):
            result = False
            return result

        # zip t & s
        for char_s, char_t in zip(s,t):
            # check s_t_dict (already exists but one to many return false)
            if char_s in s_t_dict and s_t_dict[char_s]!=char_t:
                result = False
                return result
            elif char_s not in s_t_dict:
                s_t_dict[char_s] = char_t
            # check t_s_dict (already exists but many to one return false)
            if char_t in t_s_dict and t_s_dict[char_t]!=char_s:
                result = False
                return result
            elif char_t not in t_s_dict:
                t_s_dict[char_t] = char_s
        return result

## test cases 
s = Solution()
print(s.isIsomorphic("egg","add")) # true
print(s.isIsomorphic("foo","bar")) # false
print(s.isIsomorphic("paper","title")) # true