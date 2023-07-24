class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        
        if n <= 0:
            return False

    # Check if n is a power of two
        if n & (n - 1) != 0:
            return False

    # Check if the only set bit is in an even position
        return n & 0x55555555 == n
