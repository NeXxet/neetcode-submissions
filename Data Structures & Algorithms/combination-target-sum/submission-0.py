class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        sublist = []

        def backtrack(i, currentSum):
            if currentSum == target:
                result.append(sublist[:])
                return

            if currentSum > target or i == len(nums):
                return

            backtrack(i+1, currentSum)

            sublist.append(nums[i])
            backtrack(i, currentSum + nums[i])
            sublist.pop()

        backtrack(0, 0)
        
        return result 