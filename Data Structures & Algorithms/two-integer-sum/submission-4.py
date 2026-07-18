class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {num:index for index, num in enumerate(nums)}

        for index, num in enumerate(nums):
            diff = target-num
            if (diff) in hashMap and hashMap[diff] != index:
                return [index, hashMap[diff]]
        return []