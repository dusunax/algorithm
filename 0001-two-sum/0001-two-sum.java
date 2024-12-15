class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> map = new HashMap<>();
        
        for (int i = 0; i < nums.length; i++){
            int pairNum = target - nums[i];
            if (map.containsKey(pairNum)) {
                return new int[] {map.get(pairNum), i};
            }
            map.put(nums[i], i);
        }

        throw new IllegalArgumentException("two sum solution is not exist\U0001f645‍♀️");
    }
}