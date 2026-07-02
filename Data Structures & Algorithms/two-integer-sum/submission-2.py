class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}

        for index, num in enumerate(nums):
            hashMap[num] = index

        for index, num in enumerate(nums):
            if (target-num) in hashMap and hashMap[target-num] != index:
                return [index, hashMap[target-num]]
        return []