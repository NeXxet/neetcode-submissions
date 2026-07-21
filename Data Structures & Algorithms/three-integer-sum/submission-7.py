class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []

        for index, num in enumerate(nums):
            p1 = index+1
            p2 = len(nums)-1

            if index > 0 and num == nums[index-1]:
                continue

            while p1 < p2:
                if num + nums[p1] + nums[p2] == 0:
                    result.append([num, nums[p1], nums[p2]])
                    p1 += 1
                    p2 -= 1
                    while p2 > -1 and nums[p2] == nums[p2+1]:
                        p2 -=1
                elif num + nums[p1] + nums[p2] < 0:
                    p1 += 1
                else:
                    p2 -= 1

        return result