class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        self.combinations = 0

        def backtrack(i, currentSum):
            if i == len(nums):
                if currentSum == target:
                    self.combinations += 1
                return
            
            backtrack(i+1, currentSum-nums[i])
            backtrack(i+1, currentSum+nums[i])

        backtrack(0, 0)
        return self.combinations

        