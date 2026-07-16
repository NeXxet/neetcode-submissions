class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        def backtrack(i, sublist):
            if i == len(nums):
                result.append(sublist.copy())
                return

            sublist.append(nums[i])
            backtrack(i+1, sublist)
            sublist.pop()

            backtrack(i+1, sublist)

        backtrack(0, [])
        return result        