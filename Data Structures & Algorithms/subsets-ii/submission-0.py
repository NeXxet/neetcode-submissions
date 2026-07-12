class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()

        def backtrack(i, sublist):
            if i == len(nums):
                result.append(sublist[:])
                return

            sublist.append(nums[i])
            backtrack(i+1, sublist)
            sublist.pop()

            while i+1 < len(nums) and nums[i] == nums[i+1]:
                i += 1

            backtrack(i+1, sublist)
        
        backtrack(0, [])
        return result
        