class Solution {
    public int maxProfit(int[] prices) {
        int min_price = prices[0];
        int max_profit = 0;

        for (int i = 0; i < prices.length; i++) {
            if (min_price > prices[i]) {
                min_price = prices[i];
            }
            max_profit = Math.max(max_profit, prices[i] - min_price);
        }

        return max_profit;
    }
}