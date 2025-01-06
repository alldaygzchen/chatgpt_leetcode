"""
## Problem: Sliding window
# target: the longest subaaray with 2 elements
"""


from typing import List
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        
        # the output
        max_len = float('-inf')

        # the record
        fruitType_count_dict = {}

        l = 0
        
        # iterate
        for r in range(len(fruits)):
            # in the basket
            if fruits[r] in fruitType_count_dict:
                fruitType_count_dict[fruits[r]] += 1 
                max_len =  max(max_len,r-l+1)
            # not in the basket
            else:
                fruitType_count_dict[fruits[r]] = 1
                
                # update the dict and update the left index
                while len(fruitType_count_dict)>2:
                    fruitType_count_dict[fruits[l]]-=1
                    if fruitType_count_dict[fruits[l]] == 0:
                        del fruitType_count_dict[fruits[l]]
                    l+=1
                max_len= max(max_len,r-l+1)

            #print('l,','r,','fruitType_count_dict',l,r,fruitType_count_dict)
        return max_len

# test cases
s = Solution()
print(s.totalFruit([1,2,1])) # 3
print(s.totalFruit([0,1,2,2])) # 3
print(s.totalFruit([1,2,3,2,2])) # 4
print(s.totalFruit([3,3,3,1,2,1,1,2,3,3,4])) #5