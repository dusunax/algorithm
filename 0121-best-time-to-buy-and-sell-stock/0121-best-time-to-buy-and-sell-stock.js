/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function(prices) {
    min_price = prices[0];
    max_profit = 0;

    prices.forEach(p => {
        if(min_price > p) min_price = p;
        max_profit = Math.max(p - min_price, max_profit);
    })

    return max_profit;
};