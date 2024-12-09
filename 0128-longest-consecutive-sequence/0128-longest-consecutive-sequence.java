class Solution {
    public int longestConsecutive(int[] nums) {
        Set<Integer> uniqueNums = Arrays.stream(nums).boxed().collect(Collectors.toSet());
        int result = 0;

        for (int num : nums) {
            if (uniqueNums.contains(num - 1)) continue;
            int length = 1;
            while (uniqueNums.contains(num + length)) length += 1;
            result = Math.max(length, result);
        }

        return result;
    }
}