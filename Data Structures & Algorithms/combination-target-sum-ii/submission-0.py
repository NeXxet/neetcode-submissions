class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()

        sublist = []
        result = []

        def backtrack(i, currentSum):
            if currentSum == target:
                result.append(sublist[:])
                return
            
            if i == len(candidates) or currentSum > target:
                return
        
            sublist.append(candidates[i])
            backtrack(i+1, currentSum + candidates[i])
            sublist.pop()

            while i + 1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1

            backtrack(i+1, currentSum)

        backtrack(0,0)
        return result