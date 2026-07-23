class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        numsProduct = 1
        output = []
        zeroCount = nums.count(0)

        if zeroCount == 1:
            for num in nums:
                if num == 0:
                    continue
                else:
                    numsProduct = numsProduct * num
        else:
            numsProduct = math.prod(nums)

        for num in nums:
            if zeroCount == 1:
                if num == 0:
                    output.append(numsProduct)
                    continue
                else:
                    output.append(0)
            else:
                if num == 0:
                    output.append(0)
                    continue
                else:
                    output.append(int(numsProduct * (num**-1)))

        return output
