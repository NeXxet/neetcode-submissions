# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def partition(self, pairs: List[Pair], start, end) -> List[Pair]:
        if end - start + 1 <= 1:
            return pairs
        
        pivot = pairs[end]
        left = start

        for i in range(start, end):
            if pairs[i].key < pivot.key:
                pairs[left], pairs[i] = pairs[i], pairs[left]
                left += 1
        pairs[end], pairs[left] = pairs[left], pairs[end]

        self.partition(pairs, start, left-1)
        self.partition(pairs, left+1, end) 

        return pairs

    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        self.partition(pairs, 0, len(pairs)-1)
        return pairs