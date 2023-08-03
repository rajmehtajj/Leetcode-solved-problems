class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        compare=max(candies)
        result=[]
       
        for num_candies in candies:
            result.append(num_candies + extraCandies >= compare)
        
        return result