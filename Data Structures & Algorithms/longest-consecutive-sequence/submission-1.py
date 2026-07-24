class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashSet = set(nums)

        longest = 0

        for num in nums:
            length = 1
            if num-1 not in hashSet:
                while num+1 in hashSet:
                    length += 1
                    num += 1
                longest = max(longest, length)

        return longest

        