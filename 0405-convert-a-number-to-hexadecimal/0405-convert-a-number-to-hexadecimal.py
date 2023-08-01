class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return "0"

        hex_chars = "0123456789abcdef"
        result = []

        if num < 0:
            
            num += 2 ** 32

        while num > 0:
            
            result.append(hex_chars[num % 16])
            num //= 16

        return ''.join(result[::-1])  

