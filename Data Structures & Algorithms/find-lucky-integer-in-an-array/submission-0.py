class Solution:
    def findLucky(self, arr: List[int]) -> int:
        hashmap = defaultdict(int)
        luckyInt = -1

        for num in arr:
            hashmap[num] += 1

        for num, freq in hashmap.items():
            if num == freq and num > luckyInt:
                luckyInt = num

        return luckyInt
        