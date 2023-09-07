
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
       
        i = 0  # Pointer for iterating
        j = 0  # Pointer for placing non-zero elements

        while i < len(nums):
            if nums[i] != 0:
           
                nums[j] = nums[i]
                j += 1
            i += 1

        while j < len(nums):
            nums[j] = 0
            j += 1
