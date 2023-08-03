class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_w= 0 
        
        for x in accounts:
            max_w=max(max_w, sum(x))
        return max_w
        
