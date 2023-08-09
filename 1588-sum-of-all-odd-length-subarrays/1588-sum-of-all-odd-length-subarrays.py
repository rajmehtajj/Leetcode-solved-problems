
class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        n = len(arr)
        total_sum = 0
        
        for length in range(1, n+1, 2):  
            for start in range(n - length + 1):
                end = start + length - 1
                total_sum += sum(arr[start:end+1])
        
        return total_sum
