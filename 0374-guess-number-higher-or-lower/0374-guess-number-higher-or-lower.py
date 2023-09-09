class Solution:
    def guessNumber(self, n: int) -> int:
        left, right = 1, n
        
        while left <= right:
            mid = left + (right - left) // 2
            result = guess(mid)
            
            if result == 0:
                return mid
            elif result == 1:
                left = mid + 1
            else:
                right = mid - 1

# Example usage:
# Replace this function with the actual guess() function provided in your environment.
def guess(num):
    pick = 6  # Replace with the actual number you picked
    if num < pick:
        return 1
    elif num > pick:
        return -1
    else:
        return 0

