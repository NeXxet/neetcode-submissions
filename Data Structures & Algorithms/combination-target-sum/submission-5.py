class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []

        def backtrack(i, remaining, current):
            if remaining == 0:
                result.append(current.copy())
                return

            if i == len(nums) or remaining < 0:
                return

            # Use nums[i], allowing it to be reused.
            current.append(nums[i])
            backtrack(i, remaining - nums[i], current)
            current.pop()

            # Do not use nums[i] again.
            backtrack(i + 1, remaining, current)

        backtrack(0, target, [])
        return result