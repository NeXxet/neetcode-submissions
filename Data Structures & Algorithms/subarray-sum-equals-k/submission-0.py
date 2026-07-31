class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prevPrefixes = {0:1}
        result = currentSum = 0

        for num in nums:
            currentSum += num
            diff = currentSum - k

            result += prevPrefixes.get(diff, 0)

            prevPrefixes[currentSum] = 1 + prevPrefixes.get(currentSum, 0)
        
        return result