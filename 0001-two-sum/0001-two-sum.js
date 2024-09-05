// O(N^2)
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
var twoSum = function(nums, target) {
    let result = [];
    nums.forEach((num, idx) => {
        if(result.length === 2) return;
        const pair = target - num;
        const pairIndex = nums.findIndex(e => e === pair);
        if(pairIndex !== -1 && idx !== pairIndex) result = [idx, pairIndex]
    })
    return result;
};