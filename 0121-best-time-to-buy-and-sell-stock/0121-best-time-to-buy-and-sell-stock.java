class Solution {
    public int maxProfit(int[] prices) {
        int min_price = prices[0];
        int max_profit = 0;

        for (int price : prices){
            min_price = Math.min(price, min_price);
            max_profit = Math.max(price - min_price, max_profit);
        }

        return max_profit;
    }
}