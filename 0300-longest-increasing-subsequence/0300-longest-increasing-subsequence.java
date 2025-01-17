class Solution {
    public int lengthOfLIS(int[] nums) {
        List<Integer> sub = new ArrayList();

        for (int num:nums) {
            System.out.println(num);
            int pos = bisectionLeft(sub, num);
            
            if (pos == sub.size()) {
                sub.add(num);
            } else {
                sub.set(pos, num);
            }
        }

        return sub.size();
    }
    public int bisectionLeft (List<Integer> list, int target) {
        int low = 0;
        int high = list.size() - 1;

        while (low <= high) {
            int mid = low + (high - low) / 2;

            if (list.get(mid) < target) {
                low = mid + 1;
            } else {
                high = mid - 1;
            }
        }

        return low;
    }
}