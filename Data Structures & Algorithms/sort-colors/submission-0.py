class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        buckets = [0, 0, 0]

        for num in nums:
            buckets[num] += 1

        i = 0
        for index, bucket in enumerate(buckets):
            for j in range(bucket):
                nums[i] = index
                i += 1
        