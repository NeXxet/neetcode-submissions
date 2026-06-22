# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def merge(self, pairs, start, middle, end):
        left = pairs[start:middle+1]
        right = pairs[middle+1:end+1]

        i = j = 0
        k = start

        while i < len(left) and j < len(right):
            if left[i].key <= right[j].key:
                pairs[k] = left[i]
                i += 1 
                k += 1
            else:
                pairs[k] = right[j]
                j += 1
                k += 1
        
        while i < len(left):
            pairs[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            pairs[k] = right[j]
            j += 1
            k += 1


    def mergeSortHelper(self, pairs: List[Pair], start, end):
        if end - start + 1 <= 1:
            return pairs
        
        middle = (start + end) // 2

        self.mergeSortHelper(pairs, start, middle)
        self.mergeSortHelper(pairs, middle+1, end)

        self.merge(pairs, start, middle, end)

        return pairs

    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        self.mergeSortHelper(pairs, 0, len(pairs)-1)
        return pairs

