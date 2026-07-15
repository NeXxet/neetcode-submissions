class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        result = []
        solution = []
        
        def backtrack():
            if len(solution) == n:
                result.append(solution.copy())
                return

            for num in nums:
                 if num not in solution:
                    solution.append(num)
                    backtrack() 
                    solution.pop()

        backtrack()
        return result