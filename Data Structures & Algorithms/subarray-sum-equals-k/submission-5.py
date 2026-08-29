class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        seen = defaultdict(int)
        seen[0] = 1
        current_sum, result = 0, 0


        for num in nums:
            current_sum += num
            diff = current_sum - k

            result += seen[diff]
            seen[current_sum] += 1
        
        return result