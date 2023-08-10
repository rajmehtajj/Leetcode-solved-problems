class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 1:
            stones.sort() 
            heaviest1 = stones.pop()  
            heaviest2 = stones.pop()  
            if heaviest1 != heaviest2:
                new_weight = heaviest1 - heaviest2
                stones.append(new_weight)  
        if len(stones) == 1:
            return stones[0]
        else:
            return 0
