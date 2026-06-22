# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        length = len(pairs)

        if length <= 1:
            return pairs

        middle = length // 2

        leftArr = self.mergeSort(pairs[:middle])
        rightArr = self.mergeSort(pairs[middle:])

        left = right = k = 0
        newArr = [0] * length

        while left < len(leftArr) and right < len(rightArr):
            if leftArr[left].key <= rightArr[right].key:
                newArr[k] = leftArr[left]
                left += 1
            else:
                newArr[k] = rightArr[right]
                right += 1
            k += 1

        while left < len(leftArr):
            newArr[k] = leftArr[left]
            left += 1
            k += 1
        while right < len(rightArr):
            newArr[k] = rightArr[right]
            right += 1
            k += 1
        

        return newArr