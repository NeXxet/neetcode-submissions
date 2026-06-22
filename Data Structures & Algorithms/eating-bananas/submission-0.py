import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # select upper and lower bound for k.
        low = 1
        high = max(piles)

        currentLowestK = math.inf

        while low <= high:
            hoursPassed = 0
            mid = (low+high)//2

            for pile in piles:
                hoursPassed += math.ceil(pile/mid)

            if hoursPassed > h:
                low = mid+1
            else:
                if mid < currentLowestK:
                    currentLowestK = mid
                elif mid > currentLowestK:
                    break
                high = mid-1
        return currentLowestK