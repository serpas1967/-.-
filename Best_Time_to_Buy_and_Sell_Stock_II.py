
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """ calculate margin(profit)=delta  for each adjacent prices in "prices" array.
        Then choice all positive(non-negative) profits(delta).
        Their SUM is what we need: max possible profit """
        
        int = [prices[i + 1] - prices[i] for i in range(len(prices) - 1)]
        return sum([delta for delta in int if delta >= 0])