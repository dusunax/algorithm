class Solution {
    public int missingNumber(int[] nums) {
        int n = nums.length;
        int xorNums = 0;

        for (int i = 0; i < n; i++) {
            xorNums ^= nums[i];
        }
        for (int i = 0; i <= n; i++) {
            xorNums ^= i;
        }

        return xorNums;
    }
}