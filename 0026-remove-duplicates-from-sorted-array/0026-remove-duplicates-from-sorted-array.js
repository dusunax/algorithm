/**
 * @param {number[]} nums
 * @return {number}
 */
var removeDuplicates = function(nums) {
    const uniqueNums = [...new Set(nums)];
    
    nums.length = 0;
    nums.push(...uniqueNums);
    
    return uniqueNums.size;
};