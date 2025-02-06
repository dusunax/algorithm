class Solution {
    public int findMin(int[] nums) {
        if (nums.length == 1){
            return nums[0];
        }

        return Arrays.stream(nums).min().getAsInt();
    }
}