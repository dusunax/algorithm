class Solution {
    public int climbStairs(int n) {
        // 1. Bottom-Up \U0001f37a
        if (n == 1 || n == 2) return n;

        int first = 1;
        int second = 2;

        for (int i = 3; i < n + 1; i++){
            int curr = first + second;
            first = second;
            second = curr;
        }
        return second;

        // 2. Top-bottom \U0001f4dd
    }
}