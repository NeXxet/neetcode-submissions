class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []

        def backtrack(i, sublist):
            if i == len(nums):
                result.append(sublist.copy())
                return
            
            for num in nums:
                if num not in sublist:
                    sublist.append(num)
                    backtrack(i+1, sublist)
                    sublist.pop()
        
        backtrack(0, [])
        return result