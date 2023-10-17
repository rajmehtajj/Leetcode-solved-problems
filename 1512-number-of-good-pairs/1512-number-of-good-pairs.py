from typing import List

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        num_counts = {} 
        count = 0

        for num in nums:
            if num in num_counts:
                count += num_counts[num]  
                num_counts[num] += 1 
            else:
                num_counts[num] = 1  

        return count
