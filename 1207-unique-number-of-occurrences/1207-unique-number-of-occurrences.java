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
    // imprement of Counter class in python
    public Map<Integer, Integer> intCounter(int[] arr) {
        Map<Integer, Integer> freqMap = new HashMap<>();

        for(int num: arr){
            freqMap.put(num, freqMap.getOrDefault(num, 0)+1);
        }
        return freqMap;
    }
}

/*
### HashSet
`set` is interface in Java. use a **concrete implementation** of the `Set` interface, like:

- `HashSet` — unordered, backed by a hash table, best for average O(1) add/contains.
- `TreeSet` — sorted set, backed by a tree (balanced), O(log n) operations.
- `LinkedHashSet` — maintains insertion order.

=> using set for fast lookup and no need for order => HashSet.

### Entry in languages
an Entry represents a key-value pair

Java: 
- Entry `Map.Entry`
- use `.entrySet()` on map

Python: 
- tuple `(key, value)`
- use `.items()`, on dict

JavaScript: 
- Array `[key, value]`
- use `.entries()` on Object or map
*/