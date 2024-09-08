/**
 * @param {number[]} nums
 * @param {number} k
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var rotate = function(nums, k) {
    const n = k % nums.length

    const newNums = nums.splice(nums.length - n, nums.length)
    nums.unshift(...newNums)
};