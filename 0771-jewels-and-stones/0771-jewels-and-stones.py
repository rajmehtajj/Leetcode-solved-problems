class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        # Initialize a variable to count the number of jewels in stones
        num_jewels = 0

        # Create a set of jewel types for efficient lookup
        jewel_set = set(jewels)

        # Iterate through each stone
        for stone in stones:
            if stone in jewel_set:
                # If the stone is a jewel, increment the count
                num_jewels += 1

        return num_jewels
