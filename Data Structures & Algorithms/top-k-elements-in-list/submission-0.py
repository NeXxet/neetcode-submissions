class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = []
        hashmap = defaultdict(int)
        bucket = [[] for _ in range(len(nums) + 1)]

        for num in nums:
            hashmap[num] += 1

        for key, value in hashmap.items():
            bucket[value].append(key)

        for i in range(len(bucket)-1, 0, -1):
            for num in bucket[i]:
                result.append(num)
                if len(result) == k:
                    return result

        return result
        

