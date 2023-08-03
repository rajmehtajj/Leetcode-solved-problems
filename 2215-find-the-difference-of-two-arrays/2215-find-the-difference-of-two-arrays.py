class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        set_nums1 = set(nums1)
        set_nums2 = set(nums2)

        distinct_nums1 = list(set_nums1.difference(set_nums2))
        distinct_nums2 = list(set_nums2.difference(set_nums1))

        return [distinct_nums1, distinct_nums2]