"""
## Problem: Group
# Sort the word to create a key
# Create a dictionary with the key and the list of anagrams
"""


from typing import List
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        sortStr_listStr_dict = {}

        # iterate strs
        for str in strs:
            # check sorted str in sortStr_listStr_dict 
            # update sortStr_listStr_dict 
            sorted_str = "".join(sorted(str))
            if sorted_str in sortStr_listStr_dict:
                sortStr_listStr_dict[sorted_str].append(str)
            else:
                sortStr_listStr_dict[sorted_str] = [str]

        # return sortStr_listStr_dict.values
        return list(sortStr_listStr_dict.values())

s = Solution()
print(s.groupAnagrams(["eat","tea","tan","ate","nat","bat"])) # [["bat"],["nat","tan"],["ate","eat","tea"]]
print(s.groupAnagrams([""])) # [[""]]
print(s.groupAnagrams(["a"])) # [["a"]]