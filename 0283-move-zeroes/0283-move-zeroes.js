/**
 * @param {number[]} nums
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var moveZeroes = function(nums) {
    let lastNonZero = 0 // slow pointer
    for(current = 0; current < nums.length; current++){
        if(nums[current] !== 0) {
            [nums[lastNonZero], nums[current]] = [nums[current], nums[lastNonZero]];
            lastNonZero++;
        }
    }
};