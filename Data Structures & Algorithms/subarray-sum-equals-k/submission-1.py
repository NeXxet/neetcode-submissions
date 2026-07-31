class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prevPrefixes = defaultdict(int)
        prevPrefixes[0] += 1
        result = currentSum = 0

        for num in nums:
            currentSum += num
            diff = currentSum - k

            result += prevPrefixes[diff]

            prevPrefixes[currentSum] += 1
        
        return result