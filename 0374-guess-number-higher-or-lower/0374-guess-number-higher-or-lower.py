
class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        left, right = 1, n
        
        while left <= right:
            mid = left + (right - left) // 2
            result = guess(mid)

            if result == 0:
                return mid  # Found the correct number
            elif result == -1:
                right = mid - 1  # The number is lower than the guess
            else:
                left = mid + 1  # The number is higher than the guess

        