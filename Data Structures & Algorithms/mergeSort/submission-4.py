# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def merge(self, pairs, left, mid, right):
        leftArr = pairs[left:mid+1]
        rightArr = pairs[mid+1:right+1]

        i = 0 
        j = 0
        k = left

        while i < len(leftArr) and j < len(rightArr):
            if leftArr[i].key <= rightArr[j].key:
                pairs[k] = leftArr[i]
                i += 1
            else:
                pairs[k] = rightArr[j]
                j += 1
            k += 1
        
        while i < len(leftArr):
            pairs[k] = leftArr[i]
            i += 1
            k += 1
        while j < len(rightArr):
            pairs[k] = rightArr[j]
            j += 1
            k += 1

    def split(self, pairs, left, right):
        if right - left + 1 <= 1:
            return pairs

        mid = (left+right) // 2

        self.split(pairs, left, mid)
        self.split(pairs, mid+1, right)

        self.merge(pairs, left, mid, right)

        return pairs

    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        return self.split(pairs, 0, len(pairs)-1)