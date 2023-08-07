class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        size = len(flowerbed)
        count = 0
        i = 0
        
        while i < size:
            if flowerbed[i] == 0:
                # Check if the previous and next plots are also empty or out of bounds
                prev_empty = (i == 0 or flowerbed[i - 1] == 0)
                next_empty = (i == size - 1 or flowerbed[i + 1] == 0)
                
                if prev_empty and next_empty:
                    flowerbed[i] = 1  # Place a flower in the current plot
                    count += 1
            i += 1
            
        return count >= n