class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a
        
        if str1 + str2 != str2 + str1:
            return ""
        
        divisor_length = gcd(len(str1), len(str2))
        divisor = str1[:divisor_length]
        
        return divisor