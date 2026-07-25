class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = defaultdict(int)
        bucket = [[] for _ in range(len(nums)+1)]
        result = []

        for num in nums:
            hashmap[num] += 1

        for num, count in hashmap.items():
            bucket[count].append(num)

        for i in range(len(bucket)-1, -1, -1):
            for num in bucket[i]:
                result.append(num)
                if len(result) == k:
                    return result