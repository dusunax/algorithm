// O(N^2)
/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    const result = [];
    nums.forEach((num, idx) => {
        nums.forEach((e, nestIdx) => {
            if(idx !== nestIdx){
                if(num + e === target) result.push(idx);
            }
        })
    })
    return result;
};