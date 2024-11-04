class Solution {
    public int climbStairs(int n) {
        // 1. Bottom-Up \U0001f37a
        // if (n == 1 || n == 2) return n;

        // int first = 1;
        // int second = 2;

        // for (int i = 3; i < n + 1; i++){
        //     int curr = first + second;
        //     first = second;
        //     second = curr;
        // }
        // return second;

        // 2. Top-bottom \U0001f4dd
        Map<Integer, Integer> memo = new HashMap<>(); // Map(keyword for declaration type) HashMap(built-in java collection)
        return dp(n, memo);
    }

    // - must specify the types of method parameters and return values
    private int dp(int step, Map<Integer, Integer> memo){ 
        if (step == 1 || step == 2){
            return step;
        }
        if (memo.containsKey(step)){
            return memo.get(step);
        }

        memo.put(step, dp(step - 1, memo) + dp(step - 2, memo));
        return memo.get(step);
    }
}


// 
// built-in Java collections
// - Java’s standard libraries provide many common data structures: HashMap, ArrayList, Set, etc.
// that can be used without creating custom classes like `public class memo {}`

// - HashMap: storing key-value pairs. 
// `Map<Integer, Integer> memo = new HashMap<>();`

// -------------------------------------
// ❗️ Compile Error
// Line 21: error: illegal start of expression
//        private int dp(int step, Map<Integer, Integer> memo){

// cannot define a method (like dp) inside another method (like climbStairs) 
// \U0001f449 unless it's an inner class or a lambda expression

// -------------------------------------
// ❗️ Compile Error
// Line 26: error: array required, but Map<Integer,Integer> found
//        if (memo[step]){

// use `memo.containsKey(step)`, not memo[step]
// use HashMap Methods: containsKey, get, put
// HashMap Methods: https://www.w3schools.com/java/java_ref_hashmap.asp
// containsKey(): https://www.w3schools.com/java/ref_hashmap_containskey.asp