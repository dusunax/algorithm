class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        HashMap<String, List<String>> result = new HashMap<>();
        
        for (String str : strs){
            char[] chars = str.toCharArray();
            Arrays.sort(chars);
            String sortedStr = new String(chars);

            result.putIfAbsent(sortedStr, new ArrayList<>());
            result.get(sortedStr).add(str);
        }

        return new ArrayList<>(result.values());
    }
}