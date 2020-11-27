'''leetCode Problem

121. Best Time to Buy and Sell Stock


Link for this problem is given Below

https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

'''


def maxProfit(prices) -> int:
    m = -1;
    n = 0;
    for i in prices:
        if i < m or m < 0:
            m = i;
        elif i - m > n:
            n = i - m;
    return n;

print(maxProfit([7,1,5,3,6,4]))

