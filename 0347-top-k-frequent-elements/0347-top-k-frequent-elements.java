class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        Map<Integer, Integer> frequencyMap = new HashMap<>();
        int n = nums.length;
        List<Integer>[] buckets = new ArrayList[n + 1];

        for (int num : nums) {
            frequencyMap.put(num, frequencyMap.getOrDefault(num, 0) + 1);
        }

        for (int i = 0; i <= n; i++) {
            buckets[i] = new ArrayList<>();
        }

        for (Map.Entry<Integer, Integer> entry : frequencyMap.entrySet()) {
            int freq = entry.getValue();
            int num = entry.getKey();
            buckets[freq].add(num);
        }

        List<Integer> result = new ArrayList<>();  
        for (int i = n; i > 0; i--) {
            for (int num : buckets[i]) {
                if (result.size() == k) break;
                result.add(num);
            }
        }

        return result.stream().mapToInt(Integer::intValue).toArray(); // need return statement 
    }
}