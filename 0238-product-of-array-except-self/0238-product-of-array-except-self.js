/**
 * @param {number[]} nums
 * @return {number[]}
 */
var productExceptSelf = function(nums) {
    const n = nums.length;
    const answer = new Array(n).fill(1);
    
    // prefix
    for (let i = 1; i < n; i++) {
        answer[i] = answer[i - 1] * nums[i - 1] 
    }

    // suffix
    let suffix_product = 1
    for (let i = n - 1; i > -1; i--) {
        answer[i] *= suffix_product;
        suffix_product *= nums[i]
    }

    return answer
};