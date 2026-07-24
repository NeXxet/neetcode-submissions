class Solution:
    def countElements(self, arr: List[int]) -> int:
        hashset = set(arr)
        count = 0

        for num in arr:
            if (num+1) in hashset:
                count += 1

        return count
        