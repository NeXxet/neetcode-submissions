class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low, high = 0, max(piles)

        while high-low > 1:
            hours_taken = 0
            eating_rate = (low+high)//2

            for pile in piles:
                hours_taken += math.ceil(pile/eating_rate)

            if hours_taken <= h:
                high = eating_rate
            else:
                low = eating_rate

        return high