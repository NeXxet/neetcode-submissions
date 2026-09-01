class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low, high = 1, max(piles)

        while high-low > 0:
            mid = (low+high)//2

            hours_taken = 0
            for pile in piles:
                hours_taken += math.ceil(pile/mid)

            if hours_taken > h:
                low = mid + 1
            else:
                high = mid 

        return high