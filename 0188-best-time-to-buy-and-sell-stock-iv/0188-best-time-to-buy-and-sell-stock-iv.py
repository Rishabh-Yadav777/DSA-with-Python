class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)

        if n < 2 or k == 0:
            return 0

        # If k is large, transactions become unlimited
        if k >= n // 2:
            profit = 0
            for i in range(1, n):
                if prices[i] > prices[i - 1]:
                    profit += prices[i] - prices[i - 1]
            return profit

        # DP using previous and current transaction
        profit = [0] * n

        for _ in range(k):
            current = [0] * n
            max_diff = -prices[0]

            for day in range(1, n):
                current[day] = max(
                    current[day - 1],
                    prices[day] + max_diff
                )

                max_diff = max(max_diff, profit[day] - prices[day])

            profit = current

        return profit[-1]