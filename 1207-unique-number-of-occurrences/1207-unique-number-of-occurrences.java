class Solution {
    public boolean uniqueOccurrences(int[] arr) {
        Map<Integer, Integer> freq = intCounter(arr);
        Set<Integer> uniqueCheck = new HashSet();

        for (Map.Entry<Integer, Integer> entry: freq.entrySet()) {
            int count = entry.getValue();
            if (uniqueCheck.contains(count)){
                return false;
            }
            uniqueCheck.add(count);
        }

        return true;
    }
    public Map<Integer, Integer> intCounter(int[] arr) {
        Map<Integer, Integer> freqMap = new HashMap<>();

        for(int num: arr){
            freqMap.put(num, freqMap.getOrDefault(num, 0)+1);
        }
        return freqMap;
    }
}