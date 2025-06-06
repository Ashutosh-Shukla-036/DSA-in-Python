"""You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0."""


"""
So here we are trying to find the maximum profit we can get from buying the stock at lowest price and selling at the highest price.

We can do this by iterating over the array and keeping track of the minimum price we have seen so far and the maximum profit we can get from that minimum price.

example array = [7 , 1 , 5 , 6 , 3 , 4] , minimum price to buy stock = 1 , maximum profit = 6 - 1 = 5 

so here we start from mini = 7 and we find the max profit , we initail keep profit as 0 and we try selling the mini 
with next day stock price so we get 1 - 7 as -6 which is loss so we do not sell the stock on that day but 
as next days stock price is lesser we updated the mini as 1. so now we try selling the stock with next day stock price 
which is 5 - 1 we get 4 as profit so we update the max_profit as 4 and we continue this process and mini is still as
1 is lesser then 5 so we do not update the mini and we try selling the stock with next day stock price which is 6 - 1 we get 5 as profit so we update the max_profit as
5 and we continue this process and mini is still as 1 is lesser then 6. We repeat this process until we reach the end of the array. 
"""

def maxProfit(prices):
    maxProfit , mini = 0 , prices[0]
    for i in range(1, len(prices)):
        SellingProfit = prices[i] - mini
        maxProfit = max(SellingProfit, maxProfit)
        mini = min(mini, prices[i])
    print(maxProfit)

maxProfit([7 , 1 , 5 , 6 , 3 , 4])