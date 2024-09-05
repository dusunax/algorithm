// \U0001f449 Brute Force
// Time complexity: O(n^2)
// Space complexity: O(1)
/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
// var twoSum = function(nums, target) {
//     const result = [];
//     nums.forEach((num, idx) => {
//         if(result.length === 2) return;
//         nums.forEach((e, nestIdx) => {
//             if(idx !== nestIdx){
//                 if(num + e === target) result.push(idx);
//             }
//         })
//     })
//     return result;
// };
//
// var twoSum = function(nums, target) {
//     let result = [];
//     nums.forEach((num, idx) => {
//         if(result.length === 2) return;
//         const pair = target - num;
//         const pairIndex = nums.findIndex(e => e === pair);
//         if(pairIndex !== -1 && idx !== pairIndex) result = [idx, pairIndex]
//     })
//     return result;
// };

// \U0001f449 Two-pass Hash Table
// Time complexity: O(n)
// Space complexity: O(n)
var twoSum = function(nums, target) {
    let result = [];

    let numsMap = {};
    for (let i = 0; i < nums.length; i++) {
        numsMap[nums[i]] = i;
    }

    nums.forEach((num, idx) => {
        if(result.length === 2) return;
        const pairNum = target - num;
        if(numsMap[pairNum] !== undefined && numsMap[pairNum] !== idx){
            result = [numsMap[pairNum], idx]
        }
    })
    return result;
};