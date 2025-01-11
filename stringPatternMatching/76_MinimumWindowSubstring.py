
"""
## Problem: Sliding window
"""

class Solution:
    def minWindow(self, s: str, t: str) -> str:

        ## the output
        result = ""
        
        ## the record
        l = 0 
        s_char_count_dict = {}
        t_char_count_dict = {}
        min_len = float('inf')
        min_ran = [0,0]
        have = 0

        for r in range(len(t)):
            if t[r] not in t_char_count_dict:
                t_char_count_dict[t[r]]=1
            else:
                t_char_count_dict[t[r]]+=1
        
        need = len(t_char_count_dict) 
        
        # iterate s (index:r)
        for r in range(len(s)):
            # update s_char_count_dict 
            if s[r] not in s_char_count_dict:
                s_char_count_dict[s[r]]=1
            else:
                s_char_count_dict[s[r]]+=1
            # check s_char_count_dict[s[r]] == t_char_count_dict[s[r]]
            if s[r] in t_char_count_dict and s_char_count_dict[s[r]] == t_char_count_dict[s[r]]:
                have +=1

            # check have == need:
            while have == need:
                # print('###','l:',l,'r:',r,'have:',have,'need:',need,'s_char_count_dict:',s_char_count_dict)
                # check min_length is min
                if min_len>r-l+1:
                    # update min_length
                    min_len = r-l+1
                    # update min_range
                    min_ran = [l,r+1]
                # update s_char_count_dict[s[l]]-1
                s_char_count_dict[s[l]]-=1
                # check s_char_count_dict[s[l]]+1 == t_char_count_dict[s[l]]
                if s[l] in t_char_count_dict and s_char_count_dict[s[l]]+1 == t_char_count_dict[s[l]]:
                    # update have
                    have-=1
                # update l
                l+=1
        result = s[min_ran[0]:min_ran[1]]
        return result




### test cases
s = Solution()
print(s.minWindow("ADOBECODEBANC","ABC")) # "BANC"
print(s.minWindow("a","a")) # "a"
print(s.minWindow("a","aa")) # ""