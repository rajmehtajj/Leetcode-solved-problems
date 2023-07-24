class Solution:
    def reverseVowels(self, s: str) -> str:
    # Convert the string to a list for easier manipulation
        s_list = list(s)
    
    # Define a set of vowels to check against
        vowels = set('aeiouAEIOU')
    
    # Initialize two pointers: one at the start and one at the end of the string
        left, right = 0, len(s_list) - 1
    
        while left < right:
        # Move the left pointer until it points to a vowel
            while left < right and s_list[left] not in vowels:
                left += 1
        
        # Move the right pointer until it points to a vowel
            while left < right and s_list[right] not in vowels:
                right -= 1
        
        # Swap the vowels at the left and right pointers
            s_list[left], s_list[right] = s_list[right], s_list[left]
        
        # Move the pointers inward
            left += 1
            right -= 1
        
    # Convert the list back to a string and return the result
        return ''.join(s_list)



        