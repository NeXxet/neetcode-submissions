class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        current = []

        def backtrack(i, remaining):
            if remaining == 0:
                result.append(current.copy())
                return

            if i == len(nums) or remaining < 0:
                return

            # Use nums[i], allowing it to be reused.
            current.append(nums[i])
            backtrack(i, remaining - nums[i])
            current.pop()

            # Do not use nums[i] again.
            backtrack(i + 1, remaining)

        backtrack(0, target)
        return result