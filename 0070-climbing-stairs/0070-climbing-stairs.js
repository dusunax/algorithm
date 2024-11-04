/**
 * @param {number} n
 * @return {number}
 */
var climbStairs = function(n) {
    // Bottom-up: iterate
    if (n === 1 || n === 2) return n;

    let first = 1;
    let second = 2;

    for (let i = 3; i < n+1; i++){
        const curr = first + second; // base case
        first = second;
        second = curr;
    }

    return second;

    // Top-bottom: recursion
    // const memo = {}
    // const dp = (step) => {
    //     if (step === 1 || step === 2) return step;
    //     if (memo[step] !== undefined) return memo[step];
        
    //     memo[step] = dp(step -1) + dp(step-2);
    //     return memo[step];
    // }

    // return dp(n)
};

// basic DP problem

// if n is 2? 
// - two n-1 
// - one n-2
// so \U0001f449 Recurrence relation: ways(n)=ways(n−1)+ways(n−2)
// also called 점화식, recurrence formula

// 1. Bottom-Up approach
// - base cases up to the target value n
// - use itration
// - can be optimized to use constant space

// 2. Top-bottom aprroach: memoization
// - uses recursion
// - storing the results in a memoization structure (extra space, O(n))
// - use for overlapping subproblems (if it fits a recursive pattern)