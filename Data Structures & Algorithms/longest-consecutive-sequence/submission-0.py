class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashSet = set(nums)

        longest = 0

        for num in nums:
            length = 1
            currentNum = num
            if currentNum-1 not in hashSet:
                while currentNum+1 in hashSet:
                    length += 1
                    currentNum += 1
                longest = max(longest, length)

        return longest

        