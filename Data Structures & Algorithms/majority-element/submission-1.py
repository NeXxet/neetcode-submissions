class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashmap = defaultdict(int)
        result = maxCount = 0

        for num in nums:
            hashmap[num] += 1
            if maxCount < hashmap[num]:
                result = num
                maxCount = hashmap[num]

        return result        