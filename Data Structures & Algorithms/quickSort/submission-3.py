# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        self.partition(pairs, 0, len(pairs)-1)
        return pairs

    def partition(self, pairs, start, end):
        if end - start + 1 <= 1:
            return pairs
        
        pivot = pairs[end]
        left = start

        for i in range(start, end):
            if pairs[i].key < pivot.key:
                pairs[i], pairs[left] = pairs[left], pairs[i]
                left += 1
        pairs[end], pairs[left] = pairs[left], pairs[end]

        self.partition(pairs, start, left-1)
        self.partition(pairs, left+1, end)

        return pairs