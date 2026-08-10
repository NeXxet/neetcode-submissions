class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        def findPivot(left, right):
            while left < right:
                mid = left + (right-left)//2
                if nums[mid] > nums[right]:
                    left = mid + 1
                else:
                    right = mid
            return right
        
        def binarySearch(left, right):
            while left <= right:
                mid = left + (right-left)//2

                if nums[mid] == target:
                    return mid
                elif nums[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1

            return -1

        pivot = findPivot(0, len(nums)-1)
        result = binarySearch(0, pivot)
        if result != -1:
            return result
        else:
            return binarySearch(pivot, len(nums)-1)



