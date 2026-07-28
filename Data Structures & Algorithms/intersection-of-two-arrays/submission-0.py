class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        unique_one = set(nums1)

        return list(set([num for num in nums2 if num in unique_one]))