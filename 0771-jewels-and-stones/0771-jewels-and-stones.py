class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
 
        num_jewels = 0

        jewel_set = set(jewels)

        for stone in stones:
            if stone in jewel_set:
                # If the stone is a jewel, increment the count
                num_jewels += 1

        return num_jewels
