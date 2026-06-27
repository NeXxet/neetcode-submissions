class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        for index, num in enumerate(nums):
            map[num] = index
        
        for index, num in enumerate(nums):
            if (target-num) in map and map[target-num] != index:
                return [index, map[target-num]]
        
        return []