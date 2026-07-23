class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []

        def backtrack(sublist):
            if len(sublist) == len(nums):
                result.append(sublist.copy())
                return

            for num in nums:
                if num not in sublist:
                    sublist.append(num)
                    backtrack(sublist)
                    sublist.pop()

        backtrack([])
        return result
        
        