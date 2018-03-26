# -*- coding: utf-8 -*-


class Solution(object):
    def maxProfit(self, prices):
        maxprofit = 0
        if(prices != []):
            minprice = prices[0]
            for i in range(len(prices)):
                if (prices[i] < minprice):
                    minprice = prices[i]
                elif (prices[i] - minprice > maxprofit):
                    maxprofit = prices[i] - minprice
        return maxprofit


if __name__ == '__main__':
    prices = [7, 1, 5, 6, 2, 3]
    # prices = [7, 6, 5, 4, 3, 2]
    # prices = []
    solution = Solution()
    maxprofit = solution.maxProfit(prices)
    print(maxprofit)
