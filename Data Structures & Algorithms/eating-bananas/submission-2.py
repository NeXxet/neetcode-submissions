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
                hoursPassed += (pile + mid -1) // mid

            if hoursPassed > h:
                low = mid+1
            else:
                currentLowestK = mid
                high = mid-1
        return currentLowestK