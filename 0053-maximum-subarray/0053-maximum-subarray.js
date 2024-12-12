/**
 * @param {number[]} nums
 * @return {number}
 */
var maxSubArray = function(nums) {
    let currentSum = 0;
    let maxSum = nums[0];

    nums.forEach(num => {
        currentSum = Math.max(num, currentSum + num);
        if (maxSum < currentSum) maxSum = currentSum;
    })

    return maxSum;
};