class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []

        def backtrack(i, sublist, currentSum):
            if i == len(nums) or currentSum > target:
                return
            
            if currentSum == target:
                result.append(sublist[:])
                return

            sublist.append(nums[i])
            backtrack(i, sublist, currentSum+nums[i])
            sublist.pop()

            backtrack(i+1, sublist, currentSum)

        backtrack(0, [], 0)
        return result