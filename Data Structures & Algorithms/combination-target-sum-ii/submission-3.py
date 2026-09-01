class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []

        def backtrack(i, sublist, current_sum):
            if current_sum == target:
                result.append(sublist.copy())
                return
            if current_sum > target or i == len(candidates): 
                return

            sublist.append(candidates[i])
            backtrack(i+1, sublist, current_sum+candidates[i])
            sublist.pop()

            while i + 1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1

            backtrack(i+1, sublist, current_sum)
        
        backtrack(0, [], 0)
        return result